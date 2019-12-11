import ply.yacc as yacc
import server
import client
import lexer
import socket

tokens = lexer.tokens

ids = {}
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
conn = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
address = ('', 0)


# Parsing Rules
def p_statement(p):
    """
    statement : open_client
            | open_server
            | send
            | close_client
            | accept
            | close_server
            | close
    """


def p_error(p):
    if p:
        print("Syntax error at '%s'" % p.value)
    else:
        print("Syntax error at EOF")


def p_open_client(p):
    """open_client : OPEN_CLIENT"""
    client.create_socket()


def p_open_server(p):
    """open_server : OPEN_SERVER"""
    server.create_socket()
    server.bind(server_socket)
    server.listen(server_socket)
    client.connect(client_socket)


def p_send(p):
    """send : SEND"""
    server.send(conn)
    client.receive(client_socket)


def p_client_close(p):
    """close_client : CLOSE_CLIENT"""
    client.close(client_socket)


def p_accept(p):
    """accept : ACCEPT"""
    return server.accept(server_socket)


def p_server_close(p):
    """close_server : CLOSE_SERVER"""
    server.close(server_socket)


def p_close(p):
    """close : CLOSE"""
    print("Terminating program...")
    exit(0)



yacc.yacc()
while True:
    s = input('Communicastions Language >> ')
    if s == 'open_client':
        p_open_client(client_socket)
    elif s == 'open_server':
        p_open_server(server_socket)
        conn, address = p_accept(server_socket)
    elif s == 'send':
        p_send(conn)
    elif s == 'close_client':
        p_client_close(client_socket)
    elif s == 'close_server':
        p_server_close(server_socket)
    elif s == 'open_communications':
        p_open_client(client_socket)
        p_open_server(server_socket)
        conn, address = p_accept(server_socket)
        p_send(conn)
    elif s == 'close':
        p_client_close(client_socket)
        p_server_close(server_socket)
        p_close(None)
