import pandas as pd

data = pd.read_csv("student_data.csv")

print(data.head())
print(data.shape)
import pandas as pd

data = pd.read_csv("student_data.csv")

print(data.head())
print(data.shape)

from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier

X = data[["StudyHours", "Attendance", "PreviousMarks"]]
y = data["Performance"]

X_train, X_test, y_train, y_test = train_test_split(
    X, y,
    test_size=0.2,
    random_state=42
)

model = DecisionTreeClassifier()

model.fit(X_train, y_train)

print("Model Trained Successfully")
from sklearn.metrics import accuracy_score

y_pred = model.predict(X_test)

accuracy = accuracy_score(y_test, y_pred)

print("Accuracy:", accuracy)
new_student = [[4, 80, 65]]

result = model.predict(new_student)

print("Prediction:", result[0])