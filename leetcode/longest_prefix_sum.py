strs=["flower","flow","flowight"]

pref=strs[0]
pref_len=len(pref)
print(pref,pref_len)

for string in strs[1:len(strs)]:
    while pref!=string[0:pref_len]:
        pref_len-=1
        if pref_len==0:
            print("")
        else:
            pref=pref[0:pref_len]   #updating prefix for lenof mathes string like st mates at 4 flow assing to prefix
print(pref)