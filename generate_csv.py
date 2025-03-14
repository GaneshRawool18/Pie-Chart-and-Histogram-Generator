import pandas as pd

# Sample data
data = {
    "Category": ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O"],
    "Values": [20, 30, 50, 100, 200, 300, 400, 10, 20, 15, 25, 35, 45, 55, 65]
}

# Create DataFrame
df = pd.DataFrame(data)

# Save to CSV
df.to_csv("sample_data.csv", index=False)

print("CSV file 'sample_data.csv' created successfully!")
