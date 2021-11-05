"""
共通クラス
C050_StringUtil
セッション関連の共通メソッドを格納する

"""

def isNull(_str_):
    result = False
    if _str_ == None:
        result = True
    return result

def isEmpty(_str_):
    result = False
    if _str_ == None or _str_ == "":
        result = True
    return result

def isAllSpace(_str_):
    result = False
    if _str_ == None or _str_ == "":
        result = True
    else:
        _str_.replace(" ","")
        _str_.replace("　","")
        if _str_ == "":
            result = True
    return result

def isSameCharacter(str1,str2):
    result = False
    if str1 == str2:
        result = True
    return result