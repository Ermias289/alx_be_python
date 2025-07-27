def perform_operation (num1, num2, operation):
    try:
        if operation == 'add':
            result = num1 + num2
        elif operation == 'subtract':
            result = num1 - num2
        elif operation == 'multiply':
            result = num1 * num2
        elif operation == 'divide':
            if num2 == 0:
                return "Error: Division by zero is not allowed."
            result = num1 / num2
        else:
            return "Error: Invalid operation."

        return result
    except ValueError:
        return "Error: Please enter valid numbers."