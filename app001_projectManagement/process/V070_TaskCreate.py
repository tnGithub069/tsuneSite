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
               S070_SelectProject,
               S100_CreateTask,
               S900_SelectHanyoMst,
               )

def main(request,urlID):
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
            projectID = request.session['projectID']
            taskTitle = request.POST['taskTitle']
            taskTant = request.POST['taskTant']
            kignDate = request.POST['kignDate']
            kihyDate = datetime.datetime.now()
            taskStatus = request.POST['taskStatus']
            taskDetail = request.POST['taskDetail']
            taskNaiyo = request.POST['taskNaiyo']
            crtUserID = "SYSTEM000000000000"
            #サービスのパラメータをリクエストから取得する--------------------------------------

            #==チェック処理=============================================================================================
            #チェック処理
            #単項目チェック-------------------------------------------------------------------------------------------------
            itemName_taskName = "タスク名"
            itemName_kignDate = "期限日"
            #タスク名
            if C050_StringUtil.isAllSpace(taskTitle):
                errflg = "1"
                C030_MessageUtil.setMessage(request,"E0001",(itemName_taskName,))
            if C050_StringUtil.isAllSpace(kignDate):
                errflg = "1"
                C030_MessageUtil.setMessage(request,"E0001",(itemName_kignDate,))
            #単項目チェック-------------------------------------------------------------------------------------------------
            #チェックNGの場合、処理を終了して再描画
            if errflg == "1":
                flg_return = "0"
                template = C010_Const.APP_NAME_DEFAULT + '/T070_TaskCreate.html'
                context = {**context,**{
                                        "taskTitle":taskTitle,
                                        "taskTant":taskTant,
                                        "kignDate":kignDate,
                                        "taskStatus":taskStatus,
                                        "taskDetail":taskDetail,
                                        "taskNaiyo":taskNaiyo,
                                        }
                        }
                #戻り値用のjsonを作成
                json_view = {'flg_return':flg_return, 'template':template, 'context':context, 'path_name':path_name}
                return json_view

            #==チェック処理=============================================================================================

            #タスクを作成する
            #--S040-------------------------------------------------------------------------
            json_S100 = S100_CreateTask.main(projectID,taskTitle,taskDetail,taskNaiyo,taskTant,kihyDate,kignDate,taskStatus,crtUserID)
            #個々の値を取得
            #flg_S100 = json_S100["json_CommonInfo"]["errflg"]
            list_msgInfo_S100 = json_S100["json_CommonInfo"]["list_msgInfo"]
            #str_userID_S150 = json_S100["str_userID"]
            #メッセージ格納
            C030_MessageUtil.setMessageList(request,list_msgInfo_S100)
            #-------------------------------------------------------------------------------
            flg_return = "1"
            path_name = C010_Const.APP_NAME_DEFAULT + ':projectTop'
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
            template = C010_Const.APP_NAME_DEFAULT + '/T070_TaskCreate.html'
            # #ドロップダウンの値取得
            # tuple_status = S900_SelectHanyoMst.main("SEC0001",None)["tuple_M101_hanyoMst"]
            #競馬ニュース取得
            json_keibaInfo = S006_GetKeibaNews.main(10)
            todayDate = format(datetime.datetime.now(), '%Y-%m-%d')
            context = {**context, **{
                #"tuple_status":tuple_status,
                "json_keibaInfo": json_keibaInfo,
                "todayDate":todayDate
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
