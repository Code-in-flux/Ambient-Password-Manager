## What's here-
### Admin (directory)-
+ [failed_captcha.log]()-
 stores invalid captcha entries
+ [Incorrect_trials-{username}.log]()-
 stores Incorrect password enries of `{username}`. (Seperate file for each user)
 
### Password Database (directory)-
+ [{username}.psddb]()-
 stores the passwords of `{username}` in an encrypted format. Note that 'psddb' stands for 'PasSworD DataBase' (Seperate file for each user)
 
### Password_Manager.py (file)-
The main program which does all the work
