from flask import Flask, request, jsonify
from db import get_db_connection

app = Flask(__name__)

# 提交愿望
@app.route('/submit_wish', methods=['POST'])
def submit_wish():
    data = request.json
    name = data.get('name')
    wish = data.get('wish')

    if not name or not wish:
        return jsonify({'error': 'Name and wish are required'}), 400

    conn = get_db_connection()
    try:
        with conn.cursor() as cursor:
            sql = 'INSERT INTO wishes (name, wish) VALUES (%s, %s)'
            cursor.execute(sql, (name, wish))
        conn.commit()
        return jsonify({'message': 'Wish submitted successfully'}), 201
    finally:
        conn.close()

# 获取愿望列表
@app.route('/get_wishes', methods=['GET'])
def get_wishes():
    conn = get_db_connection()
    try:
        with conn.cursor() as cursor:
            sql = 'SELECT * FROM wishes'
            cursor.execute(sql)
            wishes = cursor.fetchall()
        return jsonify(wishes), 200
    finally:
        conn.close()

if __name__ == '__main__':
    app.run(debug=True)