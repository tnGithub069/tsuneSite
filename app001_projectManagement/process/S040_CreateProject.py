"""
サービスクラス
S040_CreateProject

戻り値：{共通項目、任意項目1、任意項目2、...}
        └共通項目：{実行結果（エラーフラグ）、メッセージリスト}

"""

from . import C010_Const,C020_DBUtil,C030_MessageUtil
from . import S905_SelectSaibnMst

SERVICE_ID = "S040"

def main(urlID,projectName,projectComment,projectNaiyo,projectCrtUserID,userAuthFlg):
    #--戻り値用の変数宣言------------------------------------------------------------------------------
    errflg = "0"
    list_msgInfo = []
    json_shitsmnInfo = {}
    #------------------------------------------------------------------------------------------------
    try:
        #--(1)採番処理呼び出し-----------------------------------------------------------------------------
        tableID_S100 = C010_Const.S100["tableID"]
        header_S100 = C010_Const.S100["header"]
        newID_S100 = S905_SelectSaibnMst.main(tableID_S100,header_S100)["newID"]
        #--採番処理呼び出し----------------------------------------------------------------------------
        #--DB連携基本コード----------------------------------------------------------------------------
        #DB接続開始、コネクションとカーソルを取得
        json_DBConnectInfo = C020_DBUtil.connectDB()
        #--(2.2.)クエリとパラメータを定義
        sql = "INSERT INTO T100_PROJECT VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,current_timestamp(6),%s,%s,current_timestamp(6),%s);"
        args = (newID_S100,urlID,projectName,projectComment,projectNaiyo,projectCrtUserID,userAuthFlg,SERVICE_ID,projectCrtUserID,SERVICE_ID,projectCrtUserID,"0",)
        #クエリを実行し、結果を取得
        #T100
        C020_DBUtil.executeSQL(json_DBConnectInfo,sql,args)
        #DB接続終了
        C020_DBUtil.closeDB(json_DBConnectInfo,errflg)
        #--------------------------------------------------------------------------------------------
        #メッセージがある場合はリストに追加
        #--------------------------------------------------
        #登録完了メッセージ
        msgID = "S0002"
        tuple_msgPalams = ("登録",)
        msgInfo_01 = C030_MessageUtil.getMessageInfo(msgID,tuple_msgPalams)
        list_msgInfo.append(msgInfo_01)
        #アクセスパス表示
        msgAccess = "アクセスパスを控えてください： "+ C010_Const.APP_NAME_DEFAULT+"/project/" + urlID + "/top/"
        msgID = "S0000"
        tuple_msgPalams = (msgAccess,)
        msgInfo_01 = C030_MessageUtil.getMessageInfo(msgID,tuple_msgPalams)
        list_msgInfo.append(msgInfo_01)
        #--------------------------------------------------
        #戻り値の共通項目を作成
        json_CommonInfo = {"errflg":errflg, "list_msgInfo" : list_msgInfo}
        #戻り値を作成
        json_service = {"json_CommonInfo":json_CommonInfo,"projectID":newID_S100}
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
