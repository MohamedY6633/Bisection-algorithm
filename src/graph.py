import numpy as np
import matplotlib.pyplot as plt 
import Fx_parsing as fx
def drawplot(x1, x2, function_input):
    x = np.linspace(float(x1), float(x2), 100)  
    y = [fx.evaluate_equation(function_input, val) for val in x]  
    plt.plot(x, y)
    plt.title(f"Plot of {function_input}")
    plt.xlabel('x')
    plt.ylabel('f(x)')
    plt.grid()
    plt.show()