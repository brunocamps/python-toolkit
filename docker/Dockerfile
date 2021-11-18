FROM python:latest
WORKDIR /app
COPY requirements.txt .

FROM jjanzic/docker-python3-opencv
COPY . /app
WORKDIR /app

EXPOSE 5000/tcp 

RUN pip3 install -r requirements.txt
COPY . .
CMD ["python", "name_of_python_file.py"]