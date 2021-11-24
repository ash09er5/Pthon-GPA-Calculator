classess=[]
grades=[]
creditss=[]
Qp=[]
x=1
print("How many classes did you take")
y=int(input())
while (x<=y)  : 
   print("Enter class")
   classesss=str(input())
   classess.append(classesss)
   print("Enter grade")
   grade=str(input())
   grades.append(grade)
   print("Enter credit")
   credit=float(input())
   creditss.append(credit)
   total = 0
   for element in grade:
        if element == "A+":
            total = 4.0
            Qps=(total*credit)
            Qp.append(Qps)
            gpa=sum(Qp)/sum(creditss)
            
            print(sum(Qp))
            print(sum(creditss))
            print(gpa)
        elif element == "A":
            total = 4.0
            Qps=(total*credit)
            Qp.append(Qps)
            gpa=sum(Qp)/sum(creditss)
            
            print(sum(Qp))
            print(sum(creditss))
            print(gpa)
        elif element == "A-":
            total = 3.7
            Qps=(total*credit)
            Qp.append(Qps)
            gpa=sum(Qp)/sum(creditss)
            print(sum(Qp)/sum(creditss))
            print(gpa)
        elif element == "B+":
            total =  3.3
            Qps=(total*credit)
            Qp.append(Qps)
            gpa=sum(Qp)/sum(creditss)
            print(gpa)
        elif element == "B":
            total = 3.0
            Qps=(total*credit)
            Qp.append(Qps)
            gpa=sum(Qp)/sum(creditss)
            print(gpa)
        elif element == "B-":
            total = 2.7
            Qps=(total*credit)
            Qp.append(Qps)
            gpa=sum(Qp)/sum(creditss)
            print(sum(Qp)/sum(creditss))
        elif element == "C+":
            total = 2.3
            Qps=(total*credit)
            Qp.append(Qps)
            gpa=sum(Qp)/sum(creditss)
            print(sum(Qp)/sum(creditss))
        elif element == "C":
            total = 2.0
            Qps=(total*credit)
            Qp.append(Qps)
            gpa=sum(Qp)/sum(creditss)
            print(sum(Qp)/sum(creditss))
        elif element == "C-":
            total = 1.7
            Qps=(total*credit)
            Qp.append(Qps)
            gpa=sum(Qp)/sum(creditss)
            print(sum(Qp)/sum(creditss))
        elif element == "D":
            total = 1.0
            Qps=(total*credit)
            Qp.append(Qps)
            gpa=sum(Qp)/sum(creditss)
            print(sum(Qp)/sum(creditss))
        elif element == "D-":
            total = 0.67
            Qps=(total*credit)
            Qp.append(Qps)
            gpa=sum(Qp)/sum(creditss)
            print(sum(Qp)/sum(creditss))
        elif element == "F":
            total = 0.0
            Qps=(total*credit)
            Qp.append(Qps)
            gpa=sum(Qp)/sum(creditss)
            print(sum(Qp)/sum(creditss))
   print(classess)
   print(grades)
   print(creditss)
   
   x=x+1
print(+sum(creditss))
print("Your final gpa is...")
print(sum(Qp)/sum(creditss))