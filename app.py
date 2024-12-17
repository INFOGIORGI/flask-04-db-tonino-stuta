from flask import Flask, render_template
from flask_mysqldb import MySQL
app = Flask(__name__)

app.config['MYSQL_HOST'] = '138.41.20.102'
app.config['MYSQL_PORT'] = 53306
app.config['MYSQL_DB'] = 'w3school'
app.config['MYSQL_USER'] = 'ospite'
app.config['MYSQL_PASSWORD'] = 'ospite'
mysql = MySQL(app)


@app.route("/")
def home():
    return render_template("index.html")

@app.route("/prodotti")
def products():
    return render_template("products.html")
app.run(debug = True)
