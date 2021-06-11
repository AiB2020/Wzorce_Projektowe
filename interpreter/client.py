"The Interpreter Pattern Use Case Example"

from sentence_parser import Parser

SENTENCE = "5 + IV - 3 + VII - 2"

print(SENTENCE)

AST_ROOT = Parser.parse(SENTENCE)

print(AST_ROOT.interpret())

print(AST_ROOT)