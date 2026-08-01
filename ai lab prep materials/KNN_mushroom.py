import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score, f1_score

# Load Mushroom Dataset
data = pd.read_csv("mushroom.csv")   # change filename if needed

# Separate features and target
X = data.drop('class', axis=1)   # class = target (0 edible, 1 poisonous)
y = data['class']

# Split data
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Apply KNN for different K values
for k in [3,5,7,11]:
    knn = KNeighborsClassifier(n_neighbors=k)
    knn.fit(X_train, y_train)
    y_pred = knn.predict(X_test)
    
    acc = accuracy_score(y_test, y_pred)
    f1  = f1_score(y_test, y_pred)
    
    print(f"K={k} → Accuracy={acc:.4f}  F1-Score={f1:.4f}")
