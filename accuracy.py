def getAcc(predict, ans):
    correct = 0
    for i in range(len(predict)):
        if predict[i] == ans[i]:
            correct += 1
    return (correct / len(predict)) * 100
