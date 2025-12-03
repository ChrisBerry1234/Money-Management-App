from flask import Flask, render_template, request, redirect, url_for

TRANSACTIONS = [
    {'id': 1, 'date': '2023-06-01', 'amount': 100},
    {'id': 2, 'date': '2023-06-02', 'amount': 200},
    {'id': 3, 'date': '2023-06-03', 'amount': 300}
]

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("transactions.html", data = TRANSACTIONS)

@app.route("/add_transaction", methods=["GET","POST"])
def add_transactions():

    if request.method == "GET":
        return render_template("addtransaction.html")

    transaction = {
        'id': len(TRANSACTIONS)+1,
        'date': request.form.get("date"),
        'amount': request.form.get("amount"),
    }

    TRANSACTIONS.append(transaction)

    return redirect(url_for("index"))

@app.route("/edit/<int:id>", methods=["GET", "POST"])
def edit_transaction(id):

    if request.method == "GET":
        for transaction in TRANSACTIONS:
            if id == transaction['id']:
                return render_template("edittransaction.html", transaction = transaction)

    return redirect(url_for("index"))
app.run(debug=True)