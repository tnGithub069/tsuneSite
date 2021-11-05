#DB選択
USE DB001_PMDB;

select * from M100_HANYOHEADMST;
select * from M101_HANYOMST;

#SEC0001
INSERT INTO M100_HANYOHEADMST VALUES ('SEC0001','課題ステータス','課題ステータス名',null,null,null,null,null,null,null,null,null,'S000','SYSTEM',current_timestamp(6),'S000','SYSTEM',current_timestamp(6),'0');
INSERT INTO M101_HANYOMST VALUES ('SEC0001','0',10,'起票',null,null,null,null,null,null,null,null,null,'S000','SYSTEM',current_timestamp(6),'S000','SYSTEM',current_timestamp(6),'0');
INSERT INTO M101_HANYOMST VALUES ('SEC0001','1',20,'着手',null,null,null,null,null,null,null,null,null,'S000','SYSTEM',current_timestamp(6),'S000','SYSTEM',current_timestamp(6),'0');
INSERT INTO M101_HANYOMST VALUES ('SEC0001','2',30,'検討中',null,null,null,null,null,null,null,null,null,'S000','SYSTEM',current_timestamp(6),'S000','SYSTEM',current_timestamp(6),'0');
INSERT INTO M101_HANYOMST VALUES ('SEC0001','3',40,'対応中',null,null,null,null,null,null,null,null,null,'S000','SYSTEM',current_timestamp(6),'S000','SYSTEM',current_timestamp(6),'0');
INSERT INTO M101_HANYOMST VALUES ('SEC0001','4',50,'確認待ち',null,null,null,null,null,null,null,null,null,'S000','SYSTEM',current_timestamp(6),'S000','SYSTEM',current_timestamp(6),'0');
INSERT INTO M101_HANYOMST VALUES ('SEC0001','5',60,'確認中',null,null,null,null,null,null,null,null,null,'S000','SYSTEM',current_timestamp(6),'S000','SYSTEM',current_timestamp(6),'0');
INSERT INTO M101_HANYOMST VALUES ('SEC0001','6',70,'完了',null,null,null,null,null,null,null,null,null,'S000','SYSTEM',current_timestamp(6),'S000','SYSTEM',current_timestamp(6),'0');
INSERT INTO M101_HANYOMST VALUES ('SEC0001','7',80,'削除',null,null,null,null,null,null,null,null,null,'S000','SYSTEM',current_timestamp(6),'S000','SYSTEM',current_timestamp(6),'0');
