"""
サービスクラス
S185_UserInfoShutk_SysLogin

戻り値：{共通項目、任意項目1、任意項目2、...}
        └共通項目：{実行結果（エラーフラグ）、メッセージリスト}

"""

from . import C020_DBUtil,C030_MessageUtil,C050_StringUtil

SERVICE_ID = "S910"

def main(tableName,tableItemName,itemValue,delflg):
    #--戻り値用の変数宣言------------------------------------------------------------------------------
    errflg = "0"
    list_msgInfo = []
    json_DBConnectInfo = {}
    try:
        #--DB連携基本コード----------------------------------------------------------------------------
        #DB接続開始、コネクションとカーソルを取得
        json_DBConnectInfo = C020_DBUtil.connectDB()
        #クエリを定義
        list_args = []
        sql = "select count(*) as COUNTER from " + tableName + " where " + tableItemName + " = %s "
        #項目名の値をパラメータリストに追加
        list_args.append(itemValue)
        #削除フラグの指定有無を判定
        if not C050_StringUtil.isNull(delflg):
            #指定ありの場合、クエリとパラメータに追加
            sql = sql + " and DELFLG = %s "
            list_args.append(delflg)
        sql = sql + ";"
        #パラメータを定義
        args = tuple(list_args)
        #クエリを実行し、結果を取得
        rows = C020_DBUtil.executeSQL(json_DBConnectInfo,sql,args)
        #DB接続終了
        C020_DBUtil.closeDB(json_DBConnectInfo,errflg)

        #共通処理------------------------------------------------------------------------------
        #戻り値の固有項目を作成
        counter = rows[0]["COUNTER"]
        #戻り値の共通項目を作成
        json_CommonInfo = {"errflg":errflg, "list_msgInfo" : list_msgInfo}
        #戻り値を作成
        json_service = {"json_CommonInfo":json_CommonInfo,"counter":counter}
        return json_service
        #共通処理------------------------------------------------------------------------------
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
