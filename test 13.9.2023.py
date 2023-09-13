file1 = open("objednane_jedla.txt","r")


with open('objednane_jedla.txt') as f:
    text = f.readlines()
    rows = len(text)
print(text)
print("rows: ",rows)

z=0
c=0
m=0
o=0
for i in range(rows):
    current=text[i]
    if current[-2]=="z":
        z+=1
    if current[-2]=="c":
        c+=1
    if current[-2]=="m":
        m+=1
    if current[-2]=="o":
        o+=1
print("z:",z,"c:",c,"m:",m,"o:",o)

if z<20:
    print("z has less than 20 people. The people are:")
    for i in range (rows):
        if text[i][-2]=="z":
            print(text[i][0]+text[i][1]+text[i][2])
if c<20:
    print("c is less than 20. The people are:")
    for i in range (rows):
        if text[i][-2]=="c":
            print(text[i][0]+text[i][1]+text[i][2])
if m<20:
    print("m is less than 20. The people are:")
    for i in range (rows):
        if text[i][-2]=="m":
            print(text[i][0]+text[i][1]+text[i][2])
if o<20:
    print("o is less than 20. The people are:")
    for i in range (rows):
        if text[i][-2]=="o":
            print(text[i][0]+text[i][1]+text[i][2])
