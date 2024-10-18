import Fx_parsing as fx
import graph as g
import algorithm 
function_input = input("Enter the equation to plot (in terms of x): \n ")
x1 = input("Enter the First Boundary: \n")
x2 = input("Enter the Second Boundary: \n")
x1_float = float(x1)
x2_float = float(x2)
multiplication_value = fx.evaluate_equation_calc(function_input,x1,x2)
algorithm.bisection(multiplication_value,x1_float,x2_float,function_input)
print("Credits : Mohamed Yahia Zakaria ID: 23010071") 
g.drawplot(x1_float, x2_float, function_input)
 