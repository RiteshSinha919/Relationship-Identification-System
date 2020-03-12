from logpy import *
parent=Relation()
x=var()
y=var()
l=[]
numOfRelation = int(input("How many Parent Child Relation do you want to enter : "))
for a in range(1,numOfRelation+1):
    par=input("Enter the name of "+str(a)+" parent ")
    child=input("Enter the name of "+str(a)+" child ")
    l.append((par,child))
print(l)
for b in range(0,numOfRelation):
    facts(parent,l[b])
print(run(2,x,parent(x,'bob')))