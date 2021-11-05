"""
サービスクラス
S080_SelectProject_List

戻り値：{共通項目、任意項目1、任意項目2、...}
        └共通項目：{実行結果（エラーフラグ）、メッセージリスト}

"""

from . import C020_DBUtil,C030_MessageUtil

SERVICE_ID = "S080"

def main(projectID):
    #--戻り値用の変数宣言------------------------------------------------------------------------------
    errflg = "0"
    list_msgInfo = []
    rows = ()
    #------------------------------------------------------------------------------------------------
    try:
        #--DB連携基本コード----------------------------------------------------------------------------
        #DB接続開始、コネクションとカーソルを取得
        json_DBConnectInfo = C020_DBUtil.connectDB()
        #クエリを定義
        #sql = "select PROJECTID,SEQ,TASKTITLE,TASKDETAIL,NAIYO,TANTSH,KIHYO_DATE,KIGN_DATE,TASKSTATUS from T110_TASK where PROJECTID = %s and DELFLG = %s order by SEQ ASC ;"
        sql = "select \
                    PROJECTID, \
                    SEQ, \
                    TASKTITLE, \
                    TASKDETAIL, \
                    NAIYO, \
                    TANTSH, \
                    KIHYO_DATE, \
                    KIGN_DATE, \
                    TASKSTATUS, \
                    M101.NAIYO01 AS TASKSTATUS_NAME \
                from T110_TASK T110 \
                LEFT OUTER JOIN M101_HANYOMST M101 \
                    ON T110.TASKSTATUS = M101.CD \
                    and M101.SECCD = 'SEC0001' \
                    and M101.DELFLG = '0' \
                where T110.PROJECTID = %s \
                    and T110.DELFLG = %s \
                order by T110.SEQ ASC "
        #パラメータを定義
        args = (projectID,"0",)
        #クエリを実行し、結果を取得
        rows = C020_DBUtil.executeSQL(json_DBConnectInfo,sql,args)
        #DB接続終了
        C020_DBUtil.closeDB(json_DBConnectInfo,errflg)
        #--------------------------------------------------------------------------------------------
        #メッセージがある場合はメッセージリストに追加

        #戻り値の共通項目を作成
        json_CommonInfo = {"errflg":errflg, "list_msgInfo" : list_msgInfo}
        #戻り値を作成
        json_service = {"json_CommonInfo":json_CommonInfo, "tuple_taskList" : rows}
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