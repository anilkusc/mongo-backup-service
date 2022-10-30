FROM  python:3.10.6

WORKDIR /app/
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .
RUN chmod -R 777 /app
ENTRYPOINT [ "python","-u","./main.py" ]