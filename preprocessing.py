import csv
import pandas as pd
from count_tf import tf

def creat_trainset():
    all_df = pd.DataFrame(pd.read_excel('all.xlsx'))
    train_x = all_df[['id', 'title', 'content']]
    train_y = all_df[['id', 'label']]

    test_all_df = pd.DataFrame(pd.read_excel('test_all.xlsx'))
    test_x = test_all_df[['id', 'title', 'content']]
    test_y = test_all_df[['id', 'label']]

    train_key = {}
    for i in range(train_x.shape[0]):
        keywords = {'看漲': 0, '上漲': 0, '大漲': 0, '高利率': 0, '獲利': 0, '法規鬆綁': 0, '資金回流': 0,
                    '緩和': 0, '反彈': 0, '由負轉正': 0, '利多': 0, '強勢': 0, '突破': 0, '狂飆': 0,
                    '漲停板': 0, '受惠': 0, '多頭': 0, '轉往': 0, '漲勢': 0, '樂觀': 0, '大好': 0,
                    '看跌': 0, '下跌': 0, '大跌': 0, '下掉': 0, '走下坡': 0, '下滑升息': 0, '崩盤': 0,
                    '利空': 0, '惡化': 0, '衰退': 0, '壟罩': 0, '緊縮': 0, '不利': 0, '衝擊': 0, '軋空': 0,
                    '賣空': 0, '放空': 0, '配股減少': 0, '獲利減少': 0, '轉差': 0, '虧損': 0, '恐慌': 0,
                    '金融海嘯': 0, '悲觀': 0, '大壞': 0}
        for j in range(1, 3):
            keywords = tf(train_x.iloc[i][j], keywords)
        train_key[train_x.iloc[i][0]] = list(keywords.values())

    with open('train_key.csv', 'w', newline='') as csvfile:
        # 定義欄位
        fieldnames = ['id', 'features']

        # 將 dictionary 寫入 CSV 檔
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        # 寫入第一列的欄位名稱
        writer.writeheader()

        # 寫入資料
        for key, val in train_key.items():
            writer.writerow({'id': key, 'features': val})

    test_key = {}
    for i in range(test_x.shape[0]):
        keywords = {'看漲': 0, '上漲': 0, '大漲': 0, '高利率': 0, '獲利': 0, '法規鬆綁': 0, '資金回流': 0,
                    '緩和': 0, '反彈': 0, '由負轉正': 0, '利多': 0, '強勢': 0, '突破': 0, '狂飆': 0,
                    '漲停板': 0, '受惠': 0, '多頭': 0, '轉往': 0, '漲勢': 0, '樂觀': 0, '大好': 0,
                    '看跌': 0, '下跌': 0, '大跌': 0, '下掉': 0, '走下坡': 0, '下滑升息': 0, '崩盤': 0,
                    '利空': 0, '惡化': 0, '衰退': 0, '壟罩': 0, '緊縮': 0, '不利': 0, '衝擊': 0, '軋空': 0,
                    '賣空': 0, '放空': 0, '配股減少': 0, '獲利減少': 0, '轉差': 0, '虧損': 0, '恐慌': 0,
                    '金融海嘯': 0, '悲觀': 0, '大壞': 0}
        for j in range(1, 3):
            keywords = tf(test_x.iloc[i][j], keywords)
        test_key[test_x.iloc[i][0]] = list(keywords.values())

    with open('test_key.csv', 'w', newline='') as csvfile:
        # 定義欄位
        fieldnames = ['id', 'features']

        # 將 dictionary 寫入 CSV 檔
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        # 寫入第一列的欄位名稱
        writer.writeheader()

        # 寫入資料
        for key, val in test_key.items():
            writer.writerow({'id': key, 'features': val})

    train_ylabel = {}
    for i in range(train_y.shape[0]):
        if train_y.iloc[i][1] == 'up':
            train_ylabel[train_y.iloc[i][0]] = 'up'
        else:
            train_ylabel[train_y.iloc[i][0]] = 'down'

    test_ylabel = {}
    for i in range(test_y.shape[0]):
        if test_y.iloc[i][1] == 'up':
            test_ylabel[test_y.iloc[i][0]] = 'up'
        else:
            test_ylabel[test_y.iloc[i][0]] = 'down'

    return train_key, train_ylabel, test_key, test_ylabel

# train_ylabel = []
# for i in range(train_y.shape[0]):
#     if train_y.iloc[i][0] == 'up':
#         train_ylabel.append(1)
#     else:
#         train_ylabel.append(0)
#
# print(train_ylabel)
# np.save('train_ylabel.npy', train_ylabel)
