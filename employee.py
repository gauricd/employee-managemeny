from validate import *
from datetime import datetime
class employee:
    def __init__(self,id1,name,sal,age,gender,add,city,dob,doj,dname,designation,pan,adh):
        self.id1=id1
        self.name=name
        self.sal=sal
        self.age=age
        self.gender=gender
        self.add=add
        self.city=city
        self.dob=dob
        self.doj=doj
        self.dname=dname
        self.designation=designation
        self.pan=pan
        self.adh=adh
    def display(self):
        print(self.id1,self.name,self.sal,self.age,self.gender,self.add,self.city,self.dob,self.doj,self.dname,self.designation,self.pan,self.adh)       
emp=[]
while True:
    print("1:Add a record of Employee.")
    print("2.Delete the record of Employee.")
    print("3.Update Employee details.")
    print("4.Search details of Employee.")
    print("5.Display the details of Employee with highest salary.")
    print("6.Display the details of Employee with lowest salary.")
    print("7.Exit")
    choice=int(input("Enter ur choice."))
    if choice ==1:
        id1=input("Enter ur Employee_Id.")
        while True:
            name=input("Enter ur Name.")
            if valid_Empname(name):
                break
            else:
                print("Invalid name")
        while True:
            sal=int(input("Enter ur salary."))
            if valid_Salary(sal):
                break
            else:
                print("Invalid Salary")   
        
        while True:
            gender=input("Enter ur gender.")
            if valid_Gender(gender):
                break
            else:
                print("Invalid gender") 
                
        add=input("Enter ur address with Pin code.")
        
        
        while True:
            state=input("Enter ur state.")
            city=input("Enter ur city.")
            if valid_City(state,city):
                break
            else:
                print("Invalid city")
        while True:  
            dob=input("Enter ur dob(YYYY-MM-DD).")
            year,month,date=map(int,dob.split('-')) 
            if valid_DOB(year,month,date):
                current_year=datetime.now().year
                age=current_year-year
                print(f"the year is.{year,month,date},the  age is.{age}")
                break
            else:
                print("Invalid dob")
        while True:
            doj=input("Enter ur doj(YYYY-MM-DD).")
            year,month,date=map(int,dob.split('-'))
            if valid_DOJ(year,month,date):
                break
            else:
                print("Invalid date")
            
        while True:    
            dname=input("Enter ur Department_name.")
            if valid_Depname(dname):
                break
            else:
                print("Invalid Department_name")
        while True:        
            designation=input("Enter ur designation.")
            if valid_Designation(designation):
                break
            else:
                print("Invalid designation")
        
        while True:   
            pan=input("Enter ur Pan_no.")
            if valid_Pan(pan):
                break
            else:
                print("Invalid Pan_no")
        while True:
            adh=input("Enter ur Aadhar_no.")
            if valid_Aadhar(adh):
                break
            else:
                print("Invalid Aadhar_no")
        e=employee(id1,name,sal,age,gender,add,city,dob,doj,dname,designation,pan,adh)
        emp.append(e)
            
        for i in emp:
            i.display()
            
    elif choice==2:
        eid=input("Enter the Employee_id to delete the record.")
        flag = True
        for i in emp:
            if i.id1==eid:
                flag = False
                emp.remove(i)
        if flag==True:
            print("Employee_id Not Found")
            
    elif choice==3:
        eid=input("Enter the Employee_id.")
        for i in emp:
            if i.id1==eid:
                print("Press a to update the name of the employee.")
                print("Press b to update the address of the employee.")
                print("Press c to update the dob of the employee.")
                print("Press d to update the salary of the employee.")
                ch=input("Enter ur choice.")
                if ch=="a":
                    nm=input("Enter the updated name.")
                    i.name=nm
                elif ch=="b":
                    a=int(input("Enter the updated address."))
                    i.add=a
                elif ch=="c":
                    d=input("Enter the updated DOB.")
                    i.dob=d
                elif ch=="d":
                    print("Press i to update the salary of specific employee by Employee_id.")
                    print("Press ii to update the salary of all employee working in specific department.")
                    print("Press iii to update the salary of all employee.")
                    ch=input("Enter ur choice.")
                    if ch=="i":
                        eid=input("Enter the Employee_id to update the salary.")
                        flag = True
                        for i in emp:
                            if i.id1==eid:
                                flag = False
                                i.sal = i.sal +i.sal*0.1                              
                                print("Salary updated of the gievn Employee_id")
                        if flag==True:
                            print("Employee_id Not Found") 
                    elif ch=="ii":
                        dn=input("Enter the Department_name to update the salary of all employee.")
                        flag = True
                        for i in emp:
                            if i.dname==dn:
                                flag = False
                                i.sal+=i.sal * 0.1
                                print("Salary updated of all employee has been updatedof the given department")
                        if flag==True:
                            print("Department_name Not Found") 
                    elif ch=="iii":
                        for i in emp:
                            i.sal+=i.sal * 0.1
                            print("Salary updated for all employees.")
                else:
                    print("Invallid choice")
                    
    elif choice==4:
        print("Press a to search by Employee_id.")
        print("Press b to search by Employee_name.")
        print("Press c to search by Department_name.")
        ch=input("Enter ur choice.")
        if ch=="a":
            eid=input("Enter the Employee_id to be searched.")
            for i in emp:
                if i.id1==eid:
                    i.display()
        elif ch=="b":
            nm=input("Enter the Employee_name to be searched.")
            for i in emp:
                if i.name==nm:
                    i.display()
        elif ch=="c":
            dn=input("Enter the Department_name to be searched.")
            for i in emp:
                if i.dname==dn:
                    i.display()
        else:
            print("Invalid choice")
            
    elif choice==5:
        sal=emp[0].sal
        for i in emp:
            if i.sal>sal:
                sal=i.sal
        for i in emp:
            if i.sal==sal:
                i.display()
        
    elif choice==6:
        sal=emp[0].sal
        for i in emp:
            if i.sal<sal:
                sal=i.sal
        for i in emp:
            if i.sal==sal:
                i.display()
                
    elif choice==7:
        break
    else:
        print("Enter valid choice")