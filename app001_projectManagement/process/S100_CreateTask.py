"""
サービスクラス
S100_CreateTask

戻り値：{共通項目、任意項目1、任意項目2、...}
        └共通項目：{実行結果（エラーフラグ）、メッセージリスト}

"""

import datetime
from . import C010_Const,C020_DBUtil,C030_MessageUtil

SERVICE_ID = "S100"

def main(projectID,taskTitle,taskDetail,naiyo,tantsh,kihyDate,kignDate,taskStatus,crtUserID):
    #--戻り値用の変数宣言------------------------------------------------------------------------------
    errflg = "0"
    list_msgInfo = []
    json_shitsmnInfo = {}
    #------------------------------------------------------------------------------------------------
    try:
        #--DB連携基本コード----------------------------------------------------------------------------
        #DB接続開始、コネクションとカーソルを取得
        json_DBConnectInfo = C020_DBUtil.connectDB()

        #--(1)採番処理-----------------------------------------------------------------------------
        sql_rqSeq = "select IFNULL(MAX(SEQ),0) + 1 as NEWSEQ from T110_TASK where PROJECTID = %s ;"
        args_rqSeq = (projectID,)
        int_seq = C020_DBUtil.executeSQL(json_DBConnectInfo,sql_rqSeq,args_rqSeq)[0]["NEWSEQ"]
        #--採番処理呼び出し----------------------------------------------------------------------------

        #--(2.2.)クエリとパラメータを定義
        sql = "INSERT INTO T110_TASK VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,current_timestamp(6),%s,%s,current_timestamp(6),%s);"
        args = (projectID,int_seq,taskTitle,taskDetail,naiyo,tantsh,kihyDate,kignDate,taskStatus,SERVICE_ID,crtUserID,SERVICE_ID,crtUserID,"0",)
        #クエリを実行し、結果を取得
        #T100
        C020_DBUtil.executeSQL(json_DBConnectInfo,sql,args)
        #DB接続終了
        C020_DBUtil.closeDB(json_DBConnectInfo,errflg)
        #--------------------------------------------------------------------------------------------
        #メッセージがある場合はリストに追加
        #--------------------------------------------------
        msgID_01 = "S0002"
        tuple_msgPalams_01 = ("登録",)
        msgInfo_01 = C030_MessageUtil.getMessageInfo(msgID_01,tuple_msgPalams_01)
        list_msgInfo.append(msgInfo_01)
        #--------------------------------------------------
        #戻り値の共通項目を作成
        json_CommonInfo = {"errflg":errflg, "list_msgInfo" : list_msgInfo}
        #戻り値を作成
        json_service = {"json_CommonInfo":json_CommonInfo,"projectID":projectID,"int_seq":int_seq}
        return json_service
    #==例外処理==========================================================================================
    except C020_DBUtil.MySQLDBException as e :
        #エラーフラグを立てる
        errflg = "1"
        #DB接続終了（ロールバック）
        C020_DBUtil.closeDB(json_DBConnectInfo,errflg)
        raise
    except Exception as e :
        raise
    #====================================================================================================
