# Завдання 1
import pandas as pd

data = {
    'Product': ['Laptop', 'Smartphone', 'Tablet'],
    'Price': [1200, 800, 400],
    'Stock': [50, 150, 200]
}
df = pd.DataFrame(data)

new_df = pd.DataFrame([{'Product': 'USB Hub', 'Price': 40, 'Stock': 150, 'Warranty': '2 years'}])

df = pd.concat([df, new_df], ignore_index = True)

print(df)

# Завдання 2
import pandas as pd

data = {
    'Product': ['Laptop', 'Smartphone', 'Tablet'],
    'Price': [1200, 800, 400],
    'Stock': [50, 150, 200]
}
df = pd.DataFrame(data)

new_df = pd.DataFrame([{'Product': 'USB Hub', 'Price': 'Forty', 'Stock': 150}])

df = pd.concat([df, new_df], ignore_index = True)

print(df)
print(df.dtypes)

# Результат:

#       Product  Price  Stock
# 0      Laptop   1200     50
# 1  Smartphone    800    150
# 2      Tablet    400    200
# 3     USB Hub  Forty    150

# Product       str
# Price      object <- зміна типу стовпця Price з int64 на object. Після чого будь-які математичні функції викликатимуть помилку.
# Stock       int64
# dtype: object

# Завдання 3

import pandas as pd

df = pd.read_csv('customer_feedback.csv')

grouped = df.groupby(['Region', 'Month'])

average_rating = grouped['Rating'].mean()

tabled_df = average_rating.unstack(level = 'Month')

result = tabled_df.fillna(df['Rating'].mean())

print(result)
