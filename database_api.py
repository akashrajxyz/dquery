import sqlite3
from flask import Flask, jsonify

app = Flask(__name__)

@app.errorhandler(404)
def page_not_found(e):
    return "Use -> /1/queries/count/<date|time>", 404

def get_count(query):
        conn = sqlite3.connect('site.db')
        c = conn.cursor()
        fquery = "SELECT count(DISTINCT value)  FROM ln WHERE date LIKE '{}%'".format(query)
        try:
                result = c.execute(fquery).fetchone()
        except sqlite3.Error as e:
                print("An error occured: ", e.args[0])
        conn.close()
        return result[0]

@app.route('/1/queries/count/<string:date_prefix>')
def main(date_prefix):
        return jsonify({ "count" : get_count(date_prefix)})


if __name__=="__main__":
        app.run(debug=True)

