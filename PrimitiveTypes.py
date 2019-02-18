def ToText(rawtext):
    txtState = False
    rawtext = str(rawtext)
    text = ""
    for ct in range(len(rawtext)):
        if rawtext[ct] == '"' and txtState == False:
            txtState = True
        elif rawtext[ct] != '"' and txtState == True:
            text += rawtext[ct]
        elif rawtext[ct] == '"' and txtState == True:
            txtState = False
    return str(text)


def ToNum(rawnum):
    return float(rawnum)


def IsNum(expr):
    if expr.isnumeric():
        return True
    else:
        return False

def IsText(expr):
    if not expr.isnumeric() and not IsBin(expr):
        return True
    else:
        return False


def IsBin(expr):
    if expr == '0b' or expr == '1b':
        return True
    else:
        return False


def setType(val):
    if IsBin(val):
        if val == '0b':
            return False
        elif val == '1b':
            return True
    elif IsText(val):
        return ToText(val)
    elif IsNum(val):
        return ToNum(val)
