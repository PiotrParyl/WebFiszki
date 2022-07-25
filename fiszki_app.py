from flask import Flask, render_template
import mysql.connector
from setings import *



#======================= bd.connection #=======================

db = mysql.connector.connect(
    host= host,
    user=user,
    passwd=passwd,
    database=database,
)

mycursor = db.cursor()


#======================= Web App #======================= 

app = Flask(__name__)


@app.route('/')
def home():

    return render_template("home.html"  )


if __name__==("__main__"):
    
    app.run(debug=True)