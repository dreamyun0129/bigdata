import re


def tf(texts, keywords):
    texts = re.sub('\W+', '', texts)
    for length in range(2, 5):
        for i in range(len(texts) - (length - 1)):
            result = texts[i:i+length]
            if result in keywords:  # 統計數量
                keywords[result] += 1
                # print(result)

    return keywords

