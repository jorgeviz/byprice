# Drugs Request Pact

The drugs request microservice provides a full dataset from a retailer that returns all items from the drugs department with its correspondant parameters. Data is taken with a web crawler made using scrapy. 

##Features

+ Web crawling through the drugs department to retrieve data.
+ Stores scraped data into a MySQL database.
+ Access from the complete database of drugs from such retailer.
+ Quick search from a request of a determined value.

## How would I use the Request microservice?

1. Create a **virtualenv** and install all requirements
2. Create a database called __testdb__ with a __test623__ password from your MySQL manager
2. Source into the *virtualenv* created and run __scrapy crawl medicamento__ from the ./scrapmex/farmacia_scrap/ directory
2. Run the **byprice.py** file 
3. On the default IP Address http://0.0.0.0:5000/ , the whole database can be consulted on http://0.0.0.0:5000/db 
5. And look for a drug given a certain 'keyword' in http://0.0.0.0:5000/db/'keyword'/


