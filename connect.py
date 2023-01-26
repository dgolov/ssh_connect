import asyncio
import asyncssh
import json
import re

from typing import Union, Any


async def connect(host_name: str, username: str, secret: str, command: str, port: int = 22) -> tuple:
    """ Connect to server and run command
    :param host_name: 192.168.1.1 (For example)
    :param username: user
    :param secret: password
    :param command: docker -v
    :param port: ssh port
    :return: host_name + command result
    """
    print(f"[#] Connect to {host_name}")
    try:
        conn = await asyncio.wait_for(
            asyncssh.connect(host=host_name, username=username, password=secret, port=port),
            timeout=10
        )
        print(f"[#] Connect to {host_name} - Successfully")
    except asyncio.TimeoutError:
        print(f"[#] Connect to {host_name} - Timeout Error")
        return None, None

    async with conn:
        result = await conn.run(command, check=True)
    return host_name, result.stdout


def create_out_file(stdout_results: Union[list, Any]) -> None:
    """ Creating result file
        format -  host: stdout
    :param stdout_results: tasks result
    :return: None
    """
    with open('result.txt', 'w', encoding='utf-8') as out_file:
        for result in stdout_results:
            if not result[0]:
                continue
            line = f"{result[0]}: {result[1]}"
            if not line.endswith('\n'):
                line += '\n'
            out_file.write(line)


async def main(hosts: dict) -> None:
    """ Main function
    :param hosts: host from json file
    :return: None
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
