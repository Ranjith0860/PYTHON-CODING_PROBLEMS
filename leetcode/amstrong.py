# .print amstrong number

# what is amstrong ==>num=153 1+5+3=9 1**9+5**9+3**9=153 is know as amstrong 


num=(input("enyer number: "))


powr=len(num)
sum1=0

print(powr)

for i in num:
    sum1=sum1+int(i)**powr
print(sum1)

if int(num)==sum1:
    print(f"{num} is an amstrong number")
else:
    print(f"{num} not an amstrong number")





