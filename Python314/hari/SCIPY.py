import numpy as np
from scipy import optimize
def scipy_example():
    def objective_function(x):
        return x**2+2*x+1
    initial_guess=0
    result=optimize.minimize(objective_function,initial_guess)
    optimal_x=result.x[0]
    optimal_value=result.fun
    print(f"Optimal X:{optimal_x}")
    print(f"Optimal Value:{optimal_value}")

if __name__=="__main__":
    scipy_example()
