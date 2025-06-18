import pandas as pd
import os

# Path to the input CSV file
input_file = 'data/raw/creditcard.csv'
output_dir = 'data/raw'

# Ensure output directory exists
os.makedirs(output_dir, exist_ok=True)

# Read the CSV file
df = pd.read_csv(input_file)

# Calculate number of rows per part (4 equal parts)
total_rows = len(df)
rows_per_part = total_rows // 4 + (1 if total_rows % 4 else 0)  # Ceiling division

# Split into four parts
part1 = df.iloc[:rows_per_part]
part2 = df.iloc[rows_per_part:2*rows_per_part]
part3 = df.iloc[2*rows_per_part:3*rows_per_part]
part4 = df.iloc[3*rows_per_part:]

# Save the parts with headers
part1.to_csv(os.path.join(output_dir, 'creditcard_part1.csv'), index=False)
part2.to_csv(os.path.join(output_dir, 'creditcard_part2.csv'), index=False)
part3.to_csv(os.path.join(output_dir, 'creditcard_part3.csv'), index=False)
part4.to_csv(os.path.join(output_dir, 'creditcard_part4.csv'), index=False)

# Print file sizes to verify
print(f"Part 1 size: {os.path.getsize(os.path.join(output_dir, 'creditcard_part1.csv')) / (1024*1024):.2f} MB")
print(f"Part 2 size: {os.path.getsize(os.path.join(output_dir, 'creditcard_part2.csv')) / (1024*1024):.2f} MB")
print(f"Part 3 size: {os.path.getsize(os.path.join(output_dir, 'creditcard_part3.csv')) / (1024*1024):.2f} MB")
print(f"Part 4 size: {os.path.getsize(os.path.join(output_dir, 'creditcard_part4.csv')) / (1024*1024):.2f} MB")