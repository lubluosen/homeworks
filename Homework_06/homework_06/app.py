from flask import Flask, request, jsonify, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://user:password@db/mydb'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


class Record(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    value = db.Column(db.String(50), nullable=False)


@app.route('/')
def hello_world():
    return 'index page'


@app.route('/add', methods=['POST'])
def add_record():
    data = request.get_json()
    new_record = Record(name=data['name'], value=data['value'])
    db.session.add(new_record)
    db.session.commit()
    return jsonify({'message': 'Запись успешно добавлена'})


@app.route('/records', methods=['GET'])
def get_records():
    records = Record.query.all()
    return render_template('records.html', records=records)


if __name__ == "__main__":
    app.run('127.0.0.1', 8000)
