from logpy import *
father=Relation()
mother=Relation()
male=Relation()
female=Relation()
x=var()
y=var()

a=['ned','robert','stanis','railey','ray','john','rob','joffry','zoro','sanji']
b=['cathrine','denarys','lily','cersy','arya','olivia','sansa','kailey','robin']
la1=['ned','robert','stanis','railey','ray']
lb1=['cathrine','denarys','lily','cersy','arya']
la2=['john','rob','joffry','zoro','sanji']
lb2=['olivia','sansa','kailey','robin']
l=[('ray','railey'),('ray','stanis'),('ray','robert'),('ray','ned'),('ned','john'),('ned','rob'),('ned','sansa'),('robert','joffry'),('robert','kailey'),('stanis','robin'),('stanis','olivia'),('railey','zoro'),('railey','sanji'),('arya','railey'),('arya','stanis'),('arya','robert'),('arya','ned'),('cathrine','john'),('cathrine','rob'),('cathrine','sansa'),('cersy','joffry'),('cersy','kailey'),('lily','robin'),('lily','olivia'),('denarys','zoro'),('denarys','sanji')]
print(l)

for i in a:
    fact(male,i)
for j in b:
    fact(female,j)
facts(father,('ray','railey'),('ray','stanis'),('ray','robert'),('ray','ned'),('ned','john'),('ned','rob'),('ned','sansa'),('robert','joffry'),('robert','kailey'),('stanis','robin'),('stanis','olivia'),('railey','zoro'),('railey','sanji'))
facts(mother,('arya','railey'),('arya','stanis'),('arya','robert'),('arya','ned'),('cathrine','john'),('cathrine','rob'),('cathrine','sansa'),('cersy','joffry'),('cersy','kailey'),('lily','robin'),('lily','olivia'),('denarys','zoro'),('denarys','sanji'))

person1=input("Select two names from the above list to find relation between them.\nName of first person : ")
person2=input("Name of second person : ")


#function for grandfather
def grandfather(x,y):
    temp=var()
    result = conde((father(x,temp),father(temp,y),male(x)))
    return result
rela1=run(0,x,grandfather(x,person1))
rela2=run(0,x,grandfather(person2,x))
rela3=run(0,x,grandfather(person1,x))
rela4=run(0,x,grandfather(x,person2))
if rela1==(person2,) or rela2==(person1,):
    print(person2+" is grandfather of "+person1)
elif rela3==(person2,) or rela4==(person1,):
    print(person1+" is grandfather of "+person2)


#function for grandmother
def grandmother(x,y):
    temp=var()
    result = conde((mother(x,temp),father(temp,y),female(x)))
    return result
relb1=run(0,x,grandmother(x,person1))
relb2=run(0,x,grandmother(person2,x))
relb3=run(0,x,grandmother(person1,x))
relb4=run(0,x,grandmother(x,person2))
if relb1==(person2,) or relb2==(person1,):
    print(person2+" is grandmother of "+person1)
elif relb3==(person2,) or relb4==(person1,):
    print(person1+" is grandmother of "+person2)


#function for father
relc1=run(0,x,father(x,person1))
relc2=run(0,x,father(person2,x))
relc3=run(0,x,father(person1,x))
relc4=run(0,x,father(x,person2))
if relc1==(person2,) or relc2==(person1,):
    print(person2+" is father of "+person1)
elif relc3==(person2,) or relc4==(person1,):
    print(person1+" is father of "+person2)

#function for mother
reld1=run(0,x,mother(x,person1))
reld2=run(0,x,mother(person2,x))
reld3=run(0,x,mother(person1,x))
reld4=run(0,x,mother(x,person2))
if reld1==(person2,) or reld2==(person1,):
    print(person2+" is mother of "+person1)
elif reld3==(person2,) or reld4==(person1,):
    print(person1+" is mother of "+person2)


#Function for cousin brothers
def cousin_bro(x,y):
    temp=var()
    temp1=var()
    temp2=var()
    result = conde((father(temp1,x),father(temp,temp1),father(temp,temp2),father(temp2,y),male(x),male(y)))
    return result
rele1=run(0,x,cousin_bro(x,person1))
state1=run(0,x,father(x,person2))
state2=run(0,x,father(x,person1))
for i in rele1:
    if i==person2 and state1!=state2:
        print(person1+" and "+person2+" are cousin brothers")

#Function for cousin sisters
def cousin_sis(x,y):
    temp=var()
    temp1=var()
    temp2=var()
    result = conde((father(temp1,x),father(temp,temp1),father(temp,temp2),father(temp2,y),female(x),female(y)))
    return result
relf1=run(0,x,cousin_sis(x,person1))
statf1=run(0,x,father(x,person2))
statf2=run(0,x,father(x,person1))
for i in relf1:
    if i==person2 and statf1!=statf2:
        print(person1+" ard "+person2+" cousin sisters")


#Function for cousin brother and cousin sister
def cousin(x,y):
    temp=var()
    temp1=var()
    temp2=var()
    result = conde((father(temp1,x),father(temp,temp1),father(temp,temp2),father(temp2,y),male(x),female(y)))
    return result
