import pandas as pd

#Doc.file csv
df=pd.read_csv('/Users/nguyennhi/baitapPandas/data/FoodPrice_in_Turkey.csv',)
df.head()

#Doc file html
url='https://en.wikipedia.org/wiki/List_of_sovereign_states_and_dependent_territories_in_North_America'
df=pd.read_html(url)
df[0].head()

#Doc file excel
df=pd.read_excel('/Users/nguyennhi/baitapPandas/data/Superstore.xlsx')
df.head()

#Đọc file json
df=pd.read_json('/Users/nguyennhi/baitapPandas/data/data_hanghoa.json')
df.head()