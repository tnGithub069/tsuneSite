"""
ビュークラス
V120_userKoshn
質問作成ページ用View
エラーフラグ：0(正常終了),1(業務エラー),2(システムエラー)
flg_return：0(render),1(redirect)

flg_return==0の時、「template」「context」必須
flg_return==1の時、「path_name」必須

"""

import datetime
from django.urls import reverse
from . import (C010_Const,C030_MessageUtil,
                ZS160_UserInfoKoshn,
)

def main(request):
    #--View共通----------------------------------------------
    #戻り値用の変数宣言
    flg_return = ""
    template = ''
    context = {}
    path_name = ''
    #-------------------------------------------------------
    try:
        if request.method == 'POST':
            #POSTの場合
            """
            POST時の処理を書く。
            パターンに応じてflg_returnの値を設定する。
            bottunパターンによって処理を分けたりもするかも。
            例は、redirect
            """
            errflg = "0"
            #更新ボタンの場合
            #サービスのパラメータをリクエストから取得する--------------------------------------
            userID = request.session['userID']
            userName = request.POST['userName']
            mailAddress = request.POST['mailAddress']
            loginID = request.POST['loginID']
            loginPass = request.POST['loginPass']
            loginPass_conf = request.POST['loginPass_conf']
            hyoka = 0
            userComment = request.POST['userComment']
            #loginKbn =  "0"
            #サービスのパラメータをリクエストから取得する--------------------------------------
            #--S150-------------------------------------------------------------------------
            json_S160 = ZS160_UserInfoKoshn.main(userID,userName,mailAddress,loginID,loginPass,hyoka,userComment)
            #個々の値を取得
            flg_S160 = json_S160["json_CommonInfo"]["errflg"]
            list_msgInfo_S160 = json_S160["json_CommonInfo"]["list_msgInfo"]
            str_userID_S160 = json_S160["str_userID"]
            #メッセージ格納
            C030_MessageUtil.setMessageList(request,list_msgInfo_S160)
            #-------------------------------------------------------------------------------
            flg_return = "1"
            path_name = 'teachersapp:myPage'
        else:
            #POST以外の場合
            """
            POST以外時の処理を書く。
            パターンに応じてflg_returnの値を設定する。
            bottunパターンによって処理を分けたりもするかも。
            例は、render
            """
        
        #戻り値用のjsonを作成
        json_view = {'flg_return':flg_return, 'template':template, 'context':context, 'path_name':path_name}
        return json_view
    #==例外処理==========================================================================================
    except Exception as e :
        #システムエラー共通処理
        C030_MessageUtil.systemErrorCommonMethod()
        raise
    #====================================================================================================

