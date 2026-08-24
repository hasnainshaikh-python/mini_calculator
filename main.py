def add(a:float,b:float):
    return a+b

def subtract(a:float,b:float):
    return a - b

def multiply(a:float,b:float):
    return a * b

def divide(a:float,b:float):
    if b == 0:
        raise ZeroDivisionError("Cannot divide by zero.")
    return a / b

history = []

operations = {
       "+": add,
        "1": add,
        "-": subtract,
        "2": subtract,
        "*": multiply,
        "3": multiply,
        "/": divide,
        "4": divide }

print(" LOADING SIMPLE CALCULATOR")

while True:
    user_input = input("enter operators +,-,*,/ or 1,2,3,4 | exit for quitting | history for checking history : ").strip().lower()

    if user_input == "exit":
        print("Exiting the calculator")
        break

    if user_input == "history":
        if not history:
            print("there is no history yet\n")
        else:
            print("\n--- Calculation History ---")
            for entry in history[-5:]:
                print(entry)
            print("---------------------------\n")
        continue

    if user_input == "delete history":
        history.clear()
        break
    
    if(user_input not in operations):
        print("Enter valid operators like +,-,*,/ or 1,2,3,4 | exit for quitting")
        continue

    


    try:
        num1 = float(input("enter your first number: "))
        num2 = float(input("enter your second number: "))

        operation_func = operations[user_input]
        result = operation_func(num1, num2)

        record = f"{num1} {user_input} {num2} = {result}\n"
        history.append(record)
        print(f"Result: {record}\n")

    except ValueError:
            print("Error: Invalid input. Please enter valid numerical values.\n")
    except ZeroDivisionError as e:
            print(f"Math Error: {e}\n")


     
