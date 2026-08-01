import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.neighbors import KNeighborsClassifier
from sklearn.naive_bayes import GaussianNB
from sklearn.preprocessing import LabelEncoder
from sklearn.preprocessing import OneHotEncoder
from sklearn.feature_extraction.text import TfidfVectorizer

dataset = pd.read_csv("StudentFeedback.csv")
dataset.dropna(inplace=True)
dataset.drop_duplicates(inplace=True)
label_encoder = LabelEncoder()
tfidf = TfidfVectorizer()
Y = label_encoder.fit_transform(dataset['label'])
X = tfidf.fit_transform(dataset['text'])




from sklearn.metrics import confusion_matrix, precision_score, recall_score, f1_score
import matplotlib.pyplot as plt
import seaborn as sns
# Confusion Matrix
cm = confusion_matrix(y_test, y_pred)
plt.figure(figsize=(4,3))
sns.heatmap(cm, annot=True, fmt="d", cmap="Blues")
plt.xlabel("Predicted")
plt.ylabel("Actual")
plt.title("Confusion Matrix")
plt.show()

# Metrics
precision = precision_score(y_test, y_pred, average='weighted')
recall = recall_score(y_test, y_pred, average='weighted')
f1 = f1_score(y_test, y_pred, average='weighted')

# Bar Chart
metrics = ['Precision', 'Recall', 'F1 Score']
values = [precision, recall, f1]
plt.bar(metrics, values, color=['green', 'blue', 'orange'])
plt.ylim(0, 1)
plt.title("Model Performance Metrics")
plt.show()
