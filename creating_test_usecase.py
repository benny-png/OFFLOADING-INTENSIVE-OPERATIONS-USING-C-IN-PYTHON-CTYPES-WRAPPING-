import csv

filename = 'large_file.csv'
num_lines = 1000000  # Adjust the number of lines as needed

with open(filename, mode='w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['Column1', 'Column2', 'Column3'])  # Header
    for i in range(num_lines):
        writer.writerow([f'Data1_{i}', f'Data2_{i}', f'Data3_{i}'])
