#try,except errors
try:      
    a,b=list(map(int,input("enter a,b : ").split(",")))
    z=a//b
    print(z)

    if a<b:
        print(f"a should be greater than b you have enterd a= {a},b={b}")
    if b==0 or a <0:
        print(f"the b should be greater than zero{b}")
except ValueError:
     print(f"please enter a integer seperatedby comma")
except ZeroDivisionError:
    print("zero division error")



