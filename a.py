temp=input()
temp=temp.split(" ")
p=[]
for i in temp:
    p.append(int(i))
if p[0]+p[1]==p[2]+p[3]:
    print("Balanced")
if p[0]+p[1]<p[2]+p[3]:
    print("Right")
if p[0]+p[1]>p[2]+p[3]:
    print("Left")
