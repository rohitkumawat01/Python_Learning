# question 1  

a=[]
a1=input("Enter the value of list 1 :- ")
a.append(a1)
a2=input("Enter the value of list 2 :- ")
a.append(a2)
a3=input("Enter the value of list 3 :- ")
a.append(a3)
a4=input("Enter the value of list 4 :- ")
a.append(a4)
a5=input("Enter the value of list 5 :- ")
a.append(a5)
a6=input("Enter the value of list 6 :- ")
a.append(a6)
print(a)

# Quwstion no. 2


student=[]
a1=int(input("Enter the Number of subject 1 :- ")) # int isliye lagaya kyuki execute karte time pata chal jaye ki ye value int type ki nahi to vo string type ki samjhega or unko sort karega per as a word
student.append(a1)
a2=int(input("Enter the Number of subject :- "))
student.append(a2)
a3=int(input("Enter the Number of subject 3 :- "))
student.append(a3)
a4=int(input("Enter the Number of subject :- "))
student.append(a4)
a5=int(input("Enter the Number of subject :- "))
student.append(a5)
a6=int(input("Enter the Number of subject 6 :- "))
student.append(a6)
student.sort()
print(student)

# Question 3

tuple=(222,3445345,"rohit","kumawat",342.34434)
tuple[3]="ROhit"      #####  tuples are not change because of they are IMmutable ####



# Question 4  

a=[50,3242423,54354654756,65876787546,345354353]

print(sum(a))


# Question 5

a=[7,0,8,0,0,9]
b=a.count(0)
print(b)




