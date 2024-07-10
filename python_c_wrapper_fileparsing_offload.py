import ctypes
import time
import os

# Load the shared library
if os.name == 'nt':  # Windows
    parser_lib = ctypes.CDLL('./dll_file_parsing/optmizer.dll')
else:  # Linux/macOS
    parser_lib = ctypes.CDLL('./parser_lib.so')

# Define the function prototype
parser_lib.parse_csv.argtypes = [ctypes.c_char_p]
parser_lib.parse_csv.restype = ctypes.c_int

def parse_csv(filename):
    print("Starting C function benchmark...")
    start_time = time.time()
    result = parser_lib.parse_csv(filename.encode('utf-8'))
    end_time = time.time()
    print("Finished C function benchmark.")
    return end_time - start_time, result

# Pure Python implementation for comparison
def parse_csv_python(filename):
    print("Starting Python function benchmark...")
    start_time = time.time()
    with open(filename, 'r') as file:
        for line in file:
            # Simple example: print each line
            print(line)
            pass  # Remove the print statement for fair benchmarking
    end_time = time.time()
    print("Finished Python function benchmark.")
    return end_time - start_time

# Test and benchmark both implementations
filename = "large_file.csv"  # Ensure you have this file for testing

# Benchmark the C function
c_time, c_result = parse_csv(filename)
print(f"C function time: {c_time} seconds")
print(f"C function result: {'Success' if c_result == 0 else 'Failure'}")

# Benchmark the Python function
python_time = parse_csv_python(filename)
print(f"Python function time: {python_time} seconds")

# Plot the results
import matplotlib.pyplot as plt

methods = ['C Function', 'Python Function']
times = [c_time, python_time]

plt.bar(methods, times, color=['blue', 'orange'])
plt.ylabel('Time (seconds)')
plt.title('File Parsing Benchmark')
plt.show()
