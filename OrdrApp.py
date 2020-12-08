from flask import Flask, render_template, request
from pymysql import connections
import os
import boto3
from config import *

app = Flask(__name__)

bucket = custombucket
region = customregion

db_conn = connections.Connection(
    host=customhost,
    port=3306,
    user=customuser,
    password=custompass,
    db=customdb

)
output = {}
table = 'order-form'


@app.route("/", methods=['GET', 'POST'])
def home():
    return render_template('AddEmp.html')


@app.route("/addordr", methods=['POST'])
def AddOrdr():
    cust_name = request.form['cust_name']
    std_chair = request.form['std-chair']
    bnch_4_2 = request.form['bnch_4_2']
    pic_table = request.form['pic_table']
    bar = request.form['bar']
    
    insert_sql = "INSERT INTO order-form VALUES (%s, %s, %s, %s, %s)"
    cursor = db_conn.cursor()

    try:

        cursor.execute(insert_sql, (cust_name, std_chair, bnch_4_2, pic_tbl, bar))
        db_conn.commit()
        cust_name = ""
        
        

        except Exception as e:
            return str(e)

    finally:
        cursor.close()

    print("order submited...")
    return render_template('AddOrdrOutput.html', name=cust_name)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80, debug=True)
