# -*- coding: utf-8 -*-

#■■■■■参考サイト■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■
#====Beautiflsoup関連===========================================================
#https://www.sejuku.net/blog/51241
#https://lets-hack.tech/programming/languages/python/beautifulsoup/
#http://pineplanter.moo.jp/non-it-salaryman/2018/01/03/python-scraping/
#==============================================================================
#■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■

import time
import requests
from bs4 import BeautifulSoup

#定数宣言======================================================================
fancID = 'FX-S-001'
sourceID = 'TEST'

#======================================================================


#【PRE】==============================================================================
#コネクションの取得
#conn = SC_DBAccess.connect()

#print()実行時の、numpy型のし有効数字を指定する
#np.set_printoptions(3)

#メモリ調査
#SC_Investigate.taracemalloc.taracemalloc_start()

#【FLW】==============================================================================

#====為替 ドル円 チャート（なぜか取得されない）=======================
"""
rq = requests.get("https://nikkei225jp.com/oil/")
soup = BeautifulSoup(rq.content, 'html.parser')
soup.find(class_='val2')
print(soup.find(id='V511'))
print(soup.find(id='V511').text)
vals = soup.select_one("#V511").findAll(text=True)
d1=''.join(vals)
print(d1)
"""
#=============================================================
def main(maxNo):
    list_news_Info = []
    return list_news_Info

def main_bk(maxNo):
    #====井上のサイト=============================================================
    #井上のサイトはなぜかリクエストが遅い
    """
    #処理開始時刻を取得
    tm_start = time.time()
    #サイトのURLを指定してリクエストを取得する
    rq = requests.get("https://inoshunnomad.com/")
    rq = requests.get("https://inoshunnomad.com/page/2")
    rq = requests.get("https://inoshunnomad.com/quit-thoughts")
    #処理終了時刻を取得
    tm_finish = time.time()
    print("井上のサイトのリクエスト処理にかかった時間 ：",round(tm_finish - tm_start,2),"秒")
    """
    #==============================================================================
    #====ネット競馬=============================================================
    #ネット競馬のニュースはwebスクしづらい
    """
    #サイトのURLを指定してリクエストを取得する
    rq = requests.get("https://news.netkeiba.com/?pid=news_backnumber&rank_type=2")
    #定型文、'html.parser'を使うよりも'lxml'を使う方が早いらしい
    soup_netkeiba = BeautifulSoup(rq.content, 'html.parser')
    #USDJPY_detail_ask要素の中に子要素largeがあるため、文字列として取得できない。下記記述で配列データが取得される。
    vals = soup_netkeiba.find_all(id="NewAccessRankList")
    #配列を結合することで文字列に変換する
    #d1=''.join(vals)
    """
    #==============================================================================

    #====極ウマくん=============================================================
    #処理開始時刻を取得 
    tm_start = time.time()
    #サイトのURLを指定してリクエストを取得する
    rq = requests.get("https://p.nikkansports.com/goku-uma/news/")
    #定型文、'html.parser'を使うよりも'lxml'を使う方が早いらしい
    soup = BeautifulSoup(rq.content, 'html.parser')
    #ニュースリンクのリストが表示されているエリア内の情報を全て取得
    #soup_backNumberArea = soup.find_all("",{"id":"backNumberArea"})
    soup_backNumberArea = soup.find_all(id="backNumberArea")
    #ニュースタイトルとurlのリストを作りたい
    list_news_Info_gokum = []
    for soup_backNumber in soup_backNumberArea:
        #ニュースリンクリストの情報からさらにaタグのみを取得する
        list_soup_news = soup_backNumber.find_all('a')
        i = 0
        for soup_news in list_soup_news:
            i +=1
            #aタグから、ニュースタイトル（aタグで囲まれた部分）とURLを取得する
            newsTitle = soup_news.string
            newsURL ="https://p.nikkansports.com/goku-uma/news/" + soup_news.get("href")
            json_newsInfo = {"newsTitle":newsTitle,"newsURL":newsURL}
            #リストに追加する
            list_news_Info_gokum.append(json_newsInfo)
            if not maxNo == 0 and i >= maxNo:
                break
    #処理終了時刻を取得
    tm_finish = time.time()
    print("極ウマくんのサイトのスクレイピング処理にかかった時間 ：",round(tm_finish - tm_start,2),"秒")
    #==============================================================================
    #====YouTube:競馬=============================================================
    #youtubeもダメ
    """
    #処理開始時刻を取得 
    tm_start = time.time()
    #サイトのURLを指定してリクエストを取得する
    rq = requests.get("https://www.youtube.com/channel/UCy-lzeGfBo0R6EjhK1AkcLg")
    #定型文、'html.parser'を使うよりも'lxml'を使う方が早いらしい
    soup = BeautifulSoup(rq.content, 'html.parser')
    #ニュースリンクのリストが表示されているエリア内の情報を全て取得
    soup_img = soup.find_all("iframe")
    print("soup_img:",soup_img)
    #処理終了時刻を取得
    tm_finish = time.time()
    print("YouTube:競馬のスクレイピング処理にかかった時間 ：",round(tm_finish - tm_start,2),"秒")
    """
    #==============================================================================
    #====亀谷重正公式サイト=============================================================
    #処理開始時刻を取得 
    tm_start = time.time()
    #サイトのURLを指定してリクエストを取得する
    rq = requests.get("https://k-beam.com/media")
    #定型文、'html.parser'を使うよりも'lxml'を使う方が早いらしい
    soup = BeautifulSoup(rq.content, 'html.parser')
    #「クラス：movie__flex__video」の中の「タグ：a」の「属性：href」を取得（最初の最初）
    newsVideo_kametani_url = soup.select(".movie__flex__video")[0].find_all("a")[0].get("href")
    newsVideo_kametani_imgSrc = soup.select(".movie__flex__video")[0].find_all("img")[0].get("src")
    json_newsVideoKametanInfo = {"newsVideo_kametani_url":newsVideo_kametani_url,
                                "newsVideo_kametani_imgSrc":newsVideo_kametani_imgSrc}
    #処理終了時刻を取得
    tm_finish = time.time()
    print("亀谷重正公式サイトのスクレイピング処理にかかった時間 ：",round(tm_finish - tm_start,2),"秒")
    #==============================================================================
    return_value = soup.findAll("a",text=True)
    json_keibaInfo = {
        "list_news_Info_gokum":list_news_Info_gokum,
        "json_newsVideoKametanInfo":json_newsVideoKametanInfo
        }
    return json_keibaInfo
