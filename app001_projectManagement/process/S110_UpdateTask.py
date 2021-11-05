"""
サービスクラス
S110_UpdateTask

戻り値：{共通項目、任意項目1、任意項目2、...}
        └共通項目：{実行結果（エラーフラグ）、メッセージリスト}

"""

from . import C010_Const,C020_DBUtil,C030_MessageUtil,C050_StringUtil


SERVICE_ID = "110"

def main(projectID,seq,taskTitle,taskDetail,naiyo,tantsh,kihyDate,kignDate,taskStatus,updUserID):
    #--戻り値用の変数宣言------------------------------------------------------------------------------
    errflg = "0"
    list_msgInfo = []
    #json_Info = {}
    #------------------------------------------------------------------------------------------------
    try:
        #--DB連携基本コード----------------------------------------------------------------------------
        #DB接続開始、コネクションとカーソルを取得
        json_DBConnectInfo = C020_DBUtil.connectDB()
        #--(2)クエリとパラメータを定義
        list_args = []
        sql = "update T110_TASK set "
        if not C050_StringUtil.isNull(taskTitle):
            sql = sql + "TASKTITLE = %s , "
            list_args.append(taskTitle)
        if not C050_StringUtil.isNull(taskDetail):
            sql = sql + "TASKDETAIL = %s , "
            list_args.append(taskDetail)
        if not C050_StringUtil.isNull(naiyo):
            sql = sql + "NAIYO = %s , "
            list_args.append(naiyo)
        if not C050_StringUtil.isNull(tantsh):
            sql = sql + "TANTSH = %s , "
            list_args.append(tantsh)
        if not C050_StringUtil.isNull(kihyDate):
            sql = sql + "KIHYO_DATE = %s , "
            list_args.append(kihyDate)
        if not C050_StringUtil.isNull(kignDate):
            sql = sql + "KIGN_DATE = %s , "
            list_args.append(kignDate)
        if not C050_StringUtil.isNull(taskStatus):
            sql = sql + "TASKSTATUS = %s , "
            list_args.append(taskStatus)

        sql = sql + "UPDSRV = %s , "
        list_args.append(SERVICE_ID)
        sql = sql + "UPDUSR = %s , "
        list_args.append(updUserID)
        sql = sql + "UPDDATE = current_timestamp(6)  "
        sql = sql + "where PROJECTID = %s and SEQ = %s;"
        list_args.append(projectID)
        list_args.append(seq)

        args = tuple(list_args)
        #クエリを実行し、結果を取得
        C020_DBUtil.executeSQL(json_DBConnectInfo,sql,args)
        #DB接続終了
        C020_DBUtil.closeDB(json_DBConnectInfo,errflg)
        #--------------------------------------------------------------------------------------------
        #メッセージがある場合はリストに追加
        #--------------------------------------------------
        msgID_01 = "S0002"
        tuple_msgPalams_01 = ("課題の更新",)
        msgInfo_01 = C030_MessageUtil.getMessageInfo(msgID_01,tuple_msgPalams_01)
        list_msgInfo.append(msgInfo_01)
        #--------------------------------------------------
        #戻り値の共通項目を作成
        json_CommonInfo = {"errflg":errflg, "list_msgInfo" : list_msgInfo}
        #戻り値を作成
        json_service = {"json_CommonInfo":json_CommonInfo,"projectID":projectID,"seq":seq}
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


def updateDelflg(projectID,seq,updUserID):
    #--戻り値用の変数宣言------------------------------------------------------------------------------
    errflg = "0"
    list_msgInfo = []
    #json_Info = {}
    #------------------------------------------------------------------------------------------------
    try:
        #--DB連携基本コード----------------------------------------------------------------------------
        #DB接続開始、コネクションとカーソルを取得
        json_DBConnectInfo = C020_DBUtil.connectDB()
        #--(2)クエリとパラメータを定義
        sql = "update T110_TASK set UPDSRV = %s , UPDUSR = %s , UPDDATE = current_timestamp(6), DELFLG = %s where PROJECTID = %s and SEQ = %s;"
        #パラメータを定義
        args = (SERVICE_ID,updUserID,"1",projectID,seq,)
        #クエリを実行し、結果を取得
        C020_DBUtil.executeSQL(json_DBConnectInfo,sql,args)
        #DB接続終了
        C020_DBUtil.closeDB(json_DBConnectInfo,errflg)
        #--------------------------------------------------------------------------------------------
        #メッセージがある場合はリストに追加
        #--------------------------------------------------
        msgID_01 = "S0002"
        tuple_msgPalams_01 = ("課題の削除",)
        msgInfo_01 = C030_MessageUtil.getMessageInfo(msgID_01,tuple_msgPalams_01)
        list_msgInfo.append(msgInfo_01)
        #--------------------------------------------------
        #戻り値の共通項目を作成
        json_CommonInfo = {"errflg":errflg, "list_msgInfo" : list_msgInfo}
        #戻り値を作成
        json_service = {"json_CommonInfo":json_CommonInfo,"projectID":projectID,"seq":seq}
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