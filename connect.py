import asyncio
import asyncssh


async def connect(host_name: str, username: str, secret: str, command: str, port: int = 22) -> str:
    """ Connect to server and run command
    :param host_name: 192.168.1.1 (For example)
    :param username: user
    :param secret: password
    :param command: docker -v
    :param port: ssh port
    :return: command result
    """
    async with asyncssh.connect(host=host_name, username=username, password=secret, port=port) as conn:
        result = await conn.run(command, check=True)
    return result.stdout


async def main():
    host = ''
    user = ''
    password = ''
    stdout = await connect(host, user, password, 'docker -v', 222)
    print(stdout)

if __name__ == '__main__':
    asyncio.run(main())
