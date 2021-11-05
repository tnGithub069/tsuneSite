"""
ビュークラス
V030_ShitsmnSaksiProcess
質問作成ページ用View
エラーフラグ：0(正常終了),1(業務エラー),2(システムエラー)
flg_return：0(render),1(redirect)

flg_return==0の時、「template」「context」必須
flg_return==1の時、「path_name」必須

"""

import datetime
from django.urls import reverse
from . import (C010_Const,C030_MessageUtil,C050_StringUtil,
                ZS150_UserInfoTork,
                ZS185_UserInfoShutk_SysLogin,
                S910_TableItemCounter,
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
            #サービスのパラメータをリクエストから取得する--------------------------------------
            userName = request.POST['userName']
            mailAddress = request.POST['mailAddress']
            loginID = request.POST['loginID']
            loginPass = request.POST['loginPass']
            loginPass_conf = request.POST['loginPass_conf']
            hyoka = 0
            userComment = "よろしくお願いします。"
            loginKbn =  "0"
            #サービスのパラメータをリクエストから取得する--------------------------------------

            #==チェック処理=============================================================================================
            #チェック処理
            #単項目チェック-------------------------------------------------------------------------------------------------
            itemName_userName = "ユーザ名"
            itemName_mailAddress = "メールアドレス"
            itemName_loginID = "ログインID"
            itemName_loginPass = "ログインパスワード"
            itemName_loginPass_conf = "ログインパスワード（確認用）"
            #ユーザ名
            if C050_StringUtil.isAllSpace(userName):
                errflg = "1"
                C030_MessageUtil.setMessage(request,"E0001",(itemName_userName,))
            #メールアドレス
            if C050_StringUtil.isAllSpace(mailAddress):
                errflg = "1"
                C030_MessageUtil.setMessage(request,"E0001",(itemName_mailAddress,))
            #ログインID
            if C050_StringUtil.isAllSpace(loginID):
                errflg = "1"
                C030_MessageUtil.setMessage(request,"E0001",(itemName_loginID,))
            #ログインパスワード
            if C050_StringUtil.isAllSpace(loginPass):
                errflg = "1"
                C030_MessageUtil.setMessage(request,"E0001",(itemName_loginPass,))
            #ログインパスワード（確認用）
            if C050_StringUtil.isAllSpace(loginPass_conf):
                errflg = "1"
                C030_MessageUtil.setMessage(request,"E0001",(itemName_loginPass_conf,))
            #単項目チェック-------------------------------------------------------------------------------------------------

            #パスワードとパスワード（確認用）の一致チェック-----------------------------------------------------------------------
            if not C050_StringUtil.isSameCharacter(loginPass,loginPass_conf):
                errflg = "1"
                C030_MessageUtil.setMessage(request,"E0005",(itemName_loginPass,itemName_loginPass_conf,))
            #パスワードとパスワード（確認用）の一致チェック-----------------------------------------------------------------------

            #DBに同じメールアドレスが登録されていないかのチェック--------------------------------------------------------------------
            json_S185 = S910_TableItemCounter.main("M050_USER","LOGINID",mailAddress,"0")
            #errflg_S185 = json_S185["json_CommonInfo"]["errflg"]
            list_msgInfo_S185 = json_S185["json_CommonInfo"]["list_msgInfo"]
            #メッセージ格納
            #C030_MessageUtil.setMessageList(request,list_msgInfo_S185)
            counter_loginID =json_S185["counter"]
            if counter_loginID > 0 :
                errflg = "1"
                #「このメールアドレスは使えません」
                C030_MessageUtil.setMessage(request,"E0004",(itemName_mailAddress,))
            #DBに同じメールアドレスが登録されていないかのチェック--------------------------------------------------------------------

            #DBに同じログインIDが登録されていないかのチェック--------------------------------------------------------------------
            json_S185 = S910_TableItemCounter.main("M050_USER","MAIL_ADDRESS",loginID,"0")
            #errflg_S185 = json_S185["json_CommonInfo"]["errflg"]
            list_msgInfo_S185 = json_S185["json_CommonInfo"]["list_msgInfo"]
            #メッセージ格納
            #C030_MessageUtil.setMessageList(request,list_msgInfo_S185)
            counter_loginID =json_S185["counter"]
            if counter_loginID > 0 :
                errflg = "1"
                #「このユーザIDは使えません」
                C030_MessageUtil.setMessage(request,"E0004",(itemName_loginID,))
            #DBに同じログインIDが登録されていないかのチェック--------------------------------------------------------------------

            #チェックNGの場合、処理を終了して再描画
            if errflg == "1":
                flg_return = "0"
                template = 'teachersapp/T100_SignUp.html'
                context = {**context,**{
                                        "userName":userName,
                                        "mailAddress":mailAddress,
                                        "loginID":loginID,
                                        }
                        }
                #戻り値用のjsonを作成
                json_view = {'flg_return':flg_return, 'template':template, 'context':context, 'path_name':path_name}
                return json_view

            #==チェック処理=============================================================================================

            
            #--S150-------------------------------------------------------------------------
            json_S150 = ZS150_UserInfoTork.main(userName,mailAddress,loginID,loginPass,hyoka,userComment,loginKbn)
            #個々の値を取得
            #flg_S150 = json_S150["json_CommonInfo"]["errflg"]
            list_msgInfo_S150 = json_S150["json_CommonInfo"]["list_msgInfo"]
            #str_userID_S150 = json_S150["str_userID"]
            #メッセージ格納
            C030_MessageUtil.setMessageList(request,list_msgInfo_S150)
            #-------------------------------------------------------------------------------
            #--S185-------------------------------------------------------------------------
            #サービス呼び出し
            json_S185 = ZS185_UserInfoShutk_SysLogin.main(loginID,loginPass)
            #個々の値を取得
            #flg_S185 = json_S185["json_CommonInfo"]["errflg"]
            list_msgInfo_S185 = json_S185["json_CommonInfo"]["list_msgInfo"]
            str_userID_S185 = json_S185["str_userID"]
            str_userName_S185 = json_S185["str_userName"]
            #メッセージ格納
            C030_MessageUtil.setMessageList(request,list_msgInfo_S185)
            #-------------------------------------------------------------------------------
            #セッション処理----------------------------------------------------
            #セッションにuserIDを追加
            request.session['userID'] = str_userID_S185
            request.session['userName'] = str_userName_S185
            #----------------------------------------------------------------
            flg_return = "1"
            path_name = C010_Const.PATH_NAME_SUCCESS
        else:
            #POST以外の場合
            """
            POST以外時の処理を書く。
            パターンに応じてflg_returnの値を設定する。
            bottunパターンによって処理を分けたりもするかも。
            例は、render
            """
            """
            #サービスを利用する場合は呼び出す
            #--S060-------------------------------------------------------------------------
            #サービス呼び出し
            json_S060 = S060_ShitsmnListShutk_Shinchk.main()
            #個々の値を取得
            flg_S060 = json_S060["json_CommonInfo"]["errflg"]
            list_msgInfo_S060 = json_S060["json_CommonInfo"]["list_msgInfo"]
            list_T100_shitsmnList_shinchk_S060 = json_S060["list_T100_shitsmnList_shinchk"]
            #メッセージ格納
            C030_MessageUtil.setMessageList(request,list_msgInfo_S060)
            #-------------------------------------------------------------------------------
            """
            #戻り値にセット
            flg_return = "0"
            template = 'teachersapp/T100_SignUp.html'
            #list_newsInfo = S006_GetKeibaNews.main(10)
            context = {**context,**{
                                    #"list_newsInfo":list_newsInfo,
                                    }
                    }
        
        #戻り値用のjsonを作成
        json_view = {'flg_return':flg_return, 'template':template, 'context':context, 'path_name':path_name}
        return json_view
    #==例外処理==========================================================================================
    except Exception as e :
        #システムエラー共通処理
        C030_MessageUtil.systemErrorCommonMethod()
        raise
    #====================================================================================================
