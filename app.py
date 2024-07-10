from flask import Flask, render_template, request, redirect, url_for, flash

app = Flask(__name__)
app.secret_key = 'supersecretkey'

# Correct password
CORRECT_PASSWORD = 'mypassword'

@app.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        password = request.form['password']
        if password == CORRECT_PASSWORD:
            flash('Password is correct! Welcome to the imaginary app.', 'success')
            return redirect(url_for('dashboard'))
        else:
            flash('Incorrect password. Please try again.', 'danger')
    return render_template('login.html')

@app.route('/dashboard')
def dashboard():
    return render_template('dashboard.html')

if __name__ == '__main__':
    app.run(debug=True)
