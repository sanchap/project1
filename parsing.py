import argparse

parser = argparse.ArgumentParser(description="Calculator")
parser.add_argument("num1", type = int, help="First number")
parser.add_argument("num2", type = int, help="Second number")
parser.add_argument("operation", type = str, help = "operation")

arg_group = parser.add_mutually_exclusive_group()
arg_group.add_argument("-v,", "--verbose", action="store_true", help="use text to show answer")
args = parser.parse_args()

num1=args.num1
num2=args.num2

def solved_number():
    if args.operation == "addition":
        value=num1+num2

    elif args.operation == "subtraction":
        value=num1-num2

    elif args.operation == "multiplication":
        value=num1*num2

    elif args.operation == "division":
        value=num1/num2

    return value

def solve_sign():
    if args.operation == "addition":
        sign="+"

    elif args.operation == "subtraction":
        sign="-"

    elif args.operation == "multiplication":
        sign="x"

    elif args.operation == "division":
        sign="/"

    return sign

if args.verbose==True:
    print(str(num1)+" "+solve_sign()+" "+str(num2)+" = "+str(solved_number()))

else:
    print(solved_number())
