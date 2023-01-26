import asyncio
import asyncssh


async def connect(host_name: str, username: str, secret: str, command: str, port: int = 22) -> tuple:
    """ Connect to server and run command
    :param host_name: 192.168.1.1 (For example)
    :param username: user
    :param secret: password
    :param command: docker -v
    :param port: ssh port
    :return: host_name + command result
    """
    async with asyncssh.connect(host=host_name, username=username, password=secret, port=port) as conn:
        result = await conn.run(command, check=True)
    return host_name, result.stdout


async def main():
    host = ''
    user = ''
    password = ''
    host2 = ''
    user2 = ''
    password2 = ''

    task1 = connect(host, user, password, 'docker -v', 222)
    task2 = connect(host2, user2, password2, 'docker -v', 222)
    tasks_result = await asyncio.gather(task1, task2)
    print(tasks_result)

if __name__ == '__main__':
    asyncio.run(main())
