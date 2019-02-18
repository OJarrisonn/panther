import Builtins
import PrimitiveTypes


def Tokenizer(line):
    tk = {'key': '', 'args': ''}
    sj = line.find(':')
    tk['key'] = line[:sj].rstrip().lstrip()
    tk['args'] = line[sj+1:].rstrip().lstrip()
    return tk


def Interpreter(toks):
    for i in range(len(toks)):
        if toks[i]['key'] == 'print':
            Builtins.bPrint(PrimitiveTypes.ToText(toks[i]['args']))
        elif toks[i]['key'] == 'set':
            Builtins.bSet(toks[i]['args'])


def Lexer(file):
    src = file.readlines()
    for s in range(len(src)):
        if src[s].endswith('\n'):
            src[s] = src[s][:-2]
        if '\'' in src[s]:
            src[s] = src[s].replace('\'', "'")
        src[s] = Tokenizer(src[s])
    return src
