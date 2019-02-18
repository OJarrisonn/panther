import Vars
def bPrint(textMsg):
    varStart = 'nil'
    varEnd = 'nil'
    var = ''
    for ct in range(len(textMsg)):
        if textMsg[ct] == '[' and varStart == 'nil':
            varStart = ct
        elif textMsg[ct] == ']' and varEnd == 'nil':
            varEnd = ct
        if varStart != 'nil' and varEnd != 'nil':
            var = textMsg[varStart+1:varEnd]
            varStart = 'nil'
            varEnd = 'nil'
            textMsg = textMsg.replace('[{}]'.format(var), Vars.VARS.get(var))
    print(textMsg)


def bSet(args):
    Vars.setVar(args)
