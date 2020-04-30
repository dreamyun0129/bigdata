import math


def cosine_similarity(v1, v2):
    # 計算兩個向量的正弦相似度。距離越近，相似度數值會越高。

    sum_xx, sum_xy, sum_yy = 0.0, 0.0, 0.0
    for i in range(0, len(v1)):
        sum_xy += v1[i] * v2[i]
        sum_xx += math.pow(v1[i], 2)
        sum_yy += math.pow(v2[i], 2)

    return sum_xy / math.sqrt(sum_xx * sum_yy)
