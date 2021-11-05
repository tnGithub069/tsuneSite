#DB選択
USE PMDB;

update M050_USER 
	set USERNAME = '' , 
		MAIL_ADDRESS = '' , 
        LOGINID = '' , 
        LOGINPASS = '' , 
        HYOKA = '' , 
        USERCOMMENT = '' , 
        LOGINKBN = '' , 
		UPDSRV = "S0001" ,
		UPDUSR = "SYSTEM000000000000" ,
		UPDDATE = current_timestamp(6) 
	where USERID = 'SYSTEM000000000000' ;

update M050_USER 
	set DELFLG = '' , 
		UPDSRV = "S0001" ,
		UPDUSR = "SYSTEM000000000000" ,
		UPDDATE = current_timestamp(6) 
	where USERID = 'SYSTEM000000000000' ;

