# SSH Connector

### Description:

Асинхронно подключается к списку удаленных серверов указанных во входном файле hosts.json и выполняет указанные команды.
По окончинию работы записывает результат команд в файл result.txt в формате host: stdout

Пример входного файла можно посмотреть в hosts.example.json

С помощью данного скрипта можно автоматизировать процесс проверки устаревших версий ПО на серверах инфраструктуры компании.

### Usage:

1. Install requirements 

```
python3 -m venv venv
. /venv/bin/activate OR /venv/Scripts/activate.bat (For Windows)
pip install -r requirements.txt
```

2. Add host.json

3. Run application

```
python connect.py
```

## Technologies used:

- Python3.9
- asyncssh
- asyncio