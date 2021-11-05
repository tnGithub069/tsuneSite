from django.db import models

# Create your models here.
"""
参考サイト
【Django】model の主キーにAutoFieldを設定しても自動採番してくれない
https://teratail.com/questions/221566
Django モデルフィールド：データベースフィールド 型対応表
https://qiita.com/okoppe8/items/13ad7b7d52fd6a3fd3fc
Django 3.0 のモデルフィールドリファレンス一覧まとめ
https://qiita.com/KeAt/items/55fdedc8cac7c6852043
Djangoのモデルの各フィールドの使い方まとめ「その１」
https://www.nblog09.com/w/2019/05/14/django-field/

"""
"""
#T100_質問テーブル
class T100_SHITSMN(models.Model):
    #テーブル固有項目
    SHITSMN_ID = models.BigAutoField(primary_key=True,max_length=18)
    SHITSMN_TITLE = models.CharField(max_length=256)
    SHITSMN_NAIYO = models.TextField(max_length=2048)
    SHITSMN_USERID = models.CharField(max_length=30)
    KAIGIID = models.AutoField(max_length=18,null=True)
    #共通項目
    CRTACTID = models.CharField(max_length=5)
    CRTUSERID = models.CharField(max_length=30)
    CRTDATE =  models.DateTimeField('date published')
    UPDACTID = models.CharField(max_length=5)
    UPDUSERID = models.CharField(max_length=30)
    UPDDATE =  models.DateTimeField('date published')
    DELFLG = models.CharField(max_length=1)
    def __str__(self):
        return self.SHITSMN_TITLE

#T101_質問ハッシュタグ
class T101_SHITSMNHASHTAG(models.Model):
    #テーブル固有項目
    SHITSMN_ID = models.BigIntegerField(primary_key=True)
    HASHTAG_ID = models.BigIntegerField(primary_key=True)
    #共通項目
    CRTACTID = models.CharField(max_length=5)
    CRTUSERID = models.CharField(max_length=30)
    CRTDATE =  models.DateTimeField('date published')
    UPDACTID = models.CharField(max_length=5)
    UPDUSERID = models.CharField(max_length=30)
    UPDDATE =  models.DateTimeField('date published')
    DELFLG = models.CharField(max_length=1)
    def __str__(self):
        return self.SHITSMN_TITLE

"""