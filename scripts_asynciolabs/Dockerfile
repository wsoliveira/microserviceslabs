FROM python:3.8
ENV PYTHONUNBUFFERED=1
WORKDIR /code/microserviceslab/AsyncioLabs/
COPY requirements.txt /code/microserviceslab/AsyncioLabs/
RUN pip install -r requirements.txt --no-cache-dir
COPY . /code/microserviceslab/AsyncioLabs/
ENTRYPOINT ["python3"]