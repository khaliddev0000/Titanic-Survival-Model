import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score

df = pd.read_csv("train.csv")
df['Embarked']= df['Embarked'].fillna(df['Embarked'].mode()[0])
df['Age']=df['Age'].fillna(df['Age'].median())
x = df.drop(columns=['Survived', 'Name','PassengerId', 'Ticket', 'Cabin'])

X = pd.get_dummies(x, dtype=int)
y = df['Survived']

X_train,X_test,y_train,y_test = train_test_split(X, y, test_size=0.2, random_state=42)

model = DecisionTreeClassifier(max_depth=4,random_state=42)
model.fit(X_train, y_train)
predictions = model.predict(X_test)
score = accuracy_score(y_test, predictions)
print(f"Model Accuracy: {score*100}%")_









