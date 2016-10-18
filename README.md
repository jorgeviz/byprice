# Drugs Request Pact

The drugs request microservice provides a full dataset from a retailer thatreturns all items from the drugs department with its correspondant parameters. Data is taken with a web crawler made using scrapy. Both services run in 2 different Azure Ubuntu Server 14.01 LTS VMs.

# Features

## On the MySQL Server

+ Web crawling through the drugs department to retrieve data.
+ Stores scraped data into a MySQL database.
+ Database is updated hourly using a crontab command.

## On the Flask microservice request app

+ Access to the complete database of drugs from defined retailer.
+ Quick search into the server from a request of a determined value.
+ Usage of NginX with Gunicorn as the web server.

# How would I use the Request microservice?

## Configuring Flask request application

1. SSH into the virtual machine.
2. Install all packages needed:
```bash
$ sudo apt-get install python3-pip
$ sudo easy_install3 pip
$ sudo apt-get install python-dev python-pip libxml2-dev libxslt1-dev zlib1g-dev libffi-dev libssl-dev
$ sudo apt-get install git
$ sudo apt-get update
$ sudo apt-get install mysql-server
$ sudo pip install virtualenv
```
3. Clone repository.
4. Create virtual environment __virtualenv venv__  and source it __source ./venv/bin/activate__
5. Install all dependencies with __pip install -r requirements.txt__
6. Execute the following lines to configure NginX with Guicorn:
```bash
$ sudo apt-get install -y nginx gunicorn
$ /etc/init.d/nginx start
$ sudo rm /etc/nginx/sites-enabled/default
$ sudo touch /etc/nginx/sites-available/Byprice
$ sudo ln -s /etc/nginx/sites-available/Byprice /etc/nginx/sites-enabled/Byprice
```
7. Edit NginX server file entering __sudo nano /etc/nginx/sites-enabled/Byprice__
```
	server {
		location / {
		proxy_pass http://localhost:8000;
		proxy_set_header Host $host;
		proxy_set_header X-Real-IP $remote_addr;
		}
		location /static {
		alias /Byprice/static/;
		}
	}
```
8. Restart the server adn run the int the background app with gunicorn (To stop the thread pkill gunicorn)
```bash
$ sudo /etc/init.d/nginx restart
$ gunicorn byprice:application -b 0.0.0.0:8000 --reload &
```
9. On the default http://IP_Address:8000/db the whole database an be consulted, and add a 'keyword' to the path for a search http://IP_Address:8000/db/'keyword'/

## Configuring MySQL Server

1. SSH into the virtual machine.
2. Install all packages needed:
```bash
$ sudo apt-get install python3-pip
$ sudo easy_install3 pip
$ sudo apt-get install python-dev python-pip libxml2-dev libxslt1-dev zlib1g-dev libffi-dev libssl-dev
$ sudo apt-get install git
$ sudo apt-get update
$ sudo apt-get install mysql-server
$ sudo pip install virtualenv
```
3. Clone repository.
4. Enter as administrator into the mysql server running __mysql -u root -p__
5. Create a new database, new user and grant respective privileges
```bmysql
CREATE DATABASE testdb;
CREATE USER 'testuser'@'localhost' IDENTIFIED BY 'password';
GRANT ALL ON testdb.* TO 'testuser'@'localhost';
QUIT;
```
6. Create virtual environment __virtualenv venv__  and source it __source ./venv/bin/activate__
7. Install all dependencies with __pip install -r requirements.txt__
8. Now run __sudo crontab -e__ and add the following command into the file:
```
0 * * * * /home/user/byprice/crawlupdate
```
9. Create a new user from another host into the MySQL server  __mysql -u root -p__
```mysql
CREATE USER 'user'@'IPADDRESS' IDENTIFIED BY 'password';
GRANT ALL PRIVILEGES ON testdb.* TO 'user'@'IPADDRESS';
FLUSH PRIVILEGES;
QUIT;
```
10. Finally edit using __sudo nano /etc/mysql/my.cfg__ and comment the __bind-address = 127.0.0.1__ line.
