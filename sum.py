"""
This module defines a function to find the sum of elements in an array.
"""
# We create a function to calculate the values in an array
def find_sum(array):
    """
    Function calcilate the sum of elements inside the function
    """
    sumo = 0
    for i in array:
        sumo += i
    return sumo

# Create a sample array for testing the function created
arr = [3,7,1,9,3,9]
print(find_sum(arr))
