import pandas as pd
import matplotlib.pyplot as plt
data = pd.read_csv("base.csv") # /home/intelqong/Downloads/base.csv
# The file base.csv is modified for better calculation.
numerical_columns = ['Age', 'Class hour (weekly)', 'Sleeping hour (Daily)', 'Study hour (Daily)',
                     'CGPA (Average)', 'Monthly expanses', 'Monthly Income', 'Daily Exercise (Time)',
                     'Screening Time (Daily)', 'Prayer time (Daily)', 'Organizational Activities (Monthly)',
                     'Leisure Time (Daily)', 'Skill Upgraded Time (weekly)']
def create_bar_chart(column_name):
    grouped_data = data.groupby("Gender")[column_name].mean()
    plt.figure(figsize=(10, 6))
    plt.bar(grouped_data.index, grouped_data.values)
    plt.xlabel("Gender")
    plt.ylabel(column_name)
    plt.title(f"Average {column_name} by Gender")
    plt.show()
    plt.close()
for column in numerical_columns:
    create_bar_chart(column)