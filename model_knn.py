from similarity import cosine_similarity


def knn_classify(test_tf, train_tf, train_class, k):
    tf_distance = {}
    # 計算每個訓練集合特徵關鍵字字詞頻率向量和輸入向量的距離
    for place in train_tf.keys():
        tf_distance[place] = cosine_similarity(train_tf.get(place), test_tf)

    # 把距離排序，取出k個最近距離的分類

    class_count = {}
    # print('(2) 取K個最近鄰居的分類, k = %d' % k)
    for i, place in enumerate(sorted(tf_distance, key=tf_distance.get, reverse=True)):
        current_class = train_class.get(place)
        # print('\tTF(%s) = %f, class = %s' % (place, tf_distance.get(place), current_class))
        class_count[current_class] = class_count.get(current_class, 0) + 1
        if (i + 1) >= k:
            break

    print('(3) K個最近鄰居分類出現頻率最高的分類當作最後分類')
    input_class = ''
    for i, c in enumerate(sorted(class_count, key=class_count.get, reverse=True)):
        if i == 0:
            input_class = c
        print('\t%s, %d' % (c, class_count.get(c)))

    print('(4) 分類結果 = %s' % input_class)

    return str(input_class)
