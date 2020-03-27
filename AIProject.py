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
person1=input("Enter the name of persons to find relation between them.\nName of first person : ")
person2=input("Name of second person : ")
def grandparent(x,y):
    temp=var()
    result = conde((parent(x,temp),parent(temp,y)))
    return result
def sibling(x,y):
    temp=var()
    result = conde((parent(temp,x),parent(temp,y)))
    return result
def uncle(x,y):
    temp=var()
    temp1=var()
    result = conde((parent(temp,x),parent(temp,temp1),parent(temp1,y)))
    return result
def cousin(x,y):
    temp=var()
    temp1=var()
    temp2=var()
    result = conde((parent(temp1,x),parent(temp,temp1),parent(temp,temp2),parent(temp2,y)))
    return result
rel_par_1=run(1,x,parent(x,person1))
rel_par_2=run(1,x,parent(person2,x))
rel_par_3=run(1,x,parent(person1,x))
rel_par_4=run(1,x,parent(x,person2))
if rel_par_1==(person2,) or rel_par_2==(person1,):
    print(person2+" is parent of "+person1+" or "+person1+" is son of "+person2)
elif rel_par_3==(person2,) or rel_par_4==(person1,):
    print(person2+" is son of "+person1+" or "+person1+" is parent of "+person2)