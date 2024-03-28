import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report, confusion_matrix, accuracy_score

data = pd.read_csv('/content/kepler_data (1).csv', delimiter=',', skiprows=range(52))

#-------------- Step 2: Data Exploration
print(data.head())
print(data['koi_disposition'].value_counts())

#------------------Step 3: Data Preprocessing
#------------------Separate features and target variable
X = data.drop('koi_disposition', axis=1)
y = data['koi_disposition']

#------------------Encode the target variable
label_encoder = LabelEncoder()
y = label_encoder.fit_transform(y)

#------------------Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

#----------------- Step 4: Model Building
rf_classifier = RandomForestClassifier(n_estimators=100, random_state=42)
rf_classifier.fit(X_train, y_train)

#------------------Step 5: Model Evaluation
y_pred = rf_classifier.predict(X_test)

print("Classification Report:")
print(classification_report(y_test, y_pred))

print("Confusion Matrix:")
print(confusion_matrix(y_test, y_pred))

print("Accuracy Score:", accuracy_score(y_test, y_pred))

