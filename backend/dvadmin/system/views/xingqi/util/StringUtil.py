import re

def tripString(text):


    if text is None:
        return ""
    elif not isinstance(text, str):
        return ""
    else:
        return re.sub(r"\s+", "", text)

def isEmptyOrNone(text):
    if text is None:
        return True
    elif not isinstance(text, str):
        return True
    elif len(text) == 0:
        return True
    elif len(tripString(text)) == 0:
        return True
    else:
        return False