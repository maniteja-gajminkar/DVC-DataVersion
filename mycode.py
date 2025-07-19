import pandas as pd
import os

# Create a simple dataframe with column names
data = {
    'Name': ['Alice', 'Bob', 'Charlie'], 
    'Age': [25, 30, 35],
    'city': ['Newyork', 'Los Angeles', 'Chicago']
}

df = pd.DataFrame(data)

# Adding new row
#new_row_loc2 = {'Name': 'V3', 'Age': 30, 'city': 'city1'}
#df.loc[len(df.index)] = new_row_loc2

# Ensure data directory exists at root level
data_dir = 'data'
os.makedirs(data_dir, exist_ok=True)  # This line ensures the directory exists

file_path = os.path.join(data_dir, 'sample_data.csv')

# Save the DataFrame to a CSV including column names
df.to_csv(file_path, index=False)

print(f"CSV file saved to {file_path}")
