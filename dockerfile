FROM python:latest

WORKDIR /app 

COPY requirements.txt ./
RUN pip install -r requirements.txt

COPY ./example.py ./

ENTRYPOINT [ "python","example.py" ]