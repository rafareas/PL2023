import ply.lex as lex

# Lista de tokens
tokens = [
    'INT', 'ID', 'FUNCTION', 'PROGRAM', 'FOR', 'IN', 'RANGE',
    'PRINT', 'LBRACE', 'RBRACE', 'LPAREN', 'RPAREN', 'SEMICOLON', 'COMMA',
    'PLUS', 'MINUS', 'TIMES', 'DIVIDE', 'ASSIGN', 'EQ', 'LT', 'GT',
    'LTE', 'GTE', 'NEQ', 'COMMENT', 'WS'
]

# Regras de expressão regular para tokens simples
t_LBRACE = r'{'
t_RBRACE = r'}'
t_LPAREN = r'\('
t_RPAREN = r'\)'
t_SEMICOLON = r';'
t_COMMA = r','
t_PLUS = r'\+'
t_MINUS = r'-'
t_TIMES = r'\*'
t_DIVIDE = r'/'
t_ASSIGN = r'='
t_EQ = r'=='
t_LT = r'<'
t_GT = r'>'
t_LTE = r'<='
t_GTE = r'>='
t_NEQ = r'!='

# Regra para identificar números inteiros
def t_INT(t):
    r'\d+'
    t.value = int(t.value)
    return t

# Regra para identificar identificadores
def t_ID(t):
    r'[a-zA-Z_][a-zA-Z0-9_]*'
    t.type = reserved.get(t.value, 'ID')
    return t

# Regras para palavras reservadas
reserved = {
    'int': 'INT',
    'function': 'FUNCTION',
    'program': 'PROGRAM',
    'for': 'FOR',
    'in': 'IN',
    'range': 'RANGE',
    'print': 'PRINT',
}

# Regras para ignorar comentários e espaços em branco
def t_COMMENT(t):
    r'//.*'
    pass

def t_WS(t):
    r'\s+'
    pass

# Regra para lidar com erros de tokenização
def t_error(t):
    print(f'Caractere ilegal {t.value[0]}')
    t.lexer.skip(1)

# Instanciando o analisador léxico
lexer = lex.lex()

# Testando o analisador léxico com um código de exemplo
code = """
/* factorial.p
-- 2023-03-20 
-- by jcr
*/

int i;

// Função que calcula o factorial dum número n
function fact(n){
  int res = 1;
  while res > 1 {
    res = res * n;
    res = res - 1;
  }
}

// Programa principal
program myFact{
  for i in [1..10]{
    print(i, fact(i));
  }
}
"""

# Passando o código para o analisador léxico
lexer.input(code)

# Imprimindo a lista de tokens encontrados
for token in lexer:
    print(token)
