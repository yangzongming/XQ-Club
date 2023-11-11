import re

def tripString(text):
    return re.sub(r"\s+", "", text)

def isEmptyOrNone(text):
    if text is None:
        return True
    elif len(text) == 0:
        return True
    elif len(tripString(text)) == 0:
        return True
    else:
        return False