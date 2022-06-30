def check_input(input):
    try:
        return input
    except ValueError as err:    
        print(err)
        