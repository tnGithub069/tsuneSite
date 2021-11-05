#DB選択
USE DB001_PMDB;

select * from M020_MSGMST

#M020
#DEBUG用メッセージ-----------------------------------------------------------------------------------------------------
INSERT INTO M020_MSGMST VALUES ('D0000','D','@1','S000','SYSTEM000000000000',current_timestamp(6),'S000','SYSTEM000000000000',current_timestamp(6),'0');

#INFORM用メッセージ-----------------------------------------------------------------------------------------------------
INSERT INTO M020_MSGMST VALUES ('I0000','I','@1','S000','SYSTEM000000000000',current_timestamp(6),'S000','SYSTEM000000000000',current_timestamp(6),'0');
INSERT INTO M020_MSGMST VALUES ('I0001','I','@1と@2を差し置いてマカヒキが優勝したようです。。','S000','SYSTEM000000000000',current_timestamp(6),'S000','SYSTEM000000000000',current_timestamp(6),'0');

#SUCCESS用エラーメッセージ-----------------------------------------------------------------------------------------------------
INSERT INTO M020_MSGMST VALUES ('S0000','S','@1','S000','SYSTEM000000000000',current_timestamp(6),'S000','SYSTEM000000000000',current_timestamp(6),'0');
INSERT INTO M020_MSGMST VALUES ('S0001','S','@1が成功しました。@2をした後、@3をします。','S000','SYSTEM000000000000',current_timestamp(6),'S000','SYSTEM000000000000',current_timestamp(6),'0');
INSERT INTO M020_MSGMST VALUES ('S0002','S','@1が完了しました。','S000','SYSTEM000000000000',current_timestamp(6),'S000','SYSTEM000000000000',current_timestamp(6),'0');

#WARNNING用メッセージ-----------------------------------------------------------------------------------------------------
INSERT INTO M020_MSGMST VALUES ('W0000','W','@1','S000','SYSTEM000000000000',current_timestamp(6),'S000','SYSTEM000000000000',current_timestamp(6),'0');
INSERT INTO M020_MSGMST VALUES ('W0001','W','削除します。よろしいですか？','S000','SYSTEM000000000000',current_timestamp(6),'S000','SYSTEM000000000000',current_timestamp(6),'0');

#ERROR用メッセージ-----------------------------------------------------------------------------------------------------
INSERT INTO M020_MSGMST VALUES ('E0000','E','@1','S000','SYSTEM000000000000',current_timestamp(6),'S000','SYSTEM000000000000',current_timestamp(6),'0');
INSERT INTO M020_MSGMST VALUES ('E0001','E','@1を入力してください','S000','SYSTEM000000000000',current_timestamp(6),'S000','SYSTEM000000000000',current_timestamp(6),'0');
INSERT INTO M020_MSGMST VALUES ('E0002','E','@1が存在しません。','S000','SYSTEM000000000000',current_timestamp(6),'S000','SYSTEM000000000000',current_timestamp(6),'0');
INSERT INTO M020_MSGMST VALUES ('E0003','E','ログインIDまたはパスワードが間違っています。','S000','SYSTEM000000000000',current_timestamp(6),'S000','SYSTEM000000000000',current_timestamp(6),'0');
INSERT INTO M020_MSGMST VALUES ('E0004','E','この@1は使用できません。','S000','SYSTEM000000000000',current_timestamp(6),'S000','SYSTEM000000000000',current_timestamp(6),'0');
INSERT INTO M020_MSGMST VALUES ('E0005','E','@1と@2が一致しません。','S000','SYSTEM000000000000',current_timestamp(6),'S000','SYSTEM000000000000',current_timestamp(6),'0');


