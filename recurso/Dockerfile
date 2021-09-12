FROM python:3.8
ENV PYTHONUNBUFFERED=1
WORKDIR /code/microserviceslab/recurso/
COPY requirements.txt /code/microserviceslab/recurso/
RUN pip install -r requirements.txt --no-cache-dir
EXPOSE 8020
COPY . /code/microserviceslab/recurso/
ENTRYPOINT [ "python" ]

CMD [ "app.py" ]