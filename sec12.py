'''
pandas : "Python Data Analysis"
'''

import pandas as pd



df = pd.read_excel('output.xlsx')
df.set_index('종목명', inplace=True)  # 종목명 컬럼을 인덱스로 지정함
df.drop('N', axis=1, inplace=True)  # 'N' 컬럼을 삭제함
print(df)