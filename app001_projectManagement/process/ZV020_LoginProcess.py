"""
ビュークラス
V020_LoginProcess
ログインページ用View
エラーフラグ：0(正常終了),1(業務エラー),2(システムエラー)
flg_return：0(render),1(redirect)

flg_return==0の時、「template」「context」必須
flg_return==1の時、「path_name」必須

"""

from django.urls import reverse
from . import (C010_Const,C030_MessageUtil,
                ZS185_UserInfoShutk_SysLogin
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
            #--S185-------------------------------------------------------------------------
            #サービス呼び出し
            loginID = request.POST['loginID']
            loginPass = request.POST['loginPass']
            json_S185 = ZS185_UserInfoShutk_SysLogin.main(loginID,loginPass)
            #個々の値を取得
            flg_S185 = json_S185["json_CommonInfo"]["errflg"]
            list_msgInfo_S185 = json_S185["json_CommonInfo"]["list_msgInfo"]
            str_userID_S185 = json_S185["str_userID"]
            str_userName_S185 = json_S185["str_userName"]
            #メッセージ格納
            C030_MessageUtil.setMessageList(request,list_msgInfo_S185)
            #-------------------------------------------------------------------------------
            #認証OKの場合、セッションにユーザIDを格納してからTopページにリダイレクト
            if flg_S185 == "0" :
                #セッション処理----------------------------------------------------
                #セッションにuserIDを追加
                request.session['userID'] = str_userID_S185
                request.session['userName'] = str_userName_S185
                #----------------------------------------------------------------
                #1：リダイレクトを指定する
                flg_return = "1"
                #テンプレートを指定する
                path_name = 'teachersapp:topPage'
            #認証NGの場合、ログインページをレンダー
            elif flg_S185 == "1" :
                flg_return = "0"
                template = 'teachersapp/T020_Login.html'
                context = {**context,**{
                                        "loginID":loginID,
                                        #"loginPass":loginPass,
                                        }
                        }
        else:
            #POST以外の場合
            """
            POST以外時の処理を書く。
            パターンに応じてflg_returnの値を設定する。
            bottunパターンによって処理を分けたりもするかも。
            例は、render
            """
            #サービスを利用する場合は呼び出す
            """
            #--S185-------------------------------------------------------------------------
            #サービス呼び出し
            loginID = request.POST['loginID']
            loginPass = request.POST['loginPass']
            json_S185 = S185_UserInfoShutk_SysLogin.main(loginID,loginPass)
            #個々の値を取得
            flg_S185 = json_S185["json_CommonInfo"]["errflg"]
            list_msgInfo_S185 = json_S185["json_CommonInfo"]["list_msgInfo"]
            str_userID_S185 = json_S185["str_userID"]
            #メッセージ格納
            C030_MessageUtil.setMessageList(request,list_msgInfo_S185)
            #-------------------------------------------------------------------------------
            """
            #戻り値にセット
            flg_return = "0"
            template = 'teachersapp/T020_Login.html'
            context = {**context,**{
                                    #"list_shitsmnList_shinchk":list_T100_shitsmnList_shinchk_S060,
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

