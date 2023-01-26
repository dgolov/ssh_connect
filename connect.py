import paramiko


def connect(host_name: str, username: str, secret: str, command: str, port: str = '22') -> str:
    """ Connect to server and run command
    :param host_name: 192.168.1.1 (For example)
    :param username: user
    :param secret: password
    :param command: docker -v
    :param port: ssh port
    :return: command result
    """
    client = paramiko.SSHClient()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    client.connect(hostname=host_name, username=username, password=secret, port=port)
    stdin, stdout, stderr = client.exec_command(command=command)
    data = stdout.read() + stderr.read()
    client.close()
    return data
