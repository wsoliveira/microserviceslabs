FROM python:3.8
ENV PYTHONUNBUFFERED=1
WORKDIR /code/microserviceslab/cadastro/
COPY requirements.txt /code/microserviceslab/cadastro/
RUN pip install -r requirements.txt --no-cache-dir
EXPOSE 8010
COPY . /code/microserviceslab/cadastro/
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8010"]

#docker build -t cadastro .
#docker run -d --name applabs_cadastro -p 8010:8010 cadastro

#uvicorn main:app --port 8010 --reload

#subir para o HUB
#docker login --username wsoliveiraudia
#docker tag cadastro wsoliveiraudia/appcadastro_labs
#docker push wsoliveiraudia/appcadastro_labs