#DB選択
USE PMDB;

UPDATE M100_HANYOHEADMST set SECNAME = "画面設定値", HEADER01 = "質問表示件数", HEADER02 = "サジェスト表示件数", HEADER03 = null, HEADER04 = null, HEADER05 = null, HEADER06 = null, HEADER07 = null, HEADER08 = null, HEADER09 = null, HEADER10 = null where seccd = "SEC0001";
UPDATE M101_HANYOMST set HYOJIJN = 1, NAIYO01 = "20", NAIYO02 = "5", NAIYO03 = null, NAIYO04 = null, NAIYO05 = null, NAIYO06 = null, NAIYO07 = null, NAIYO08 = null, NAIYO09 = null, NAIYO10 = null where seccd = "SEC0001" AND cd = "01";

