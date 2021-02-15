import csv
p=open("demo.csv","w",newline='')
emp=csv.writer(p)
emp.writerow(["Emp id","Emp Name","salary"])
for i in range(3):
    empid=int(input("enter ID:"))
    empname=input("Enter Name:")
    salary=int(input("Enter Salary:"))
    empinfo=[empid,empname,salary]
    emp.writerow(empinfo)

p.close()
