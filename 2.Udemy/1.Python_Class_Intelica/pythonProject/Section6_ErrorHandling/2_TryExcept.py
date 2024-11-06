def do_math():
    user_input = input("Enter a number:")

    try:
        number = float(user_input)        
        print(number)
    except ValueError:
        print("Please enter a valid number!")
        do_math()
    except ZeroDivisionError:
        print("Please do not divide by 0!")
    except Exception as e:
        print("Something went wront!", e)

do_math()