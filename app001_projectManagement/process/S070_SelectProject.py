"""
サービスクラス
S070_SelectProject

戻り値：{共通項目、任意項目1、任意項目2、...}
        └共通項目：{実行結果（エラーフラグ）、メッセージリスト}

"""

from . import C020_DBUtil,C030_MessageUtil

SERVICE_ID = "S070"

def main(projctID):
    #--戻り値用の変数宣言------------------------------------------------------------------------------
    errflg = "0"
    list_msgInfo = []
    json_projectInfo = {}
    #------------------------------------------------------------------------------------------------
    try:
        #--DB連携基本コード----------------------------------------------------------------------------
        #DB接続開始、コネクションとカーソルを取得
        json_DBConnectInfo = C020_DBUtil.connectDB()
        #クエリを定義
        sql = "select PROJECTID,URLID,PROJECTNAME,PROJECT_COMMENT,PROJECT_NAIYO,PROJECT_CRTUSER,USERAUTHFLG,CRTDATE,UPDDATE from T100_PROJECT where PROJECTID = %s and DELFLG = %s ;"
        #パラメータを定義
        args = (projctID,"0",)
        #クエリを実行し、結果を取得
        rows = C020_DBUtil.executeSQL(json_DBConnectInfo,sql,args)
        #DB接続終了
        C020_DBUtil.closeDB(json_DBConnectInfo,errflg)
        #--------------------------------------------------------------------------------------------
        #0取得件数が0件の場合はエラー
        
        if len(rows) == 0 :
            errflg = "1"
            msgID = "E0002"
            tuple_msgPalams = ("このプロジェクト",)
            json_msgInfo = C030_MessageUtil.getMessageInfo(msgID,tuple_msgPalams)
            list_msgInfo.append(json_msgInfo) 
        else:
            json_projectInfo = rows[0]

        #戻り値の共通項目を作成
        json_CommonInfo = {"errflg":errflg, "list_msgInfo" : list_msgInfo}
        #戻り値を作成
        json_service = {"json_CommonInfo":json_CommonInfo, "json_projectInfo" : json_projectInfo}
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


def selectT100_ByUrlID(urlID):
    #--戻り値用の変数宣言------------------------------------------------------------------------------
    errflg = "0"
    list_msgInfo = []
    json_projectInfo = {}
    #------------------------------------------------------------------------------------------------
    try:
        #--DB連携基本コード----------------------------------------------------------------------------
        #DB接続開始、コネクションとカーソルを取得
        json_DBConnectInfo = C020_DBUtil.connectDB()
        #クエリを定義
        sql = "select PROJECTID,URLID,PROJECTNAME,PROJECT_NAIYO,PROJECT_CRTUSER,CRTDATE,UPDDATE from T100_PROJECT where URLID = %s and DELFLG = %s ;"
        #パラメータを定義
        args = (urlID,"0",)
        #クエリを実行し、結果を取得
        rows = C020_DBUtil.executeSQL(json_DBConnectInfo,sql,args)
        #DB接続終了
        C020_DBUtil.closeDB(json_DBConnectInfo,errflg)
        #--------------------------------------------------------------------------------------------
        #0取得件数が0件の場合はエラー
        
        if len(rows) == 0 :
            errflg = "1"
            msgID = "E0002"
            tuple_msgPalams = ("このプロジェクト",)
            json_msgInfo = C030_MessageUtil.getMessageInfo(msgID,tuple_msgPalams)
            list_msgInfo.append(json_msgInfo) 
        else:
            json_projectInfo = rows[0]

        #戻り値の共通項目を作成
        json_CommonInfo = {"errflg":errflg, "list_msgInfo" : list_msgInfo}
        #戻り値を作成
        json_service = {"json_CommonInfo":json_CommonInfo, "json_projectInfo" : json_projectInfo}
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