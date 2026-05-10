import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score

# Đọc dataset
data = pd.read_csv("data/creditcard.csv")

# Input (dữ liệu để học)
X = data.drop(columns=['Class'])

# Output (đáp án)
y = data['Class']

# Chia dữ liệu train/test
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

# Tạo model AI
model = DecisionTreeClassifier(max_depth=4)

# Train model
model.fit(X_train, y_train)

# Dự đoán
y_pred = model.predict(X_test)

# Tính accuracy
acc = accuracy_score(y_test, y_pred)

print("Accuracy:", acc)
import matplotlib.pyplot as plt

# Vẽ biểu đồ
plt.scatter(
    data['Time'],
    data['Amount'],
    c=data['Class']
)

# Tên trục
plt.xlabel("Time")
plt.ylabel("Amount")

# Tiêu đề
plt.title("Credit Card Fraud Detection")

# Hiển thị biểu đồ
plt.show()