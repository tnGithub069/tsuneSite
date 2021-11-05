USE PMDB;

select * from T100_PROJECT where PROJECTID = "P20211017000000036" ;
update T100_PROJECT 
	set URLID = 'tsunesanbk',
		PROJECTNAME = 'グランアレグリア一択ですか？',
        PROJECT_CRTUSER = 'SYSTEM000000000000',
        DELFLG = '0',
        UPDSRV = 'S000',
        UPDUSR = 'SYSTEM000000000000',
        UPDDATE = current_timestamp(6)
	where where PROJECTID = "P20211017000000036" 
;