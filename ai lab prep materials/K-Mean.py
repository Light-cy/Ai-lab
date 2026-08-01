import pandas as ali
data = ali.read_csv("students.csv")
print(data)

# ---- DIFFERENT FROM NB & KNN ----
# K-Means is UNSUPERVISED → No label (Y) is separated
X = data.drop('GradeClass', axis=1).values  
# In NB & KNN we separated Y. Here we use only X.
# ---------------------------------

print(X)

from sklearn.model_selection import train_test_split

# ---- DIFFERENT FROM NB & KNN ----
# Train-test split is optional in clustering,
# but we keep it for evaluation similarity
X_train, X_test = train_test_split(
    X, test_size=0.5, random_state=40
)
# No y_train, y_test needed
# ---------------------------------

# ---- DIFFERENT FROM NB & KNN ----
# Feature Scaling (important for distance-based clustering)
from sklearn.preprocessing import StandardScaler
Scaler = StandardScaler()
X_train = Scaler.fit_transform(X_train)
X_test = Scaler.transform(X_test)
# ---------------------------------

# ---- DIFFERENT FROM NB & KNN ----
from sklearn.cluster import KMeans  
# Instead of GaussianNB or KNeighborsClassifier
# ---------------------------------

# ---- DIFFERENT FROM NB & KNN ----
model = KMeans(n_clusters=2, random_state=40)  
# n_clusters = K (number of clusters)
# In KNN we used n_neighbors
# In NB we used GaussianNB()
# ---------------------------------

model.fit(X_train)

# ---- DIFFERENT FROM NB & KNN ----
response = model.predict(X_test)  
# Predicts cluster numbers (0,1,...)
# Not class labels like NB & KNN
# ---------------------------------

print("Cluster Assignments:", response)
