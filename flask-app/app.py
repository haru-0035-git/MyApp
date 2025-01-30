from flask import Flask, request, render_template, redirect
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///kakeibo.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# データベースのモデル（収支の記録）
class Transaction(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.Date, nullable=False, default=datetime.today)
    category = db.Column(db.String(50), nullable=False)
    amount = db.Column(db.Integer, nullable=False)
    type = db.Column(db.String(10), nullable=False)  # "income" or "expense"

# 📝 収支登録ページ（フォーム表示 & データ追加）
@app.route('/add', methods=['GET', 'POST'])
def add():
    if request.method == 'POST':
        date = datetime.strptime(request.form['date'], "%Y-%m-%d")
        category = request.form['category']
        amount = int(request.form['amount'])
        type = request.form['type']

        new_transaction = Transaction(date=date, category=category, amount=amount, type=type)
        db.session.add(new_transaction)
        db.session.commit()
        return redirect('/list')

    return render_template('add.html')

# 📜 収支一覧ページ（データ表示）
@app.route('/list')
def list_transactions():
    transactions = Transaction.query.order_by(Transaction.date.desc()).all()
    total_income = sum(t.amount for t in transactions if t.type == 'income')
    total_expense = sum(t.amount for t in transactions if t.type == 'expense')

    return render_template('list.html', transactions=transactions, total_income=total_income, total_expense=total_expense)

# ✏️ 収支の編集ページ
@app.route('/edit/<int:id>', methods=['GET', 'POST'])
def edit(id):
    transaction = db.session.get(Transaction, id)
    if not transaction:
        return redirect('/list')

    if request.method == 'POST':
        transaction.date = datetime.strptime(request.form['date'], "%Y-%m-%d")
        transaction.category = request.form['category']
        transaction.amount = int(request.form['amount'])
        transaction.type = request.form['type']

        db.session.commit()
        return redirect('/list')

    return render_template('edit.html', transaction=transaction)

# 🗑 収支の削除
@app.route('/delete/<int:id>')
def delete(id):
    transaction = db.session.get(Transaction, id)
    if transaction:
        db.session.delete(transaction)
        db.session.commit()
    return redirect('/list')

# データベース初期化
with app.app_context():
    db.create_all()

if __name__ == '__main__':
    app.run(debug=True)
