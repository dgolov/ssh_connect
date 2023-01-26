# SSH Connector

### Description:

Асинхронно подключается к списку удаленных серверов указанных во входном файле hosts.json и выполняет указанные команды.
По окончинию работы записывает результат команд в файл result.txt в формате host: stdout

Пример можно посмотреть в hosts.json.example

С помощью данного скрипта можно автоматизировать процесс проверки устаревшие версии ПО на серверах инфраструктуры

### Usage:
```
python3 -m venv venv
. /venv/bin/activate OR /venv/Scripts/activate.bat (For Windows)
pip install -r requirements.txt
python connect.py
```

## Technologies used:

- Python3.9
- asyncssh
- asyncio