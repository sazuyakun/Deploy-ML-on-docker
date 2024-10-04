import pickle
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
import numpy as np

data = load_iris()
X, y = data.data, data.target

X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=42, test_size=0.2)

model = RandomForestClassifier()
model.fit(X_train, y_train)

prediction = model.predict(X_test)

accuracy = accuracy_score(y_test, prediction)
print(f"Accuracy: {accuracy * 100:.2f}")

with open('model.pkl', 'wb') as f:
    pickle.dump(model, f)

print("Training and saving successful")

