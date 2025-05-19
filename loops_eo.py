'''
1. Lists:
Mutable (can be changed after creation).

Typically used to store multiple items of any data type.

Can store single values or multiple values like numbers, strings, other lists, etc.

You add/remove items from a list using methods like .append(), .remove(), etc.


2. Tuples:
Immutable (cannot be changed after creation).

Also used to store multiple values (just like a list).

Used when you want to ensure the data cannot be modified (for example, in cases where integrity of data is important).

You can access and read the values, but you cannot modify them (i.e., no .append() or .remove()).

List: Mutable, allows modification. Use when you might change the contents later.

Tuple: Immutable, cannot be modified after creation. Use when you don’t need to modify the values, and you want to keep the data protected.

Use a tuple when you want to group related values together and you don’t need to modify them.

Example: Returning related information from a function, like status codes, coordinates, etc.

Use a list if you need to store multiple items that might change or need to be updated later. (e.g., adding/removing items, which you don’t do in this case).
'''


def even_odd(n):
    if n > 0:
        value = "positive"
    elif n < 0:
        value = "negative"
    else:
        value = "zero"
    
    if n % 2 == 0:
        val = "even"
    else:
        val = "odd"
        
    return value, val  

def main():
    num = []
    while True:
        n = input("Enter a number (or 'stop' to finish): ")
        if n.lower() == 'stop':  # Make case-insensitive check for 'stop'
            break
        try:
            num.append(int(n))
        except:
            print("Please enter a valid number.")  # Handle invalid input
            
    print(num)
    
    results = []
    for i in num:
        pnz, eo = even_odd(i)
        results.append((pnz,eo))  # packing them as tuple as there is no modification required.
        print(f"The number {i} is {pnz} and {eo}")
        
    print("All results")
    for num in results:
        print(num)
        
main()

