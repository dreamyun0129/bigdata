import pandas as pd
df1 = pd.DataFrame(pd.read_excel('train.xlsx', sheet_name='forum_up'))
df2 = pd.DataFrame(pd.read_excel('train.xlsx', sheet_name='news_up'))
df3 = pd.DataFrame(pd.read_excel('train.xlsx', sheet_name='forum_down'))
df4 = pd.DataFrame(pd.read_excel('train.xlsx', sheet_name='news_down'))
all_df = pd.concat([df1, df2, df3, df4], sort=False)
all_df.to_excel("all.xlsx")

test_df1 = pd.DataFrame(pd.read_excel('test.xlsx', sheet_name='forum_up'))
test_df2 = pd.DataFrame(pd.read_excel('test.xlsx', sheet_name='news_up'))
test_df3 = pd.DataFrame(pd.read_excel('test.xlsx', sheet_name='forum_down'))
test_df4 = pd.DataFrame(pd.read_excel('test.xlsx', sheet_name='news_down'))
all_test_df = pd.concat([test_df1, test_df2, test_df3, test_df4], sort=False)
all_test_df.to_excel("test_all.xlsx")