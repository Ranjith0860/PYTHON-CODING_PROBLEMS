str1="ranjith"
str2="kkkk"

dictt=dict()
anagram=True
for i in str1:
    if i in dictt:
        dictt[i]+=1
    else:
        dictt[i]=1
for i in str2:
        if i in dictt:
             dictt[i]-=1
        else:
            print("not an anagram")
            anagram=False
            break
if anagram:
    for i in dictt.values():
            if i!=0:
                print("false")
                break
    else:
        print("true")