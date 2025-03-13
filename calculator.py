#calculator.py

def add (a,b):
    return a+b

def subtract(a,b):
    return a-b

def multiply(a,b):
    return a*b

def divide(a,b):
    if b==0:
        return "error"
    else:
        return a/b
    
def main():
    n1 = int(input("Enter first number:"))
    n2 = int(input("Enter second number:"))


    print("Addition of two numbers is:", add(n1, n2))
    print("Subtraction of two numbers is:", subtract(n1, n2))
    print("Multiplication of two numbers is:", multiply(n1, n2))
    print("Division of two numbers is:", divide(n1, n2))


def test_calculator():
    assert add(3, 2) == 5
    assert subtract(5, 3) == 2
    assert multiply(4, 2) == 8
    assert divide(6, 2) == 3
    assert divide(5, 0) == "error"

if __name__ == "__main__":
    main()