try:
    a, b = map(int, input("Enter a,b (comma separated): ").split(","))
    
    if b == 0:
        print("Error: b should not be zero")

    elif  a < b:
         print(f"Warning: a should be greater than b (you entered a={a}, b={b})")
    
    elif a < 0:
            print(f"Warning: a or b should not be negative (you entered a={a}) b= {b}")
    else:
        z = int(a //b)
        print(f"Result of Α ~➗ b ➡️    {z}")
        
       

except ValueError:
    print("Error: Please enter two integers separated by a and b")
except ZeroDivisionError:
    print("Error: Division by zero is not allowed")