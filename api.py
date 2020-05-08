from flask import Flask

app = Flask(__name__)

STUDENTS = {
  '1': {'name': 'Mark', 'age': 23, 'spec': 'math'},
  '2': {'name': 'Jane', 'age': 20, 'spec': 'biology'},
  '3': {'name': 'Peter', 'age': 21, 'spec': 'history'},
  '4': {'name': 'Kate', 'age': 22, 'spec': 'science'},
}

@app.route('/init')
def index():
  return STUDENTS

if __name__ == "__main__":
  app.run(host='127.0.0.1', port=5000, debug=True)