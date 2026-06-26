from flask import Flask, render_template, request
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier

app = Flask(__name__, template_folder='.')

# Dataset Load
data = pd.read_csv("student_data.csv")

# Features and Target
X = data[["StudyHours", "Attendance", "PreviousMarks"]]
y = data["Performance"]

# Train Model
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

model = DecisionTreeClassifier()
model.fit(X_train, y_train)

# Login Page
@app.route('/', methods=['GET', 'POST'])
def login():

    if request.method == 'POST':

        username = request.form['username']
        password = request.form['password']

        if username == "student" and password == "Student@2026":
            return render_template('dashboard.html')

        else:
            return render_template(
                'login.html',
                error="Invalid Username or Password"
            )

    return render_template('login.html')

# Dashboard
@app.route('/dashboard')
def dashboard():
    return render_template('dashboard.html')

# Prediction Page
@app.route('/home')
def home():
    return render_template('index.html')

# ML Prediction
@app.route('/predict', methods=['POST'])
def predict():

    study_hours = int(request.form['study_hours'])
    attendance = int(request.form['attendance'])
    previous_marks = int(request.form['previous_marks'])

    result = model.predict([[study_hours, attendance, previous_marks]])

    return render_template(
        'result.html',
        prediction=result[0]
    )

# About Page
@app.route('/about')
def about():
    return render_template('about.html')

# History Page
@app.route('/history')
def history():
    return render_template('history.html')

# Contact Page
@app.route('/contact')
def contact():
    return render_template('contact.html')

if __name__ == '__main__':
    app.run(debug=True)