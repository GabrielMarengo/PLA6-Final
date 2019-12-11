import socket


def create_socket():
    print('Client created')
    return socket.socket(socket.AF_INET, socket.SOCK_STREAM)


def connect(s):
    s.connect(("127.0.0.1", 8080))
    print('Established connection to 127.0.0.1')


def receive(s):
    msg = s.recv(8080)
    print("Received message: {}".format(msg.decode("utf-8")))


def close(s):
    s.close()
    print('Disconnected')