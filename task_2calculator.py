import pickle

def get_numbers():
    try:
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))
        return num1, num2
    except ValueError:
        print("Invalid input. Please enter numeric values.")
        return get_numbers()

def get_operation():
    print("Choose an operation:")
    print("1. Addition (+)")
    print("2. Subtraction (-)")
    print("3. Multiplication (*)")
    print("4. Division (/)")
    
    operation = input("Enter the operation (1/2/3/4): ")
    if operation in ['1', '2', '3', '4']:
        return operation
    else:
        print("Invalid operation. Please choose from 1, 2, 3, or 4.")
        return get_operation()

def perform_calculation(num1, num2, operation):
    if operation == '1':
        result = num1 + num2
        operation_str = '+'
    elif operation == '2':
        result = num1 - num2
        operation_str = '-'
    elif operation == '3':
        result = num1 * num2
        operation_str = '*'
    elif operation == '4':
        if num2 == 0:
            return None, "Error: Division by zero."
        result = num1 / num2
        operation_str = '/'
    
    return result, f"{num1} {operation_str} {num2} = {result}"

def save_result(result):
    with open('result.pkl', 'wb') as file:
        pickle.dump(result, file)

def load_result():
    try:
        with open('result.pkl', 'rb') as file:
            return pickle.load(file)
    except FileNotFoundError:
        return "No previous result found."

def main():
    num1, num2 = get_numbers()
    operation = get_operation()
    result, message = perform_calculation(num1, num2, operation)
    
    if result is not None:
        print(message)
        save_result(message)
    else:
        print(message)
    
    previous_result = load_result()
    print(f"Previous result: {previous_result}")

if __name__ == "__main__":
    main()


