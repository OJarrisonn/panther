from Analyser import Lexer
from Analyser import Interpreter
src = open("main.pth", "r")


def main():
    Interpreter(Lexer(src))


main()
