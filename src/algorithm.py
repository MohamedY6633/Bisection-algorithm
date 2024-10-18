import Fx_parsing as fx

def bisection(mutivalue, a, b, eqn, epsilon=0.0001, i=0):

    if mutivalue >= 0:
        print("Error: The product of f(a) and f(b) must be negative.")
        return None
    
    c0 = 0

    while True:
        c = 0.5 * (a + b)  
        print(f"Evaluating c = {c:.4f} with equation result {fx.evaluate_equation_calc_c(c, eqn):.4f}")


        if abs(c - c0) < epsilon:
            print(f"Converged to root: {c:0.4f}" )
            return c

        if fx.evaluate_equation_calc_c(c, eqn) == 0:
            print("This is iteration no.", i + 1)
            print(f"The Root is: {c:0.4f}")
            return c
        

        if fx.evaluate_equation_calc_c(c, eqn) < 0:
            c0 = c
            a = c
        else:
            c0 = c
            b = c

        i += 1
        print(f"This is iteration no. {i} and C = {c:.4f}")
        print("The Number Of iteration Now is : ", i  )
