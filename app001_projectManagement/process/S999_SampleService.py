"""
サービスクラス
S999_SampleService

戻り値：{共通項目、任意項目1、任意項目2、...}
        └共通項目：{実行結果（エラーフラグ）、メッセージリスト}

"""

from . import C020_DBUtil,C030_MessageUtil

def main():
    #--戻り値用の変数宣言------------------------------------------------------------------------------
    errflg = "0"
    list_msgInfo = []
    json_shitsmnIchirn = {}
    #------------------------------------------------------------------------------------------------
    try:
        #--DB連携基本コード----------------------------------------------------------------------------
        #DB接続開始、コネクションとカーソルを取得
        json_DBConnectInfo = C020_DBUtil.connectDB()
        #クエリを定義
        sql = "SELECT SHITSMN_ID,SHITSMN_TITLE,SHITSMN_NAIYO,SHITSMN_USERID,KAIGIID FROM T100_SHITSMN"
        #パラメータを定義
        args = ()
        #クエリを実行し、結果を取得
        rows = C020_DBUtil.executeSQL(json_DBConnectInfo,sql,args)
        #DB接続終了
        C020_DBUtil.closeDB(json_DBConnectInfo,errflg)
        #--------------------------------------------------------------------------------------------
        #メッセージがある場合はメッセージリストに追加
        #--------------------------------------------------
        msgID1 = "W0001"
        tuple_msgPalams1 = ()
        msgInfo1 = C030_MessageUtil.getMessageInfo(msgID1,tuple_msgPalams1)
        list_msgInfo.append(msgInfo1)
        #--------------------------------------------------
        msgID2 = "S0001"
        tuple_msgPalams2 = ("本能寺の変","信長を暗殺","下剋上")
        msgInfo2 = C030_MessageUtil.getMessageInfo(msgID2,tuple_msgPalams2)
        list_msgInfo.append(msgInfo2)
        #--------------------------------------------------
        #戻り値の共通項目を作成
        json_CommonInfo = {"errflg":errflg, "list_msgInfo" : list_msgInfo}
        #戻り値を作成
        rows = [] #大量に出てくるため初期化
        json_service = {"json_CommonInfo":json_CommonInfo, "tuple_shitsmnIchirn" : rows}
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