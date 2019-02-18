import PrimitiveTypes as PT
VARS = {'1b': True, '0b': False}


def setVar(args):
    args = args.split('=')
    name = args[0].rstrip().lstrip()
    value = PT.setType(args[1].rstrip().lstrip())
    VARS[name] = value

def getVar(name):
    if name in VARS:
        return VARS.get(name)
    else:
        return False
