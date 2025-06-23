### My SQL PC setup
`sudo dnf install community-mysql-server -y`
`sudo systemctl start mysqld`
`sudo systemctl enable mysqld`
`systemctl status mysqld`
- check if it is active

`sudo mysql_secure_installation`
- `VALIDATE PASSWORD COMPONENT?` (Recommended to say `Y` for strong passwords, but you can say `N` if you want a simpler password without validation.)
- `Remove anonymous users?` (`Y`)
- `Disallow root login remotely?` (`Y`)
- `Remove test database and access to it?` (`Y`)
- `Reload privilege tables now?` (`Y`)


### Basic use SQL Commands

`mysql -u root -p`
`pip install mysqlclient`
#### Settings.py setup

DATABASES = {

'default' : {

'ENGINE' : 'django.db.backends.mysql',

'NAME' : 'restaurant',

'USER' : 'root',

'PASSWORD' : 'Abhi590sql@',

'HOST' : 'localhost',

'PORT' : '3306',

}

}


### SQL

`CREATE DATABASE restaurant;`
`SHOW DATABASES;SHOW DATABASES;`
`USE restaurant`


### Python SQL sync

`python manage.py makemigrations`
` python manage.py migrate`



