import socket


def create_socket():
    print('Server created')
    return socket.socket(socket.AF_INET, socket.SOCK_STREAM)


def bind(s):
    # port = int(input('Type port: '))
    s.bind(('', 8080))
    print('Binded socket')


def listen(s):
    s.listen(5)
    print('listening...')


def accept(s):
    print('Connection established')
    conn, address = s.accept()
    return conn, address


def send(connection):
    msg = input("Enter message: ")
    connection.send(msg.encode())
    print('Message sent')


def close(s):
    s.close()
    print('Session terminated')
