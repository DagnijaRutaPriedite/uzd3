# CSV
# katra otra elementa summa
with open ("data.csv") as f:
    a=[]
    for line in f:
        row=line.rstrip().split(",")
        l=len(row)
        if l==5:
            if row[1]=="A128100":
                a.append(int(row[4]))
            else:
                pass
katrs_otrais=sum(a[::2]) if a else None
print(katrs_otrais)

#TOP3 videjais rezultats
a.sort(reverse=True) #sakarto sarakstu(visticamak sekojosa dala savadaka)
tris=sum(a[:3]) if len(a)>=3 else None
print(tris)

# videja vertiba
average=round(sum(a)/len(a))
print(average)

# kopeja vertiba
print(len(a))

# noteiktai lietai
data=[]...[]..[].
for row in data:
    vecums=row(1)
    if vecums<25
    print(row)