relg1=run(0,x,cousin(x,person1))
relg2=run(0,x,cousin(person2,x))
relg3=run(0,x,cousin(person1,x))
relg4=run(0,x,cousin(x,person2))
statg1=run(0,x,father(x,person2))
statg2=run(0,x,father(x,person1))
if person2 in relg4 or relg1:
    if person2 in la2 and statg1!=statg2:
        print(person1+" is cousin sister of "+person2)
if person2 in relg3 or relg2:
    if person2 in lb2 and statg1!=statg2:
        print(person1+" is cousin brother of "+person2)


#Function for spouse
def spouse(x,y):
    temp=var()
    result = conde((father(x,temp),mother(y,temp)))
    return result
relk1=run(0,x,spouse(x,person1))
relk2=run(0,x,spouse(person2,x))
relk3=run(0,x,spouse(person1,x))
relk4=run(0,x,spouse(x,person2))
if relk2==(person1,) and relk1==(person2,):
    print(person2+" and "+person1+" are both spouses")
if relk3==(person2,) and relk4==(person1,):
    print(person1+" and "+person2+" are both spouses")

#function for uncle
def uncle(x,y):
    temp=var()
    result = conde((father(temp,x),grandfather(temp,y),male(x)))
    return result
relh1=run(0,x,uncle(x,person1))
relh2=run(0,x,uncle(x,person2))
stath1=run(0,x,father(person2,x))
stath2=run(0,x,father(person1,x))
if person2 in (relh1 or relh2) and person1 not in (stath1 or stath2):
    if person2 in la1:
        print(person2+" is uncle of "+person1)
if person1 in (relh1 or relh2) and person2 not in (stath1 or stath2):
    if person1 in la1:
        print(person1+" is uncle of "+person2)

#Function for aunty
def aunty(x,y):
    temp=var()
    temp1=var()
    temp2=var()
    temp3=var()
    result = conde((mother(x,temp3),father(temp2,temp3),father(temp,temp2),father(temp,temp1),father(temp1,y),female(x)))
    return result
reli1=run(0,x,aunty(x,person1))
reli2=run(0,x,aunty(x,person2))
stati1=run(0,x,mother(person1,x))
stati2=run(0,x,mother(person2,x))
if person2 in (reli1 or reli2) and person1 not in (stati1 or stati2):
    if person2 in lb1:
        print(person2+" is aunty of "+person1)
if person1 in (reli1 or reli2) and person2 not in (stati1 or stati2):
    if person1 in lb1:
        print(person1+" is aunty of "+person2)

#Function for siblings
def sibling(x,y):
    temp=var()
    result = conde((father(temp,x),father(temp,y)))
    return result
relj1=run(0,x,sibling(x,person1))
statj1=run(0,x,father(x,person1))
statj2=run(0,x,father(x,person2))
if person1 in relj1 and person2 in relj1:
    if statj1==statj2:
        print(person2+" and "+person1+" are siblings")

#Function for mother in law
def mother_in_law(x,y):
    temp=var()
    result = conde((mother(x,temp),spouse(temp,y),female(x),female(y)))
    return result
rell1=run(0,x,mother_in_law(x,person1))
rell2=run(0,x,mother_in_law(person2,x))
rell3=run(0,x,mother_in_law(person1,x))
rell4=run(0,x,mother_in_law(x,person2))
if person1 in rell2 and rell1==(person2,):
    print(person2+" is mother in law of "+person1)
elif rell4==(person1,) and person2 in rell3:
    print(person1+" is mother in law of "+person2)

#Function for father in law
def father_in_law(x,y):
    temp=var()
    result = conde((father(x,temp),spouse(temp,y),male(x),female(y)))
    return result
relm1=run(0,x,father_in_law(x,person1))
relm2=run(0,x,father_in_law(person2,x))
relm3=run(0,x,father_in_law(person1,x))
relm4=run(0,x,father_in_law(x,person2))
if person1 in relm2 and relm1==(person2,):
    print(person2+" is father in law of "+person1)
elif relm4==(person1,) and person2 in relm3:
    print(person1+" is father in law of "+person2)

#Function for sister in law
def sister_in_law(x,y):
    temp=var()
    result = conde((sibling(x,temp),spouse(temp,y),male(x),female(y)))
    return result
reln1=run(0,x,sister_in_law(x,person1))
reln2=run(0,x,sister_in_law(person2,x))
reln3=run(0,x,sister_in_law(person1,x))
reln4=run(0,x,sister_in_law(x,person2))
statn1=run(0,x,spouse(person2,x))
statn2=run(0,x,spouse(x,person1))
statn3=run(0,x,spouse(person1,x))
statn4=run(0,x,spouse(x,person2))
if person1 in reln2 and person2 in reln1:
    if statn1!=(person1,) and statn2!=(person2,):
        print(person1+" is sister in law of "+person2)
elif person2 in reln3 and person1 in reln4:
    if statn4!=(person1,) and statn3!=(person2,):    
        print(person2+" is sister in law of "+person1)


#Function for co-sister in law
def co_sister_in_law(x,y):
    temp=var()
    temp1=var()
    result = conde((spouse(temp,x),sibling(temp,temp1),spouse(temp1,y),female(x),female(y)))
    return result
relo1=run(0,x,co_sister_in_law(x,person1))
relo2=run(0,x,co_sister_in_law(person2,x))
if person1 in relo2 and person2 in relo1:
    if person1 in lb1 and person2 in lb1:
        print(person1+" is co sister in law of "+person2)