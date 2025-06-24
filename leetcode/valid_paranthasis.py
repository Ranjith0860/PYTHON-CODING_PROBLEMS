

s=""
stack=[]
for i in s:
    if stack=="":
        print("empty")
    if i in '([{':
        stack.append(i)
    else:
        if not  stack or\
        (i==')'and stack[-1]!='(')or\
        (i==']' and stack[-1]!='[')or\
        (i=='}' and stack[-1]!='{'):
            print(False) 
        stack.pop()
print(not stack) 