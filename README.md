# yadro_telecom_internship task

## Раздел 1

Создан Python-скрипт, который делает 5 запросов к сервису [https://httpstat.us] c произвольно выбранными статус-кодами из заданного диапазона (по умолчанию, диапазон состоит из всех статус-кодов)

Скрипт ведет логирование
 - успешных запросов (1xx, 2xx, 3xx) в файл log
 - ошибочных запросов (4xx, 5xx) в файл log и stdout.

Также реализован вывод итоговой статистики в stdout.

Используются библиотеки: requests, logging.

## Раздел 2

Создан Dockerfile на базе образа ubuntu:22.04, в котором

- Устанавливается Python и pip
- Устанавливается необходимые зависимости(requests)
- Автоматические запускает скрипт при запуске

### Сборка и запуск контейнера:

```bash
docker build -t requests-logger .
docker run -d --name <название контейнера> python-requests
```

Работу скрипта можно проверить после запуска командой:

```bash
docker logs <название контейнера>
```

## Раздел 3

Для запуска плейбуков была использована виртуальная машина на Ubuntu Server с предправительно настроенным доступом по SSH

Были написаны:
 - install-docker.yaml - Плейбук для установки Docker на хост, добавления пользователя в группу docker
 - start-script.yaml - Плейбук для сборки и запуска контейнера с Python скриптом
 - Inventory.yaml - содержит IP и пользователя хоста

### Запуск

### Пинг хостов
```bash
ansible -m ping -i inventory.yaml
```

### Установка Docker
```bash
ansible-playbook install-docker.yaml -i inventory.yaml
```

### Запуск контейнера со скриптом
```bash
ansible-playbook start-script.yaml -i inventory.yaml
```
