from flask import Flask, render_template, jsonify

app= Flask(__name__)

JOBS=[{"id": 1,
      "title":"Data Analyst",
      "location":"Ibadan, Nigeria",
      "salary":"$7000.00"},
     {"id": 2,
      "title":"Data Engineer",
      "location":"Lagos, Nigeria",
      "salary":"$7500.00"},
     {"id": 3,
      "title":"Machine Learning Engineer",
      "location":"Remote, Nigeria",
      "salary":"$8000.00"},
     {"id": 4,
      "title":"Data Scientist",
      "location":"Abuja, Nigeria",
      "salary":"$8800.00"}]

@app.route("/")
def hello():
  return render_template("home.html",jobs=JOBS,
                        first_name="Oluwafunbi")

@app.route("/api/jobs")
def listjobs():
  return jsonify(JOBS)

if __name__ == "__main__":
  app.run(host="0.0.0.0",debug=True)