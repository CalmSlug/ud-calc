import re


def perform_math():
    print("Absolutely Magical Calculator")
    print("Type 'exit' to quit\n")
    previous = "1st time"

    while True:
        if previous == "1st time":
            equation = input("Enter equation: ")
            
            if equation == 'exit':
                print("Goodbye, human!")
                break
            
            equation = re.sub('[a-zA-Z]', '', equation)
            previous = eval(equation)
        
        else:
            equation = input(str(previous))
            
            if equation == 'exit':
                print("Goodbye, human!")
                break
            
            equation = re.sub('[a-zA-Z]', '', equation)
            previous = eval(str(previous) + equation)


perform_math()
