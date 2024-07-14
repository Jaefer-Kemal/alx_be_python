# robust_division_calculator.py

def safe_divide(numerator, denominator):
    try:
        num = float(numerator)
        deno = float(denominator)
        
        if deno == 0:
            return "Error: Cannot divide by zero."
        
        return f"The result of the division is {num / deno}"
    
    except ValueError:
        return "Error: Please enter numeric values only."
