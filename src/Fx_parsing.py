import sympy as sp
import sympy as sp
def evaluate_equation(eqn_str, x):
    x_sym = sp.symbols('x')
    try:
        eqn = sp.sympify(eqn_str)
    except (sp.SympifyError, ValueError):
        print("Invalid equation. Please enter a valid mathematical expression.")
        return None

    try:
        result = eqn.evalf(subs={x_sym: float(x)})  # Evaluate the function at x
    except Exception as e:
        print(f"Error evaluating equation: {e}")
        return None
    
    return result

def evaluate_equation_calc(eqn_str,X1 , X2):
    x = sp.symbols('x')
    eqn = sp.sympify(eqn_str)
    X1 = float(X1)
    X2 = float(X2)
    result1 = eqn.subs(x, X1)
    result2 = eqn.subs(x, X2)
    print("F(", X1 , ") =" ,result1)
    print("F(", X2 , ") =" ,result2)
    return result1*result2

def evaluate_equation_calc_c(X1,eqn_str):
    x = sp.symbols('x')
    eqn = sp.sympify(eqn_str)
    X1 = float(X1)
    result1 = eqn.subs(x, X1)
    return result1


