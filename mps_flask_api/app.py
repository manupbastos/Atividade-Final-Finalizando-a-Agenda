from flask import render_template
from flask_mysqldb import MySQL
import connexion

app = connexion.App(__name__, specification_dir="./")
app.app.config["MYSQL_HOST"] = "localhost"
app.app.config["MYSQL_PORT"] = 3306
app.app.config["MYSQL_USER"] = "mps manu"
app.app.config["MYSQL_PASSWORD"] = "mamute123"
app.app.config["MYSQL_DB"] = "mydb"
app.add_api("swagger.yml")
MYSQL_DB = MySQL(app.app)

@app.route("/")
def home():
    return render_template("home.html")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)