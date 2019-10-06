Features

1>Django 2.0+
2>Python3.5
3>mysql database support .
4>Other things I'm forgetting now.

.....................................................

step1-sudo apt-get install sendmail

step2-create app and installed app in settigs.py ....>INSTALLED_APPS = (
  ...
  'mailings'
)
step3-Create database connection with mysql
step4- writ Email Host user and password
step5- Create send mails function in django views 
step6-also create a simple UI form which contains all required data

......................................................
steps to run project
--->create mysql database
--->write the mysql database name,username and password in settings.py
--->go to present directory of project
--->cd mailfire-master
--->python manage.py makemigrations
--->python manage.py migrate
--->python manage.py runserver

@send mails and store data into data base 
In your browser, go to http://localhost:8000/send_mails/
....>after feeling all the required data click on send button
....>check email and and also database 

@send mails to admin 
In your browser, go to http://localhost:8000/mailings/sendAdminMail/
....>send all today email send data to admin