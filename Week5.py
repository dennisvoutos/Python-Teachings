import numpy as np
import time
# NUMPY BASICS

# 1. Understanding the Purpose and Significance of NumPy
# NumPy is the foundation for scientific computing in Python. It provides high-performance, efficient computations
# with large data sets and is crucial for numerical and data analysis tasks.
# print("\n--- Understanding the Purpose of NumPy ---")
# print("NumPy is up to 50x faster than traditional Python lists for numerical data.")

# Example showing time efficiency with NumPy array vs Python list
# size = 1_000_000
# python_list = list(range(size))
# numpy_array = np.arange(size)

# # Perform a simple operation (addition) on both to compare speed
# # %timeit sum(python_list)  # Time for Python list #if you have a jyputer notebook open this works
# # %timeit np.sum(numpy_array)  # Time for NumPy array
# start_time = time.time()
# sum(python_list)  # Time for Python list
# end_time = time.time()
# print(f"Time taken for Python list sum: {end_time - start_time} seconds")

# # # Timing NumPy array sum
# start_time = time.time()
# np.sum(numpy_array)  # Time for NumPy array
# end_time = time.time()
# print(f"Time taken for NumPy array sum: {end_time - start_time:.6f} seconds")

# # 2. Familiarizing with NumPy Array Objects
# print("\n--- Creating NumPy Arrays ---")

# # Creating a NumPy array from a list
# list_data = [1, 2, 3, 4, 5]
# np_array_from_list = np.array(list_data)
# print(f"NumPy array from list: {np_array_from_list}")

# # # Creating an array of zeros, ones, and random numbers
# zeros_array = np.zeros((3, 3))
# ones_array = np.ones((2, 5))
# random_array = np.random.rand(4, 4)

# print(f"Array of zeros:\n{zeros_array}")
# print(f"Array of ones:\n{ones_array}")
# print(f"Array of random numbers:\n{random_array}")

# # Indexing and slicing arrays
# print("\n--- Accessing and Manipulating Elements ---")
# array_1d = np.array([10, 20, 30, 40, 50])
# # print(f"Original array: {array_1d}")

# # # Accessing elements
# # print(f"Element at index 2: {array_1d[2]}")  # Accessing element
# # print(f"Slice from index 1 to 4: {array_1d[1:]}")  # Slicing

# # # Modifying elements
# array_1d[2] = 99
# print(f"Modified array: {array_1d}")


# # 3. Performing Mathematical Operations with NumPy
# print("\n--- Mathematical Operations ---")

# # Creating two arrays
array_a = np.array([1, 2, 3, 4])
array_b = np.array([10, 20, 30, 40])

# # Basic mathematical operations
# print(f"Addition: {array_a + array_b}")
# print(f"Subtraction: {array_a - array_b}")
# print(f"Multiplication: {array_a * array_b}")
# print(f"Division: {array_a / array_b}")

# # Advanced mathematical functions
# angles = np.array([0, np.pi / 2, np.pi])
# print(f"Sine of angles: {np.sin(angles)}")  # Trigonometric function
# print(f"Logarithm of array: {np.log(array_b)}")  # Logarithmic function

# # Element-wise operations and broadcasting
# print("\n--- Element-wise Operations and Broadcasting ---")
# broadcast_array = np.array([1, 2, 3, 4])
# scalar = 10

# # # Broadcast scalar to array
# print(f"Array multiplied by scalar {scalar}: {broadcast_array / scalar}")


# # 4. Analyzing and Manipulating Data using NumPy
# print("\n--- Array Manipulation ---")

# # Reshaping arrays
array_to_reshape = np.arange(1, 13)
reshaped_array = array_to_reshape.reshape(3, 4)
# print(f"Original array:\n{array_to_reshape}")
# print(f"Reshaped to 3x4:\n{reshaped_array}")

# # Slicing and indexing
# print("\nSlicing a 2D array:")
# print(f"First row: {reshaped_array[0, :]}")
# print(f"Element at [2,3]: {reshaped_array[2, 3]}")

# # Handling missing data using NaN (Not a Number)
data_with_nan = np.array([1, 2, np.nan, 4, 5])
# print(f"Array with missing data: {data_with_nan}")
# print(f"Is NaN in array: {np.isnan(data_with_nan)}")

# # Replacing NaN with the mean of the array
clean_data = np.where(np.isnan(data_with_nan), np.nanmean(data_with_nan), data_with_nan)
print(f"Data after replacing NaN with mean: {clean_data}")

# # Aggregation and summary statistics
array_stats = np.array([[1, 2, 3], [4, 5, 6]])
# print(f"Sum: {np.sum(array_stats)}")
# print(f"Mean: {np.mean(array_stats)}")
# print(f"Max: {np.max(array_stats)}")
# print(f"Standard Deviation: {np.std(array_stats)}")


# # 5. Exploring Advanced Features of NumPy
# print("\n--- Advanced Features ---")

# # Broadcasting example - Arrays with different shapes
# array_x = np.array([[1, 2, 3], [4, 5, 6]])
# array_y = np.array([1, 2, 3])
# # print(f"Array X:\n{array_x}")
# # print(f"Array Y:\n{array_y}")

# # # Broadcasting Y to X
# broadcast_result = array_x + array_y
# print(f"Result of broadcasting:\n{broadcast_result}")

# # Universal functions (ufunc) - Efficient element-wise operations
# print("\nUniversal Functions (ufunc):")
# array_numbers = np.array([1, 2, 3, 4, 5,-1])
# print(f"Square root of the array: {np.sqrt(array_numbers)}")

# # Linear algebra - matrix multiplication
# matrix_a = np.array([[1, 2], [3, 4]])
# matrix_b = np.array([[5, 6], [7, 8]])
# matrix_product = np.dot(matrix_a, matrix_b)
# print(f"\nMatrix A:\n{matrix_a}")
# print(f"Matrix B:\n{matrix_b}")
# print(f"Matrix multiplication result:\n{matrix_product}")

# # Random number generation
# print("\nRandom Numbers:")
# random_integers = np.random.randint(1, 100, 10)
# print(f"Random integers: {random_integers}")

# # Fourier analysis (Discrete Fourier Transform)
# time = np.linspace(0, 2 * np.pi, 100)
# signal = np.sin(time)
# fourier = np.fft.fft(signal)
# print(f"Fourier transform of the signal:\n{fourier}")
