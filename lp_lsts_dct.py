'''
Concept	
Input + validation	
Loops	
Functions	
Return values (tuple)	
List handling	
Dictionaries	
Float vs int handling	
Counting/classifying	
Code structure/logical flow
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
    num = [] # lists to store 
    results_dict = {}
    while True:
        n = input("Enter a number (or 'stop' to finish): ")
        if n.lower() == 'stop':  # Make case-insensitive check for 'stop'
            break
        try:
            num.append(float(n))
        except ValueError:
            print("Please enter a valid number.")  # Handle invalid input
            
    print(num)
    num_len = len(num)
    count_even=count_odd=count_pos=count_neg=count_zero = 0
    for i in num:
        if i.is_integer():
            pnz, eo = even_odd(i)
            if eo == 'even':
                count_even +=1 
            else:
                count_odd +=1
            if pnz == 'positive':
                count_pos +=1
            elif pnz == 'negative':
                count_neg +=1
            else:
                count_zero +=1
        
            print(f"The number {i} is {eo} and {pnz}")
            results_dict[i] = [pnz, eo]  # makes it match the float case
        else:
            # For non-integers, we skip even/odd but still evaluate sign
            if i > 0:
                pnz = "positive"
                count_pos += 1
            elif i < 0:
                pnz = "negative"
                count_neg += 1
            else:
                pnz = "zero"
                count_zero += 1

            results_dict[i] = [pnz, "not applicable"]
            print(f"The number {i} is not applicable for even/odd and {pnz}")
            
        
    print(f"You entered {num_len} numbers")
    print(f"Even: {count_even}, Odd: {count_odd}")
    print(f"Positive: {count_pos}, Negative: {count_neg}, Zero: {count_zero}")
    
    print("\n Classifications: ")
    for k,v in results_dict.items():
        print(f"{k}:{v}")
        
    
main()
