from art import logo


def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1- n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1 / n2

# check if variable is valid amount
def is_valid_amount(variable):
    try:
        int_value = float(variable)
        return True
    except ValueError:
        return False

operations = {
    '+' : add,
    '-' : subtract,
    '*' : multiply,
    '/' : divide
}

# get valid number inputs
def get_number_input(prompt):
    is_valid = False
    while not is_valid:
        num = input(prompt)

        if is_valid_amount(num):
            is_valid = True
            return float(num)
        else:
            print("Invalid input. Please provide a valid number.")    

# get valid operation
def get_operation_input(operations):
    is_valid = False
    while not is_valid:
        operation = input("Choose an operation: ")
        if operation in operations:
            is_valid = True
            return operation
        else:
            print("Invalid input. Please provide a valid operation.") 

# calculate
def calculate():

    print(logo)

    num1 = get_number_input("What's the first number?: ")
    for operation in operations:
        print(operation)
    
    to_continue = True
    while to_continue:

        operation = get_operation_input(operations)

        num2 = get_number_input("What's the next number?: ")

        result = operations[operation](num1, num2)

        print(f"{num1} {operation} {num2} = {result}")
        print()

        
        while True:

            user_decision = input(f"Type 'y' to continue calculating with {result}, or type 'n' to start a new calculation or type 'q' to quit program ").lower()

            if user_decision not in ['y', 'n' , 'q']:
                print("Invalid input.")
            else:
                break
        
        if user_decision == 'y':
            num1 = result
        elif user_decision == 'n':
            to_continue = False
            calculate()
        else:
            to_continue = False
            print("Program terminated.")

# perform calculate operation
calculate()