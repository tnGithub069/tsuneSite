from django.shortcuts import render,redirect

# Create your views here.

from .process import (
    V030_ProjectList,
    V040_ProjectCreate,
    V050_ProjectTop,
    V060_TaskTable,
    V070_TaskCreate,
    V080_TaskDetail,
    V090_TaskUpdate,
    V100_TaskDelete,
)
from .process import C010_Const,C030_MessageUtil
from .process import S006_GetKeibaNews

PATH_ERR = C010_Const.PATH_NAME_ERR

#プロジェクトリスト
def v030_ProjectList(request):
    try:
        #ビュープロセスクラスを呼び出し
        json_view = V030_ProjectList.main(request)
        #「render」か「redirect」かを判断
        flg_return = json_view["flg_return"]
        if flg_return == "0":
            #「render」の場合
            context = json_view["context"]
            template = json_view["template"]
            return render(request, template, context)
        elif flg_return == "1":
            #「redirect」の場合
            path_name = json_view["path_name"]
            return redirect(path_name)
    except Exception as e :
        #システムエラー共通処理
        C030_MessageUtil.systemErrorCommonMethod()
        #システムエラー画面に遷移
        return redirect(PATH_ERR)

#プロジェクトリスト
def v040_ProjectCreate(request):
    try:
        #ビュープロセスクラスを呼び出し
        json_view = V040_ProjectCreate.main(request)
        #「render」か「redirect」かを判断
        flg_return = json_view["flg_return"]
        if flg_return == "0":
            #「render」の場合
            context = json_view["context"]
            template = json_view["template"]
            return render(request, template, context)
        elif flg_return == "1":
            #「redirect」の場合
            path_name = json_view["path_name"]
            return redirect(path_name)
    except Exception as e :
        #システムエラー共通処理
        C030_MessageUtil.systemErrorCommonMethod()
        #システムエラー画面に遷移
        return redirect(PATH_ERR)

#プロジェクトトップ
def v050_ProjectTop(request,urlID):
    try:
        #ビュープロセスクラスを呼び出し
        json_view = V050_ProjectTop.main(request,urlID)
        #「render」か「redirect」かを判断
        flg_return = json_view["flg_return"]
        if flg_return == "0":
            #「render」の場合
            context = json_view["context"]
            template = json_view["template"]
            return render(request, template, context)
        elif flg_return == "1":
            #「redirect」の場合
            path_name = json_view["path_name"]
            return redirect(path_name)
    except Exception as e :
        #システムエラー共通処理
        C030_MessageUtil.systemErrorCommonMethod()
        #システムエラー画面に遷移
        return redirect(PATH_ERR)

#課題表
def v060_TaskTable(request,urlID):
    try:
        #ビュープロセスクラスを呼び出し
        json_view = V060_TaskTable.main(request,urlID)
        #「render」か「redirect」かを判断
        flg_return = json_view["flg_return"]
        if flg_return == "0":
            #「render」の場合
            context = json_view["context"]
            template = json_view["template"]
            return render(request, template, context)
        elif flg_return == "1":
            #「redirect」の場合
            path_name = json_view["path_name"]
            return redirect(path_name)
    except Exception as e :
        #システムエラー共通処理
        C030_MessageUtil.systemErrorCommonMethod()
        #システムエラー画面に遷移
        return redirect(PATH_ERR)

#課題追加
def v070_TaskCreate(request,urlID):
    try:
        #ビュープロセスクラスを呼び出し
        json_view = V070_TaskCreate.main(request,urlID)
        #「render」か「redirect」かを判断
        flg_return = json_view["flg_return"]
        if flg_return == "0":
            #「render」の場合
            context = json_view["context"]
            template = json_view["template"]
            return render(request, template, context)
        elif flg_return == "1":
            #「redirect」の場合
            path_name = json_view["path_name"]
            return redirect(path_name,urlID)
    except Exception as e :
        #システムエラー共通処理
        C030_MessageUtil.systemErrorCommonMethod()
        #システムエラー画面に遷移
        return redirect(PATH_ERR)

#課題詳細
def v080_TaskDetail(request,urlID,seq):
    try:
        #ビュープロセスクラスを呼び出し
        json_view = V080_TaskDetail.main(request,urlID,seq)
        #「render」か「redirect」かを判断
        flg_return = json_view["flg_return"]
        if flg_return == "0":
            #「render」の場合
            context = json_view["context"]
            template = json_view["template"]
            return render(request, template, context)
        elif flg_return == "1":
            #「redirect」の場合
            path_name = json_view["path_name"]
            return redirect(path_name)
    except Exception as e :
        #システムエラー共通処理
        C030_MessageUtil.systemErrorCommonMethod()
        #システムエラー画面に遷移
        return redirect(PATH_ERR)

#課題更新
def v090_TaskUpdate(request,urlID,seq):
    try:
        #ビュープロセスクラスを呼び出し
        json_view = V090_TaskUpdate.main(request,urlID,seq)
        #「render」か「redirect」かを判断
        flg_return = json_view["flg_return"]
        if flg_return == "0":
            #「render」の場合
            context = json_view["context"]
            template = json_view["template"]
            return render(request, template, context)
        elif flg_return == "1":
            #「redirect」の場合
            path_name = json_view["path_name"]
            return redirect(path_name,urlID,seq)
    except Exception as e :
        #システムエラー共通処理
        C030_MessageUtil.systemErrorCommonMethod()
        #システムエラー画面に遷移
        return redirect(PATH_ERR)

#課題削除
def v100_TaskDelete(request,urlID,seq):
    try:
        #ビュープロセスクラスを呼び出し
        json_view = V100_TaskDelete.main(request,urlID,seq)
        #「render」か「redirect」かを判断
        flg_return = json_view["flg_return"]
        if flg_return == "0":
            #「render」の場合
            context = json_view["context"]
            template = json_view["template"]
            return render(request, template, context)
        elif flg_return == "1":
            #「redirect」の場合
            path_name = json_view["path_name"]
            return redirect(path_name,urlID)
    except Exception as e :
        #システムエラー共通処理
        C030_MessageUtil.systemErrorCommonMethod()
        #システムエラー画面に遷移
        return redirect(PATH_ERR)

def v910_SuccessView(request):
    template = 'app001_projectManagement/T910_Success.html'
    context = {}
    try:
        return render(request, template, context)
    except Exception as e :
        #システムエラー共通処理
        C030_MessageUtil.systemErrorCommonMethod()
        #システムエラー画面に遷移
        return redirect(PATH_ERR)

def v990_SystemError(request):
    template = 'app001_projectManagement/T990_ERR500.html'
    context = {}
    try:
        return render(request, template, context)
    except Exception as e :
        #コンソールにエラーを出力
        C030_MessageUtil.systemErrorCommonMethod()
        return render(request, template, context)

#==================================================

    #テスト01
def test01(request):
    json_keibaInfo = S006_GetKeibaNews.main(0)
    #メッセージリストを宣言
    template = "app001_projectManagement/T999_test01.html"
    context = {"json_keibaInfo":json_keibaInfo}
    #返却
    return render(request, template, context) 
#==================================================