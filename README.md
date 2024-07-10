
---

# File Parsing (or similar Intensive I/O, computational Operations) Offloading Usecase Exploration

![INPUT BENCHMARK PNG](https://github.com/benny-png/OFFLOADING-INTENSIVE-OPERATIONS-USING-C-IN-PYTHON-CTYPES-WRAPPING-/blob/main/benchmark2.png)

This project demonstrates how to optimize file parsing tasks by offloading them to C from Python using a DLL (Dynamic Link Library). It includes benchmarks comparing the performance of a C function and a pure Python implementation for parsing a large CSV file.

## Project Overview

### Purpose

The purpose of this project is to showcase the performance benefits of using C for computationally intensive and memory usage tasks like file parsing, especially when dealing with large datasets, Numerical Computations and Data Processing, Algorithmic Implementations, Image and Signal Processing, Cryptography and Security, Machine Learning and AI, File and I/O Operations, Network Operations and any tested use case.

### Benchmark Results

- **C Function Time:** 92.4 seconds
- **Python Function Time:** 193.36 seconds

The C function demonstrates significantly faster performance compared to the pure Python implementation.

### How to Use

#### Requirements

- Microsoft Visual Studio (for creating the DLL)
- Python 3.x (for running the benchmarks and scripts)

#### Steps to Reproduce

1. **Creating the DLL using Microsoft Visual Studio:**

![INPUT BENCHMARK PNG](https://github.com/benny-png/OFFLOADING-INTENSIVE-OPERATIONS-USING-C-IN-PYTHON-CTYPES-WRAPPING-/blob/main/dll_Ms_visualstudio.png)

   - Open Microsoft Visual Studio.
   - Create a new "Empty Project" (or any appropriate project type).
   - Add a new C file (`parser_lib.c`) containing the C code for file parsing.
   - Compile the project to generate the DLL (`parser_lib.dll`).

2. **Python Setup and Benchmarking:**

   - Ensure Python is installed and configured on your system.
   - Run the provided Python script (`benchmark.py`) to benchmark both the C and Python functions for file parsing.

3. **Plotting Benchmark Results:**

   - The script generates a bar chart (`benchmark.png`) showing the comparative execution times of the C and Python implementations.

   ![INPUT BENCHMARK PNG](https://github.com/benny-png/OFFLOADING-INTENSIVE-OPERATIONS-USING-C-IN-PYTHON-CTYPES-WRAPPING-/blob/main/benchmark2.png)

#### Notes on Third-Party C Libraries

- If integrating third-party C libraries (e.g., libcurl for network operations), ensure they are correctly linked with the DLL (`parser_lib.dll`).
- Use tools like `vcpkg` to simplify the integration process within Microsoft Visual Studio, especially for managing dependencies like libcurl.

#### Example Benchmarking (Optional)

- Additional code snippets (`benchmark_curl_requests.py`) are provided for benchmarking the performance difference between using libcurl (via C) and Python's `requests` library for web requests.

#### Conclusion

This project highlights the advantages of leveraging C's performance optimizations through Python wrappers, particularly beneficial for tasks involving heavy computation or large data processing.

---
