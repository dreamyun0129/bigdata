import numpy as np
from sklearn.metrics import confusion_matrix
import matplotlib.pyplot as plt
from accuracy import getAcc
from model_knn import knn_classify
from preprocessing import creat_trainset

if __name__ == '__main__':

    train_tf, train_class, test_tf, test_class, = creat_trainset()

    # calculate predict label
    predict_class_dict = {}
    i = 0
    for key, value in test_tf.items():
        input_tf = test_tf.get(key)
        predict_class = knn_classify(input_tf, train_tf, train_class, k=10)
        predict_class_dict[key] = predict_class
    print(predict_class_dict)
    np.save('my_predict_class.npy', predict_class_dict)

    y_prd_knn = []
    for name in predict_class_dict.keys():
        y_prd_knn.append(predict_class_dict.get(name))

    y_true_knn = []
    for name in test_class.keys():
        y_true_knn.append(test_class.get(name))

    # plot confusion_matrix
    confmat = confusion_matrix(y_true=y_true_knn, y_pred=y_prd_knn)
    fig, ax = plt.subplots(figsize=(5, 5))
    ax.matshow(confmat, cmap=plt.cm.Blues, alpha=0.3)
    for i in range(confmat.shape[0]):
        for j in range(confmat.shape[1]):
            ax.text(x=j, y=i, s=confmat[i, j], va='center', ha='center')
    plt.xlabel('predicted label', fontsize=12)
    plt.ylabel('true label', fontsize=12)
    plt.savefig('knn_result.jpg')
    plt.show()

    # 準確率
    knn_acc = getAcc(y_prd_knn, y_true_knn)
    print(knn_acc)
