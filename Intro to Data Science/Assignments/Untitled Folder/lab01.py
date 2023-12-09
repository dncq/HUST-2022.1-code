import pandas as pd

# Load your data into a DataFrame (replace 'data.csv' with your data file)
data = pd.read_csv(r'C:\python code\Intro to Data Science\Untitled Folder\Players.csv')

# Calculate passes per minute
data['PassesPerMinute'] = data['Passes'] / data['Minutes']

# Create categories based on passes per minute
data['PassCategory'] = pd.cut(data['PassesPerMinute'], [0, 0.25, 0.5, float('inf')], labels=['<= 0.25', '0.25 - 0.5', '>= 0.5'])

# Calculate the relative percentage for each category
pass_percentage = data['PassCategory'].value_counts(normalize=True) * 100

print(pass_percentage)
