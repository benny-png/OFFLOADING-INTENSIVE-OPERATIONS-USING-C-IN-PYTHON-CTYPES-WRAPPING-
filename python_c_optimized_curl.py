import ctypes
import time
import requests
import matplotlib.pyplot as plt

# Path to the DLL
dll_path = r"C:\Users\User\Python_C_WRAPPED\dll_resources\optmizer.dll"  # Adjust path if necessary

# Load the DLL
simple_function = ctypes.CDLL(dll_path)

# Define the argument and return types of the check_file_exists function
simple_function.check_file_exists.argtypes = (ctypes.c_char_p,)
simple_function.check_file_exists.restype = ctypes.c_int

# Function to benchmark C wrapped function
def benchmark_c_wrapped(url, iterations=100):
    start_time = time.time()
    for _ in range(iterations):
        result = simple_function.check_file_exists(url.encode('utf-8'))
    end_time = time.time()
    return end_time - start_time

# Function to benchmark Python requests
def benchmark_python_requests(url, iterations=100):
    start_time = time.time()
    for _ in range(iterations):
        response = requests.get(url)
    end_time = time.time()
    return end_time - start_time

# URLs to test
url = "http://wolfprojects.altervista.org/articles/dll-in-c-for-python/"

# Number of iterations for benchmarking
iterations = 1000

# Perform benchmarking
c_wrapped_time = benchmark_c_wrapped(url, iterations)
python_requests_time = benchmark_python_requests(url, iterations)

print(f"C Wrapped function time: {c_wrapped_time} seconds")
print(f"Python requests function time: {python_requests_time} seconds")

# Plot the results
methods = ['C Wrapped', 'Python Requests']
times = [c_wrapped_time, python_requests_time]

plt.bar(methods, times, color=['blue', 'orange'])
plt.ylabel('Time (seconds)')
plt.title(f'Benchmarking: {iterations} Iterations')
plt.show()
