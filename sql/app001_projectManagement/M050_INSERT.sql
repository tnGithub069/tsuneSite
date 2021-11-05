#DB選択
USE DB001_PMDB;

#T100
#INSERT INTO M050_USER VALUES (USERID,USERNAME,MAIL_ADDRESS,LOGINID,PASS,USERCOMMENT,LOGINKBN,'S000','SYSTEM',current_timestamp(6),'S000','SYSTEM',current_timestamp(6),'0');
INSERT INTO M050_USER VALUES ("U00000000000000001","福永祐一","fukunaga.y@jp.jra.com","2018derby","wagnerian","大胆戦法福永祐一","0",'S000','SYSTEM',current_timestamp(6),'S000','SYSTEM',current_timestamp(6),'0');

select * from M050_USER