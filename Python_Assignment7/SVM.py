import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.svm import SVC
from sklearn.metrics import classification_report, accuracy_score
from sklearn.datasets import load_iris
iris = load_iris()
X = iris.data 
y = iris.target  
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)
scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)
svm_classifier = SVC(kernel='linear', random_state=42)
svm_classifier.fit(X_train, y_train)
y_pred = svm_classifier.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)
print(f"Accuracy: {accuracy:.2f}")
print("\nClassification Report:")
print(classification_report(y_test, y_pred, target_names=iris.target_names))
new_sample = np.array([[5.1, 3.5, 1.4, 0.2]])  
new_sample_scaled = scaler.transform(new_sample)
prediction = svm_classifier.predict(new_sample_scaled)
predicted_class = iris.target_names[prediction[0]]
print(f"\nPredicted class for the new sample: {predicted_class}")
