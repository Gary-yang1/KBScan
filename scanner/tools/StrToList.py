import re


def toList(KBNum_str):
    KB_list = re.findall(r'KB[0-9]\d{6}', KBNum_str)
    return KB_list
