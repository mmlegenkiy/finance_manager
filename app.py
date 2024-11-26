from flask import Flask, request, render_template, redirect
from finance_manager.services.budget_manager import BudgetManager
from finance_manager.models.transactions import Transaction
from finance_manager.services.file_manger import FileManager


app = Flask(__name__)


@app.route('/', methods=['GET'])
def index():
    manager = BudgetManager()

    loaded_transactions = FileManager.load_from_file("transactions.json")

    return render_template('index.html', transactions=loaded_transactions)

@app.route('/add', methods=['GET', 'POST'])
def add():
    if request.method == 'POST':
        amount = request.form['amount']
        category = request.form['category']
        date = request.form['date'] # взяти поточну дату
        new_transactions = Transaction(amount=float(amount), category=category, date=date)
        manager = BudgetManager()
        loaded_transactions = FileManager.load_from_file("transactions.json")
#        Не встиг :(
    return render_template('add.html')

if __name__ == '__main__':
    app.run(debug=True)