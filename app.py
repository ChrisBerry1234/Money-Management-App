from flask import Flask, render_template

TRANSACTIONS = [
    {'id': 1, 'date': '2023-06-01', 'amount': 100},
    {'id': 1, 'date': '2023-06-02', 'amount': 200},
    {'id': 1, 'date': '2023-06-03', 'amount': 300}
]


app = Flask(__name__)

@app.route("/")
def index():
    return render_template("transactions.html", data = TRANSACTIONS)



app.run(debug=True)