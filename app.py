from flask import Flask, render_template, request
import psycopg2

app = Flask(__name__)


conn = psycopg2.connect(
    host="localhost",
    database="arg_db",
    user="postgres",
    password="akash1234"
)
cur = conn.cursor()

@app.route('/')
def index():
    return render_template('login.html')

@app.route('/login', methods=['POST'])
def login():
    username = request.form['username']
    password = request.form['password']

    cur .execute("INSERT INTO users (username, password) VALUES (%s, %s)", (username, password))
    conn.commit()
    return f"Stroed in database:username={username}"

if __name__ =='__main__':
    app.run(debug=True)