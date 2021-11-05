"""
サービスクラス
S905_SelectSaibnMst

戻り値：{共通項目、任意項目1、任意項目2、...}
        └共通項目：{実行結果（エラーフラグ）、メッセージリスト}

"""

import datetime
from . import C020_DBUtil,C030_MessageUtil,C050_StringUtil,C060_ListUtil

def main(tableID,header):
    #--戻り値用の変数宣言------------------------------------------------------------------------------
    errflg = "0"
    list_msgInfo = []
    rows = ()
    #------------------------------------------------------------------------------------------------
    try:
        #--DB連携基本コード----------------------------------------------------------------------------
        #DB接続開始、コネクションとカーソルを取得
        json_DBConnectInfo = C020_DBUtil.connectDB()

        #①システム日付をYYYYDDMMの文字列型で取得する
        sysDate = datetime.date.today().strftime("%Y%m%d")
        
        #②シーケンステーブルから「①」で取得した日付の通番の最大値+1を取得する
        sql_1 = "select IFNULL(MAX(SEQ),0) +1 AS NEWSEQ from " + tableID + " where SAIBNDATE = %s ;"
        args_1 = (sysDate,)
        int_newSeq = C020_DBUtil.executeSQL(json_DBConnectInfo,sql_1,args_1)[0]["NEWSEQ"]
        #　A. 取得行が0行の場合、「最大値+1=1」とする。 B.取得行が1行以上の場合、「最大値+1」を取得する。
        #int_newSeq = 1
        #if not C050_StringUtil.isEmpty(str_newSeq) :
        #    int_newSeq = int(str_newSeq)

        #③「①」の日付、「②」の最大値+1を、シーケンステーブルに登録する。
        sql_2 = "INSERT INTO " + tableID + " VALUES (%s,%s,current_timestamp(6));"
        args_2 = (sysDate,int_newSeq,)
        C020_DBUtil.executeSQL(json_DBConnectInfo,sql_2,args_2)
        #④「③」の結果によって処理を分岐する
        #A.正常終了した場合、コミットする。日付と通番を組み合わせた採番値を返す。
        #DB接続終了
        C020_DBUtil.closeDB(json_DBConnectInfo,errflg)
        #採番値の作成
        newID = header + sysDate + str(int_newSeq).zfill(9)
        #戻り値の共通項目を作成
        json_CommonInfo = {"errflg":errflg, "list_msgInfo" : list_msgInfo}
        #戻り値を作成
        json_service = {"json_CommonInfo":json_CommonInfo, "newID" : newID}

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
