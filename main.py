# ------------------------------------------------------------
# calclex.py
#
# tokenizer for a simple expression evaluator for
# numbers and +,-,*,/
# ------------------------------------------------------------
import ply.lex as lex

# r'atring' -> r significa que la cadena es tradada sin caracteres de escape, 
# es decir r'\n' seria un \ seguido de n (no se interpretaria como salto de linea) 

#palabras reservadas
reserved = {
    'main': 'type_main',
    'int': 'type_int',
    'bool': 'type_bool',
    'float': 'type_float',
    'string': 'type_string',
    'char': 'type_char',
    'double': 'type_double',
    'long': 'type_long',
    'in': 'type_input',
    'out': 'type_ouput',
    'return': 'return_value',
    'if':  'type_struct_if',
    'else': 'type_struct_else',
    'while': 'type_struct_while',
    'do':'type_struct_do',
    'for': 'type_struct_for'
}

 # List of token names.   This is always required
tokens = [
    'num',
    'suma',
    'resta',
    'multi',
    'division',
    'parent_der',
    'parent_izq',
    'igual',
    'modulo',
    'op_mayor',
    'op_menor',
    'op_mayorq',
    'op_menorq',
    'llave_der',
    'llave_izq',
    'punto',
    'punto_coma',
    'coma',
    'id',
    'decremento',
    'incremento',
    'diferente',
    'dez_izq',
    'dez_der',
    'operador_and',
    '2puntos',
    'comentario_lineal',
    'literal',
    'decimal',
    'comentario_multilineal',
    'booleano',
] + list (reserved.values())

 # Regular expression rules for simple tokens
t_suma    = r'\+'
t_resta   = r'-'
t_multi   = r'\*'
t_division  = r'/'
t_parent_der  = r'\('
t_parent_izq  = r'\)'
t_igual  = r'='
t_modulo  = r'\%'
t_op_mayor  = r'>'
t_op_menor  = r'<'
t_op_mayorq = r'\>='
t_op_menorq = r'\<='
t_llave_der = r'\{'	
t_llave_izq = r'\}'
t_punto_coma = r';'
t_punto = r'\.'
t_coma = r','
t_incremento = r'\++'
t_decremento = r'\--'
t_diferente = r'!='
t_dez_izq = r'\<<'
t_dez_der = r'\>>'
t_operador_and = r'\&&'
t_2puntos = r'\:'
t_comentario_lineal = r'\/\/.*'
t_literal = r"'[^']*'"
#t_id = r'([a-zA-Z]|_)([a-zA-Z]|[0-9]|_)*'
t_decimal = r'[0-9]+\.[0-9]+'
t_comentario_multilineal = r'/\*(.|\n)*?\*/'

#t_num  = r'\d+'

 # A regular expression rule with some action code

def t_num(t):
    r'\d+'
    t.value = int(t.value)  # guardamos el valor del lexema  
    #print("se reconocio el numero")
    return t

 # Define a rule so we can track line numbers
def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

#definicion para boolenano
def t_booleano(t):
  r'false|true'
  return t
  
def t_id(t):
  r'[a-zA-Z_]+ ( [a-zA-Z0-9_]* )'
  t.type = reserved.get(t.value, 'id')  # Check for reserved words
  return t


 # A string containing ignored characters (spaces and tabs)
t_ignore  = ' \t'

 # Error handling rule
def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)

# Build the lexer
lexer = lex.lex()

from tabulate import tabulate

def tokenize_file(file_path):
    with open(file_path, 'r') as file:
        data = file.read()
        lexer.input(data)
        tokens_list = []
        while True:
            tok = lexer.token()
            if not tok:
                break
            tokens_list.append({'Tipo': tok.type, 'Lexema': tok.value, 'Linea': tok.lineno, 'Columna': tok.lexpos})
        return tokens_list

# Test the function
#file_path = 'hola.txt' 
#file_path = 'uso_estructuras.txt' 
file_path = 'uso_funciones.txt' 
tokens = tokenize_file(file_path)

# Convertir la lista de tokens en formato de tabla
table = tabulate(tokens, headers='keys', tablefmt='grid')

# Imprimir la tabla
print(table)
