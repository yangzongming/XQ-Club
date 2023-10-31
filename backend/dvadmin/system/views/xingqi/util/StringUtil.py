import re

def tripString(text):
    return re.sub(r"\s+", "", text)