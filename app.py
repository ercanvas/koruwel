from flask import Flask, render_template, request, jsonify
from db_config import get_db_connection

app = Flask(__name__)


@app.route('/')
def home():
      return render_template("index.html")

@app.route('/transactions')
def transactions():
      data = [
            {"id": 1, "amount": 100, "category": "Gıda", "date":"2024-12-02"},
            {"id": 2, "amount": 200, "category": "Eğlence", "date":"2024-12-02"},
            {"id": 3, "amount": 300, "category": "Tadilat", "date":"2024-12-02"},
            {"id": 4, "amount": 400, "category": "Tadilat", "date":"2024-12-02"}
      ]
      return render_template('transactions.html', transactions=data)

@app.route('/add_user', methods=['POST'])
def add_user():
      data = request.json
      username = data['username']
      password = data['password']
      email = data.get('email', None)

      connection = get_db_connection()
      cursor = connection.cursor()

      query = "INSERT INTO users (username, password, email) VALUES (%s, %s, %s)"
      cursor.execute(query, (username, password, email))
      connection.commit()
      cursor.close()
      connection.close()

      return jsonify({"message": "user added succesfully"}), 201

if __name__ == '__main__':
      app.run(debug=True)