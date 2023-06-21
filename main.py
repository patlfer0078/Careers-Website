from flask import Flask, render_template, jsonify

app = Flask(__name__)

JOBS = [
  {
    'id':1, 
    'title': 'Data Analyst',
    'location': 'Dallas, Texas',
    'salary': '63,000.00',
  },
  {
    'id':2, 
    'title': 'Data Scientist',
    'location': 'San Antonio, Texas',
    'salary': '80,000.00',
  },
  {
    'id':3, 
    'title': 'Frontend Engineer',
    'location': 'Remote',
    'salary': '56,000.00',
  },
  {
    'id':4, 
    'title': 'Backend Engineer',
    'location': 'San Francisco, California',
    'salary': '65,000.00',
  }
]
@app.route("/")
def hello_world():
  return render_template('home.html', jobs=JOBS)

@app.route("/api/jobs")
def list_jobs():
    return jsonify(JOBS)

if __name__ == "__main__":
  app.run(host='0.0.0.0', debug=True)