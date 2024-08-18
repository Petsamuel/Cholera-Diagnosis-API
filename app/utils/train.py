import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder, StandardScaler
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report
import json

# Load the dataset from a JSON file
with open("../cholera_data.json", "r") as f:
    data = json.load(f)
    
df = pd.DataFrame(data)

print(df.head())

# Handle categorical values
le = LabelEncoder()
df['Gender'] = le.fit_transform(df['Gender'])
df['Location'] = le.fit_transform(df['Location'])

# Handle missing values
df.fillna(df.mean(), inplace=True)
df['Gender'].fillna(df['Gender'].mode()[0], inplace=True)
df['Location'].fillna(df['Location'].mode()[0], inplace=True)

# Handle the date column
df['DateOnset'] = pd.to_datetime(df['DateOnset'])
df['OnsetDay'] = df['DateOnset'].dt.day
df['OnsetMonth'] = df['DateOnset'].dt.month
df['OnsetWeekday'] = df['DateOnset'].dt.weekday
df.drop('DateOnset', axis=1, inplace=True)

# Split data into features and target
X = df.drop('Cholera', axis=1)
y = df['Cholera']

# Split data into train and test sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Feature scaling
scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

# Train model
model = RandomForestClassifier()
print("Training model...", model)
model.fit(X_train, y_train)

# Model evaluation
y_pred = model.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)
print("Accuracy:", accuracy)
print(classification_report(y_test, y_pred))
