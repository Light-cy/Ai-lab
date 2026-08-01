import pandas as ali
data = ali.read_csv("students.csv")
print(data)

Y = data['GradeClass'].values
print(Y)

# Option 1 (Same style as Naive Bayes using iloc)
X = data.iloc[0:2392, 0:14].values  

# Option 2 (Safer method – automatically removes label column)
# X = data.drop('GradeClass', axis=1).values  

print(X)

from sklearn.model_selection import train_test_split

# ---- DIFFERENT FROM NAIVE BAYES ----
from sklearn.neighbors import KNeighborsClassifier  
# (Naive Bayes used: from sklearn.naive_bayes import GaussianNB)
# ------------------------------------

X_train, X_test, y_train, y_test = train_test_split(
    X, Y, test_size=0.5, random_state=40
)

# Scaler = StandardScaler() 
# X_train = Scaler.fit_transform(X_train)
# X_test = Scaler.transform(X_test)

# ---- DIFFERENT FROM NAIVE BAYES ----
model = KNeighborsClassifier(n_neighbors=5)  
# (Naive Bayes used: model = GaussianNB())
# ------------------------------------

print(X_train)

