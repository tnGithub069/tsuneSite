"""
サービスクラス
S020_ShitsmnInfoTork

戻り値：{共通項目、任意項目1、任意項目2、...}
        └共通項目：{実行結果（エラーフラグ）、メッセージリスト}

"""

from . import C010_Const,C020_DBUtil,C030_MessageUtil
from . import S900_SelectHanyoMst

SERVICE_ID = "S150"

def main(userName,mailAddress,loginID,loginPass,hyoka,userComment,loginKbn):
    #--戻り値用の変数宣言------------------------------------------------------------------------------
    errflg = "0"
    list_msgInfo = []
    json_shitsmnInfo = {}
    #------------------------------------------------------------------------------------------------
    try:
        #--(1)採番処理呼び出し-----------------------------------------------------------------------------
        tableID_S010 = C010_Const.S010["tableID"]
        header_S010 = C010_Const.S010["header"]
        newID_S010 = S900_SelectHanyoMst.main(tableID_S010,header_S010)["newID"]
        #--採番処理呼び出し----------------------------------------------------------------------------
        #--DB連携基本コード----------------------------------------------------------------------------
        #DB接続開始、コネクションとカーソルを取得
        json_DBConnectInfo = C020_DBUtil.connectDB()
        #--(2.2.)クエリとパラメータを定義
        sql = "INSERT INTO M050_USER VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,current_timestamp(6),%s,%s,current_timestamp(6),%s);"
        args = (newID_S010,userName,mailAddress,loginID,loginPass,hyoka,userComment,loginKbn,SERVICE_ID,newID_S010,SERVICE_ID,newID_S010,"0",)
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
        json_service = {"json_CommonInfo":json_CommonInfo,"str_userID":newID_S010}
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
