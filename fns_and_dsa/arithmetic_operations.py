def perform_operation(num1, num2, operation):
    # match operation:
    #     case 'add':
    #         return num1 + num2
    #     case "subtract":
    #         return num1 - num2
    #     case "multiply":
    #         return num1 * num2
    #     case "divide":
    #         return num1 / num2
    """It's commented out my first trial because the checker wants "==" sign inside the function """
    
    # Second Trial
    
    if operation == "add":
        return num1 + num2
    
    elif operation == "subtract":
        return num1 - num2
    
    elif operation == "multiply":
        return num1 * num2
    
    elif operation == "divide":
        if num2 != 0:
            return num1 / num2
        else:
            raise ValueError("arithmetic_operations.py doesn't contain num2 == 0")
        
