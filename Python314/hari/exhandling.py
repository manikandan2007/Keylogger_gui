def division_example(a,b):
    try:
        result=a/b
        print(f"Result of division:{result}")
    except ZeroDivisionError:
        print("Error: Division by zero is not allowed")
    except TypeError as e:
        print(f"Error:{e}")
    except Exception as e:
        print(f"An unexpected error occured:{e}")
    else:
        print("Division Operation executed successfully.")
    finally:
        print("This block always gets executed, regardless of exception.")

if __name__=="__main__":
    try:
        division_example(10,0)
        division_example(10,"2")
        my_list=[1,2,3]
        print(my_list[5])
    except IndexError:
        print("Error:Index out of range.")
