FROM ubuntu:22.04
WORKDIR /usr/local/script

# установка python и pip для зависимостей
RUN apt update && apt install python3 python3-pip -y

# установка зависимостей
COPY requirements.txt ./
RUN pip install -r requirements.txt

COPY main.py ./

# автоматический запуск скрипта
CMD ["python3", "main.py"]
