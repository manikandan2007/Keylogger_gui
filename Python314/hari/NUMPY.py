import numpy as np
def basic_numpy_operations():
    arr=np.array([1,2,3,4,5])
    print("Array :",arr)
    mean_value=np.mean(arr)
    print("Mean :",mean_value)
    sum_value=np.sum(arr)
    print("Sum:",sum_value)
    std_deviation=np.std(arr)
    print("Standard Deviation:",std_deviation)
    squared_values=np.square(arr)
    print("Squared Values:",squared_values)

    two_dimensional_arr=np.array([[1,2,3],[4,5,6]])
    print("2D Array:")
    print(two_dimensional_arr)
    transposed_arr=np.transpose(two_dimensional_arr)
    print("Transposed 2D Array:")
    print(transposed_arr)

if __name__=="__main__":
    basic_numpy_operations()
    
