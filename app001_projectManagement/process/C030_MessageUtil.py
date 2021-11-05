"""
共通クラス
C030_MessageUtil
メッセージ関連の共通メソッドを格納する

"""
import MySQLdb
from logging import getLogger
import traceback

from django.contrib import messages

from . import C010_Const,C020_DBUtil


"""
★
メッセージ単体をセットする場合に利用。
"""
def setMessage(request,msgID,tuple_msgPalams):
    #メッセージ情報を取得する
    json_MessageInfo = getMessageInfo(msgID,tuple_msgPalams)
    msgLevel = json_MessageInfo["msgLevel"]
    msgNaiyo = json_MessageInfo["msgNaiyo"]
    #取得したメッセージをDjangoのメッセージオブジェクトに格納する
    messages.add_message(request, msgLevel, msgNaiyo)
    return


"""
★
メッセージ情報リストをまとめてセットする場合に利用。サービスの戻り値のメッセージを設定する際に使う。
"""
def setMessageList(request,list_msgInfo):
    for json_MessageInfo in list_msgInfo:
        msgLevel = json_MessageInfo["msgLevel"]
        msgNaiyo = json_MessageInfo["msgNaiyo"]
        messages.add_message(request, msgLevel, msgNaiyo)
    return


"""
★
メッセージ情報を取得する。メッセージ情報リストを作成時などに使える。
"""
def getMessageInfo(msgID,tuple_msgPalams):
    #M020_メッセージマスタからメッセージ情報を取得する。
    json_MessageInfo_DB = getMessageInfo_DB(msgID)
    str_msgLevel = json_MessageInfo_DB["msgLevel"]
    str_msgNaiyo = json_MessageInfo_DB["msgNaiyo"]
    #メッセージレベルを特定する
    int_msgLevel = 0
    if str_msgLevel == "D":
        int_msgLevel = C010_Const.DEBUG
    elif  str_msgLevel == "I":
        int_msgLevel = C010_Const.INFO
    elif  str_msgLevel == "S":
        int_msgLevel = C010_Const.SUCCESS
    elif  str_msgLevel == "W":
        int_msgLevel = C010_Const.WARNING
    elif  str_msgLevel == "E":
        int_msgLevel = C010_Const.ERROR
    #汎用項目の置換
    i = 0
    str_hanyo = ""
    for palam in tuple_msgPalams:
        i = i + 1
        str_hanyo = "@"+str(i)
        str_msgNaiyo = str_msgNaiyo.replace(str_hanyo, palam)
    #戻り値に設定
    json_MessageInfo = {"msgLevel" : int_msgLevel, "msgNaiyo" : str_msgNaiyo}
    return json_MessageInfo


def getMessageInfo_DB(msgID):
    errflg = "0"
    #DB接続開始、コネクションとカーソルを取得
    json_DBConnectInfo = C020_DBUtil.connectDB()
    #クエリを定義
    sql = "SELECT MSGID,MSGLEVEL,MSGNAIYO FROM M020_MSGMST WHERE MSGID = %s and DELFLG = '0' ;"
    args = (msgID,) #tuple型
    #クエリを実行
    rows = C020_DBUtil.executeSQL(json_DBConnectInfo, sql, args)
    #DB接続終了
    C020_DBUtil.closeDB(json_DBConnectInfo,errflg)
    #メッセージレベル、メッセージ内容を取得
    msgLevel = rows[0]["MSGLEVEL"]
    msgNaiyo = rows[0]["MSGNAIYO"]
    #戻り値に設定
    json_MessageInfo_DB = {"msgLevel" : msgLevel, "msgNaiyo" : msgNaiyo}
    return json_MessageInfo_DB


"""
★
DEBUG用。本番環境では不要。
try~exceptで囲むと、コンソールにエラー情報が出ない。これを出力させるためのもの。

def printMessage_traceback():
    
    #開発環境
    print("[システムエラー]：",traceback.format_exc())
    #本番環境
    #何もしない
    return
"""
"""
★
メッセージをログに出力するためのもの。
"""
def loggingMessage_traceback():
    logger = getLogger(__name__)
    #開発環境
    #logger.error(f'TeachersProjectSystemError service_id:{SERVICE_ID}')
    msg = "[システムエラー]：" + traceback.format_exc()
    logger.error(f'{msg}')
    return

def systemErrorCommonMethod():
    #コンソールにエラーを出力
    #printMessage_traceback()
    #ログにエラーを出力
    loggingMessage_traceback()