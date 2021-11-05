"""
ビュークラス
V050_ProjectTop
トップページ用View
エラーフラグ：0(正常終了),1(業務エラー),2(システムエラー)
flg_return：0(render),1(redirect)

flg_return==0の時、「template」「context」必須
flg_return==1の時、「path_name」必須

"""

from django.urls import reverse
from . import (C010_Const,C030_MessageUtil,
                S006_GetKeibaNews,
                S070_SelectProject,
                S140_SelectTask_List,
                S900_SelectHanyoMst
)

def main(request,urlID):
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
            flg_return = "1"
            path_name = C010_Const.APP_NAME_DEFAULT + ':topPage'
        else:
            #POST以外の場合
            """
            POST以外時の処理を書く。
            パターンに応じてflg_returnの値を設定する。
            bottunパターンによって処理を分けたりもするかも。
            例は、render
            """
            #サービスを利用する場合は呼び出す
            #プロジェクト情報を取得する
            #--S080-------------------------------------------------------------------------
            #サービス呼び出し
            json_S070 = S070_SelectProject.selectT100_ByUrlID(urlID)
            #個々の値を取得
            flg_S070 = json_S070["json_CommonInfo"]["errflg"]
            list_msgInfo_S070 = json_S070["json_CommonInfo"]["list_msgInfo"]
            json_projectInfo = json_S070["json_projectInfo"]
            #メッセージ格納
            C030_MessageUtil.setMessageList(request,list_msgInfo_S070)
            #-------------------------------------------------------------------------------
            projectID = json_projectInfo["PROJECTID"]
            urlID = json_projectInfo["URLID"]
            projectName = json_projectInfo["PROJECTNAME"]

            #プロジェクトに紐づくタスクの一覧を取得する
            #--S140-------------------------------------------------------------------------
            #サービス呼び出し
            json_S140 = S140_SelectTask_List.main(projectID)
            #個々の値を取得
            flg_S070 = json_S140["json_CommonInfo"]["errflg"]
            list_msgInfo_S070 = json_S140["json_CommonInfo"]["list_msgInfo"]
            tuple_taskList = json_S140["tuple_taskList"]
            #メッセージ格納
            C030_MessageUtil.setMessageList(request,list_msgInfo_S070)
            #-------------------------------------------------------------------------------
            #--S900-------------------------------------------------------------------------
            #ドロップダウンの値取得
            tuple_status = S900_SelectHanyoMst.main("SEC0001",None)["tuple_M101_hanyoMst"]
            #-------------------------------------------------------------------------------
            #--S006-------------------------------------------------------------------------
            #サービス呼び出し
            #最新ニュース取得
            json_keibaInfo = S006_GetKeibaNews.main(0)
            #-------------------------------------------------------------------------------

            #セッション処理----------------------------------------------------
            #セッションにuserIDを追加
            request.session['projectID'] = projectID
            request.session['urlID'] = urlID
            request.session['projectName'] = projectName
            #セッションにマスタ値を追加
            request.session["tuple_status"] = tuple_status
            #----------------------------------------------------------------

            #戻り値にセット
            flg_return = "0"
            template = C010_Const.APP_NAME_DEFAULT + '/T050_ProjectTop.html'
            context = {**context,**{
                                    "projectInfo":json_projectInfo,
                                    "tuple_taskList":tuple_taskList,
                                    "json_keibaInfo":json_keibaInfo,
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

