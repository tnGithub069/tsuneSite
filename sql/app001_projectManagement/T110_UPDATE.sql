USE PMDB;

select * from T110_TASK where PROJECTID = "P20211017000000036" ;
update T110_TASK 
	set TASKTITLE = 'tsunesanbk',
		TASKDETAIL = 'グランアレグリア一択ですか？',
        NAIYO = 'あああああ',
        TANTSH = '福永',
        KIHYO_DATE = current_timestamp(6),
        KIGN_DATE = current_timestamp(6),
        TASKSTATUS = '0',
        DELFLG = '0',
        UPDSRV = 'S000',
        UPDUSR = 'SYSTEM000000000000',
        UPDDATE = current_timestamp(6)
	where PROJECTID = "P20211017000000036"  and SEQ = 1
;