import schedule
import time
import os
from loguru import logger
from mongo import run_backup
from dotenv import load_dotenv

load_dotenv()

def take_backup():
    logger.info("taking backup from mongo database...")
    run_backup(os.getenv("MONGO_URI"),os.getenv("MONGO_DB_NAME"))
    logger.info("backup completed")

logger.info("application starting...")
print(os.getenv("BACKUP_CRON"))
if os.getenv("BACKUP_CRON") == "daily" or os.getenv("BACKUP_CRON") == "DAILY" or os.getenv("BACKUP_CRON") == None or os.getenv("BACKUP_CRON") == "":
    if os.getenv("DAILY_HOUR") == "" or os.getenv("DAILY_HOUR") == None :
        schedule.every().day.at("00:30").do(take_backup)
        logger.info("backup cron set to everday 00:30")
    else:
        schedule.every().day.at(os.getenv("DAILY_HOUR")).do(take_backup)
        logger.info("backup cron set to everday " + os.getenv("DAILY_HOUR") )
elif os.getenv("BACKUP_CRON") == "hourly" or os.getenv("BACKUP_CRON") == "HOURLY":
    schedule.every().hour.do(take_backup)
    logger.info("backup cron set to every hour")
elif os.getenv("BACKUP_CRON") == "weekly" or os.getenv("BACKUP_CRON") == "WEEKLY":
    if os.getenv("WEEKLY_DAY") == "" or os.getenv("WEEKLY_DAY") == None:
        schedule.every().sunday.at("00.30").do(take_backup)
        logger.info("backup cron set to every sunday 00:30")
    else:
        if os.getenv("WEEKLY_DAY") == "monday":
            if os.getenv("WEEKLY_HOUR") == "" or os.getenv("WEEKLY_HOUR") == None:
                schedule.every().monday.at("00.30").do(take_backup)
                logger.info("backup cron set to every monday 00:30" )
            else:
                schedule.every().monday.at(os.getenv("WEEKLY_HOUR")).do(take_backup)
                logger.info("backup cron set to every monday " + os.getenv("WEEKLY_HOUR") )
        elif os.getenv("WEEKLY_DAY") == "tuesday":
            if os.getenv("WEEKLY_HOUR") == "" or os.getenv("WEEKLY_HOUR") == None:
                schedule.every().tuesday.at("00.30").do(take_backup)
                logger.info("backup cron set to every tuesday 00:30" )
            else:
                schedule.every().tuesday.at(os.getenv("WEEKLY_HOUR")).do(take_backup)
                logger.info("backup cron set to every tuesday " + os.getenv("WEEKLY_HOUR") )
        elif os.getenv("WEEKLY_DAY") == "wednesday":
            if os.getenv("WEEKLY_HOUR") == "" or os.getenv("WEEKLY_HOUR") == None:
                schedule.every().wednesday.at("00.30").do(take_backup)
                logger.info("backup cron set to every wednesday 00:30" )
            else:
                schedule.every().wednesday.at(os.getenv("WEEKLY_HOUR")).do(take_backup)
                logger.info("backup cron set to every wednesday " + os.getenv("WEEKLY_HOUR") )
        elif os.getenv("WEEKLY_DAY") == "friday":
            if os.getenv("WEEKLY_HOUR") == "" or os.getenv("WEEKLY_HOUR") == None:
                schedule.every().friday.at("00.30").do(take_backup)
                logger.info("backup cron set to every friday 00:30" )
            else:
                schedule.every().friday.at(os.getenv("WEEKLY_HOUR")).do(take_backup)
                logger.info("backup cron set to every friday " + os.getenv("WEEKLY_HOUR") )
        elif os.getenv("WEEKLY_DAY") == "saturday":
            if os.getenv("WEEKLY_HOUR") == "" or os.getenv("WEEKLY_HOUR") == None:
                schedule.every().saturday.at("00.30").do(take_backup)
                logger.info("backup cron set to every saturday 00:30" )
            else:
                schedule.every().saturday.at(os.getenv("WEEKLY_HOUR")).do(take_backup)
                logger.info("backup cron set to every saturday " + os.getenv("WEEKLY_HOUR") )
        elif os.getenv("WEEKLY_DAY") == "sunday":
            if os.getenv("WEEKLY_HOUR") == "" or os.getenv("WEEKLY_HOUR") == None:
                schedule.every().sunday.at("00.30").do(take_backup)
                logger.info("backup cron set to every sunday 00:30" )
            else:
                schedule.every().sunday.at(os.getenv("WEEKLY_HOUR")).do(take_backup)
                logger.info("backup cron set to every sunday " + os.getenv("WEEKLY_HOUR") )
elif os.getenv("BACKUP_CRON") == "minutely" or os.getenv("BACKUP_CRON") == "MINUTELY":
    logger.info("backup cron set to every minute" )
    schedule.every().minute.do(take_backup)

while True:
    schedule.run_pending()
    time.sleep(1)