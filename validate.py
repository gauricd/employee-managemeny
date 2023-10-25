#def valid_Empid(id):
    
def valid_Empname(name):
    l=name.split()
    if len(l)==2 or len(l)==3:
        if len(l)==3:
            if (l[0].isalpha() and l[1].isalpha() and l[2].isalpha()):
                return True
        else:
            if (l[0].isalpha() and l[1].isalpha()):
                return True
    return False
#print(valid_Empname("Gauri Deshmukh"))

def valid_Salary(sal):
    s=str(sal)
    if sal>=0 and s.isdigit():
        return True
    else:
        return False
#print (valid_Salary(30000))
"""def valid_Age(age):
    a=str(age)
    if age>=20 and a.isdigit():
        return True
    else:
        return False"""
           
def valid_Gender(g):
    gender=('Male','Female','Trans')
    if g.title() in gender:
        return True
    else:
        return False
#print (valid_Gender("male"))
    
#def valid_Address(add)


def valid_City(state,city):
    sc={"maha":["mumbai","pune","nashik"],
         "MP":["indore","ujjain"],
         "bihar":["patna","gaya","nawada"],
         "up":["agra","kanpur"]}
    v=sc[state]
    if city in v:
        return True
    else:
        return False
#print (valid_City("Maha","Pune"))


 
def valid_DOB(year,month,date):
    if year<0:
        return False
    if month<1 or month>12:
        return False
    if month in {1,3,5,7,8,10,12} and (date<1 or date>31):
        return False
    elif month in {4,6,9,11} and (date<1 or date>30):
        return False
    elif month==2:
        if(year%4==0 and year%100==0) or (year%400==0):
            if date<1 or date>29:
                return False
        else:
            if date<1 or date>28:
                return False
    return True

 
def valid_DOJ(year,month,date):
    if year<0:
        return False
    if month<1 or month>12:
        return False
    if month in {1,3,5,7,8,10,12} and (date<1 or date>31):
        return False
    elif month in {4,6,9,11} and (date<1 or date>30):
        return False
    elif month==2:
        if(year%4==0 and year%100==0) or (year%400==0):
            if date<1 or date>29:
                return False
        else:
            if date<1 or date>28:
                return False
    return True 


def valid_Depname(dname):
    d=["It","Hr","Finance","Marketing","Sales"]
    if dname in d:
        return True
    else:
        return False
#print (valid_Depname("HR"))
    
def valid_Designation(designation):
    de=["Manager","Software Developer","Accountant","Customer Service",
         "Marketing Coordinator","IT Support","Data Analyst"]
    if designation in de:
        return True
    else:
        return False


def valid_Pan(pan):
    if pan.isalnum() and pan.isupper() and len(pan)==10 and pan[0:4].isalpha() and pan[4:9].isdigit() and pan[9].isalpha():
        return True
    else:
        return False
#print (valid_Pan("AAAA00000A"))
    
def valid_Aadhar(adhno):
    if len(adhno)==12 and adhno.isdigit():
        return True
    else:
        return False
#print(valid_Aadhar("1234567890"))
        

        

        

        

        
        



        