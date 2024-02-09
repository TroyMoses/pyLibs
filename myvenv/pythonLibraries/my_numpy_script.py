# Numpy is a python library used for working with arrays.
# Provides an array object that is up to 50x faster than traditional python lists.
# The array object is called ndarray.

# Arrays are frequently used in data science and machine learning, where speed and resources are very important.
# Data science is a branch of computer science where we study how to store, use and analyze data for deriving information from it.

# Numpy arrays are stored at one continuous place in memory unlike lists, so proccesses can access and manipulate them very 
# efficiently.
# This behaviour is called locality of reference in computer science.
# Also it is optimized to work with latest CPU architectures.

# Numpy is written in partially python, but most of the parts that require fast computation are written in C or C++.

import numpy as np

arr = np.array([1, 2, 3, 4], ndmin=5)

print(arr)