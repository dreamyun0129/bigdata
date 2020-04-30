import numpy as np
import matplotlib.pyplot as plt
from sklearn.svm import SVC

from accuracy import getAcc
from preprocessing import creat_trainset

train_tf, train_class, test_tf, test_class, = creat_trainset()

# 然後要開一台SVC
clf = SVC()

# 開始訓練：clf.fit(輸入資料,正確答案)

train_x_svm = []
train_y_svm = []
for place in train_tf.keys():
    train_x_svm.append(train_tf.get(place))

for name in train_class.keys():
    train_y_svm.append(train_class.get(name))

clf.fit(train_x_svm, train_y_svm)

test_x_svm = []
for name in test_tf.keys():
    test_x_svm.append(test_tf.get(name))

y_test_predict = clf.predict(test_x_svm)
y_test_predict = y_test_predict.tolist()

y_true = []
for name in test_class.keys():
    y_true.append(test_class.get(name))


confmat = confusion_matrix(y_true=y_true, y_pred=y_test_predict)
fig, ax = plt.subplots(figsize=(5, 5))
ax.matshow(confmat, cmap=plt.cm.Blues, alpha=0.3)
for i in range(confmat.shape[0]):
    for j in range(confmat.shape[1]):
        ax.text(x=j, y=i, s=confmat[i, j], va='center', ha='center')
plt.xlabel('predicted label', fontsize=12)
plt.ylabel('true label', fontsize=12)
plt.savefig('svm_result.jpg')
plt.show()

svm_acc = getAcc(y_test_predict, y_true)

print(svm_acc)


