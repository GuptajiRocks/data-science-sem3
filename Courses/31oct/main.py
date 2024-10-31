from flask import Flask, render_template, request, redirect, url_for, session
from waitress import serve

app = Flask(__name__)

# Replace with your actual database setup
users = {
    "user1": {"name": "User 1", "balance": 1000},
    "user2": {"name": "User 2", "balance": 500},
}

@app.route('/')
def login():
    return render_template('login.html')

@app.route('/dashboard')
def dashboard():
    if 'username' in session:
        user = users.get(session['username'])
        return render_template('dashboard.html', user=user)
    else:
        return redirect(url_for('login'))

@app.route('/transfer', methods=['GET', 'POST'])
def transfer():
    if request.method == 'POST':
        sender = session['username']
        receiver = request.form['receiver']
        amount = int(request.form['amount'])

        sender_balance = users[sender]['balance']
        if sender_balance >= amount:
            users[sender]['balance'] -= amount
            users[receiver]['balance'] += amount
            return redirect(url_for('dashboard'))
        else:
            return render_template('transfer.html', error='Insufficient balance')
    else:
        return render_template('transfer.html')

# ... (other routes for registration, logout, etc.)


if __name__ == "__main__":
    serve(app, host="0.0.0.0", port=8000)
