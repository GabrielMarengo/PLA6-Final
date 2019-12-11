import ply.lex as lex

# Reserved Words
reserved = {'create_client': 'OPEN_CLIENT',
    'open_server': 'OPEN_SERVER',
    'send': 'SEND',
    'close_client': 'CLOSE_CLIENT',
    'accept': 'ACCEPT',
    'close_server': 'CLOSE_SERVER',
    'close': 'CLOSE',
}

# Tokens
tokens = [] + list(reserved.values())

# Regular Expressions
t_ignore = '\t'


# Define a rule so we can track line numbers
def t_newline(t):
    r"""
    \n+
    """
    t.lexer.lineno += len(t.value)


def t_error(t):
    print('Illegal character %s', t.value[0])
    t.lexer.skip(1)
    return t


# Build the lexer
lexer = lex.lex()
