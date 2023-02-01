import asyncio
import asyncssh
import json
import re

from typing import Union, Any


async def connect(host_name: str, username: str, secret: str, command: str, port: int = 22, timeout: int = 5) -> tuple:
    """ Connect to server and run command
    :param host_name: 192.168.1.1 (For example)
    :param username: user
    :param secret: password
    :param command: docker -v
    :param port: ssh port
    :param timeout: ssh timeout
    :return: host_name + command result
    """
    print(f"[#] Connect to {host_name}")
    try:
        conn = await asyncio.wait_for(
            asyncssh.connect(host=host_name, username=username, password=secret, port=port),
            timeout=timeout
        )
        print(f"[#] Connect to {host_name} - Successfully")
    except asyncio.TimeoutError:
        stdout = "Timeout Error"
        print(f"[#] Connect to {host_name} - {stdout}")
    except asyncssh.misc.PermissionDenied:
        stdout = "Permission denied"
        print(f"[#] Connect to {host_name} - {stdout}")
    else:
        async with conn:
            result = await conn.run(command, check=True)
            stdout = result.stdout

    return host_name, stdout


def create_out_file(stdout_results: Union[list, Any]) -> None:
    """ Creating result file
        format -  host: stdout
    :param stdout_results: tasks result
    """
    with open('result.txt', 'w', encoding='utf-8') as out_file:
        for result in stdout_results:
            host, stdout = result
            if not host:
                continue
            line = f"{host}: {stdout}"
            if not line.endswith('\n'):
                line += '\n'
            out_file.write(line)


async def main(hosts: dict) -> None:
    """ Main function
    :param hosts: host from json file
    """
    print("[#] Start application")
    tasks_list = []

    for host, values in hosts.items():
        username = values.get("user")
        password = values.get("password")
        port = values.get("port", 22)
        command = values.get("command")

        if not re.search(r"\b\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}\b", host) \
                or (not username or not password or not command):
            continue
        tasks_list.append(connect(host, username, password, command, port))

    tasks_result = await asyncio.gather(*tasks_list)
    create_out_file(stdout_results=tasks_result)

    print("[#] End")


if __name__ == '__main__':
    with open('hosts.json', 'r') as json_file:
        load_hosts = json.load(json_file)
    asyncio.run(main(hosts=load_hosts))
