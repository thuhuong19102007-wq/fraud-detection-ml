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
# Đếm số giao dịch gian lận
fraud_count = data['Class'].sum()

# Đếm tổng giao dịch
total_transactions = len(data)

print("Total Transactions:", total_transactions)
print("Fraud Transactions:", fraud_count)
import matplotlib.pyplot as plt

# Vẽ biểu đồ
# Chia dữ liệu
normal = data[data['Class'] == 0]
fraud = data[data['Class'] == 1]

# Vẽ giao dịch bình thường
plt.scatter(
    normal['Time'],
    normal['Amount'],
    label='Normal Transaction',
    alpha=0.5
)

# Vẽ giao dịch bất thường
plt.scatter(
    fraud['Time'],
    fraud['Amount'],
    label='Fraud Transaction',
    alpha=0.8
)

# Tiêu đề và chú thích
plt.xlabel("Time")
plt.ylabel("Amount")
plt.title("Fraud Detection in Accounting Transactions")

# Hiện chú thích
plt.legend()

# Hiện biểu đồ
plt.show()


# Tên trục
plt.xlabel("Time")
plt.ylabel("Amount")

# Tiêu đề
plt.title("Credit Card Fraud Detection")

# Hiển thị biểu đồ
plt.show()