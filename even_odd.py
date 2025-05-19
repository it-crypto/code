# It will check whether the number is positive, negative or zero
# It also checks if its even or odd.
# Using try/except block to check if its number or not - otherwise throwing a exception - Value Error
# Using f string to print the contents of the variables.

def even_odd(n):
    if n > 0:
        value = "positive"
    elif n < 0:
        value = "negative"
    else:
        value = "zero"
    
    if n % 2 == 0:
        print(f"The number {n} is even and {value}")
    else:
        print(f"The number {n} is odd and {value}")
    
def main():
    try:
         n = int(input("Enter a number: "))
         even_odd(n)
    except ValueError:
        print("Please enter a valid integer")
   
main()
