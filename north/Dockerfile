FROM python:3.12.2-slim-bookworm

WORKDIR /application
#Копируем в контейнер файл питоняшечьих зависимостей
COPY . /application
RUN apt-get update && apt-get install -y curl && rm -rf /var/lib/apt/lists/*
RUN pip3 install -r requirements.txt

RUN chmod +x ./entrypoint.sh

CMD [ "./entrypoint.sh" ]