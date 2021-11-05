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
from . import (C010_Const, C030_MessageUtil,C050_StringUtil,
               S006_GetKeibaNews,
               S040_CreateProject,
               S910_TableItemCounter,
               )

def main(request):
    # --View共通----------------------------------------------
    # 戻り値用の変数宣言
    flg_return = ""
    template = ''
    context = {}
    path_name = ''
    # -------------------------------------------------------
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
            urlID = request.POST['urlID']
            projectName = request.POST['projectName']
            projectNaiyo = request.POST['projectNaiyo']
            projectComment = ""
            projectCrtUserID = "SYSTEM000000000000"
            userAuthFlg = "0"
            #サービスのパラメータをリクエストから取得する--------------------------------------

            #==チェック処理=============================================================================================
            #チェック処理
            #単項目チェック-------------------------------------------------------------------------------------------------
            itemName_urlID = "プロジェクトURL"
            itemName_projectName = "プロジェクト名"
            #urlID
            if C050_StringUtil.isAllSpace(urlID):
                errflg = "1"
                C030_MessageUtil.setMessage(request,"E0001",(itemName_urlID,))
            #projectName
            if C050_StringUtil.isAllSpace(projectName):
                errflg = "1"
                C030_MessageUtil.setMessage(request,"E0001",(itemName_projectName,))
            #単項目チェック-------------------------------------------------------------------------------------------------

            #DBに同じURLが登録されていないかのチェック--------------------------------------------------------------------
            json_S185 = S910_TableItemCounter.main("T100_PROJECT","URLID",urlID,"0")
            #errflg_S185 = json_S185["json_CommonInfo"]["errflg"]
            list_msgInfo_S185 = json_S185["json_CommonInfo"]["list_msgInfo"]
            #メッセージ格納
            #C030_MessageUtil.setMessageList(request,list_msgInfo_S185)
            counter_loginID =json_S185["counter"]
            if counter_loginID > 0 :
                errflg = "1"
                #「このURLは使えません」
                C030_MessageUtil.setMessage(request,"E0004",(itemName_urlID,))
            #DBに同じメールアドレスが登録されていないかのチェック--------------------------------------------------------------------

            #チェックNGの場合、処理を終了して再描画
            if errflg == "1":
                flg_return = "0"
                template = C010_Const.APP_NAME_DEFAULT + '/T040_ProjectCreate.html'
                context = {**context,**{
                                        "urlID":urlID,
                                        "projectName":projectName,
                                        "projectNaiyo":projectNaiyo,
                                        }
                        }
                #戻り値用のjsonを作成
                json_view = {'flg_return':flg_return, 'template':template, 'context':context, 'path_name':path_name}
                return json_view

            #==チェック処理=============================================================================================

            
            #--S040-------------------------------------------------------------------------
            json_S040 = S040_CreateProject.main(urlID,projectName,projectComment,projectNaiyo,projectCrtUserID,userAuthFlg)
            #個々の値を取得
            #flg_S150 = json_S150["json_CommonInfo"]["errflg"]
            list_msgInfo_S040 = json_S040["json_CommonInfo"]["list_msgInfo"]
            #str_userID_S150 = json_S150["str_userID"]
            #メッセージ格納
            C030_MessageUtil.setMessageList(request,list_msgInfo_S040)
            #-------------------------------------------------------------------------------
            flg_return = "1"
            path_name = C010_Const.PATH_NAME_SUCCESS
        else:
            # POST以外の場合
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
            # 戻り値にセット
            flg_return = "0"
            template = C010_Const.APP_NAME_DEFAULT + '/T040_ProjectCreate.html'
            json_keibaInfo = S006_GetKeibaNews.main(10)
            context = {**context, **{
                "json_keibaInfo": json_keibaInfo,
            }
            }

        # 戻り値用のjsonを作成
        json_view = {'flg_return': flg_return, 'template': template,
                     'context': context, 'path_name': path_name}
        return json_view
    # ==例外処理==========================================================================================
    except Exception as e:
        # システムエラー共通処理
        C030_MessageUtil.systemErrorCommonMethod()
        raise
    # ====================================================================================================
