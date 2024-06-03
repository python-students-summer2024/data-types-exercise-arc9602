"""
Practice problems to get the hang of converting among data types.
In this case, we focus on converting numeric data types to strings and vice-versa.
"""


def calculate_profit():
    """
    Imagine this scenario: a company has determined that its annual profit is typically 23 percent of total sales.
    Complete this function so that it asks the user to enter in the projected amount of total sales and then displays the profit that will be made from that amount.
    You can assume the user will enter only numeric characters, e.g. "3000", not "$3,000.00"
    The output should match the format of the following examples: "Profit: $690.00" for sales of $3,000, or "Profit: $2,300.00" for sales of $10,000, etc.
    """
    sales = float(input("Please enter the number of total annual sales: "))
    print("The estimated annual profit is: $", f"{sales*0.23:,}")


def calculate_quotient_and_remainder():
    """
    Complete this function so that it asks the user to input two integers.
    You program should calculate and output the quotient and remainder when the first number is divided by the second.
    Here's an example run of the function:
      Enter number #1: 5
      Enter number #2: 2
      2 goes into 5 a total of 2 times with a remainder of 1
    """
    x = int(input("Enter first number: "))
    y = int(input("Enter second number: "))
    print(str(y)+" goes in "+str(x)+" a total of "+str(x//y)+" times with a remainder of "+str(x%y))


def calculate_miles_per_gallon():
    """
    A car's Miles Per Gallon (MPG) can be calculated using the following formula:
      MPG = Miles driven / Gallons of Gas Used
    Complete this function so that it asks the user for the number of miles driven and the gallons of gas used.
    It should calculate the car's MPG and display the result in the format indicated in this example run of the program:

      Miles driven: 100
      Gas used (gallons): 25
      Miles per gallon: 2.2 #what? how is this 2.2?
    """
    miles = float(input("Enter number of miles driven: "))
    gal = float(input("Enter number of gallons of fuel used: "))
    print("Miles driven: "+str(miles))
    print("Gas used (gallons): "+str(gal))
    print("Miles per gallon: "+str(miles/gal))




def align_text():
    """
    Complete this function such that it asks the user to enter in 3 price values (as floating point numbers).
    The print out the price values so that they are formatted to two decimal places. Also make sure that the price values are right aligned and line up at the decimal point.
    Here's a sample running of the program:

      Enter price #1: 1.55
      Enter price #2: 10
      Enter price #3: 9532.6

      Here are your prices!

      Price #1: $    1.55
      Price #2: $   10.00
      Price #3: $ 9532.60
    """
    p1 = float(input("Enter price #1: "))
    p2 = float(input("Enter price #2: "))
    p3 = float(input("Enter price #3: "))
    p1 = str(round(p1,2))
    p2 = str(round(p2,2))
    p3 = str(round(p3,2))
    print(
    f"{'Price #1:':<12}{p1:>10}",
    f"{'Price #2:':<12}{p2:>10}",
    f"{'Price #3:':<12}{p3:>10}",
    sep="\n"
    )
    print('foo\nbar'[ 4 ])
