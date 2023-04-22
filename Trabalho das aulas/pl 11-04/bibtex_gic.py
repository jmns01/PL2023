import sys
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
import ply.yacc as yacc
from bibtex_lex import tokens

def p_grammar(p):
	"""                                      
	bibtex      : referencias                     
	referencias : referencias referencia     
	            |                             
	referencia  : TIPOreg '{' PAL ',' campos '}'       
	campos      : campos ',' campo               
	campos      : campo              
	campo       : PAL SEP  TEXTO                  
	"""
	
#campos : campo outrosC  # { PAL }
#outrosC : ',' campos     # { , }            
#outrosC : €              # { '}' }

def p_error(p):
    print("Syntax error in input!",p)
    parser.success=False

parser = yacc.yacc()
parser.success=True

source = ""
#for linha in sys.stdin:
#	source += linha
f = open("bibtex.txt",encoding="utf-8")
for linha in f:
	source += linha

parser.parse(source)
#print(source)
if parser.success:
   print('Parsing completed!')
else:
   print('Parsing failed!')

#result = parser.parse(source)
#print(result)


