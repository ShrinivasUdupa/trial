import logging
import mysql.connector

# Database Connectivity
mydb = mysql.connector.connect(host = "localhost",user = "root",passwd = "root",db = "assessment4")

logging.basicConfig(filename="logf.txt",
                            filemode='a',
                            format='%(asctime)s - %(message)s',
                            level=logging.INFO)

logging.info("Database connected")
class Database:
    def database_operation(self):
        cursor = mydb.cursor()

        # To find a Maximum - sold product with product details fetched

        cursor.execute("select product_name, product_code, price from (select product_name, product_code, price, dense_rank() over(order by product_quantity desc) as r from product p join sale s on p.id = s.id) as t where r = 1")
        logging.info("Maximum - sold product with product details fetched")
        max_sold = cursor.fetchall()
        print("Maximum - sold product with product details")
        print(max_sold)

        # To find a Minimum - sold product with product details fetched

        cursor.execute("select product_name, product_code, price from (select product_name, product_code, price, dense_rank() over(order by product_quantity) as r from product p join sale s on p.id = s.id) as t where r = 1")
        logging.info("Minimum - sold product with product details fetched")
        min_sold = cursor.fetchall()
        print("Minimum - sold product with product details")
        print(min_sold)

        # To Get the billing date from user and print the product details and total amount of displaying products

        date_inp = input("Enter a date : ")
        cursor.execute("select product_name, product_code, price*product_quantity as total_amount from product p join sale s on p.id = s.id where bill_date = %s",(date_inp,))
        logging.info("Billing Date: ")
        bill_dates = cursor.fetchall()
        print("Billing Date ")
        print(bill_dates)

       
        mydb.commit()

        mydb.close()

data = Database()
data.database_operation()
#
# #*******************************O/P*********************************************
#
# # Maximum - sold product with product details
# # [('YAMAHA Speakers', 'YHT-1840', 26500)]
# # Minimum - sold product with product details
# # [('JBL Speakers', 'JBL-100', 18600)]
# # Enter a date : 2020-01-01
# # Billing Date
# # [('YAMAHA Speakers', 'YHT-1840', 106000)]
# # Enter a product code : SONY-LED-S43
# # Product code:
# # [('SONY LED TV', 'SONY-LED-S43', 58300)]
# # Successfully inserted
