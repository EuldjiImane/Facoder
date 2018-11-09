student=input("Enter student's name: ")
s1= ['Ahmad', 18, 17, 19.5, 8, 25]
s2= ['Sami', 20, 20, 19, 9, 28]
s3= ['Faris', 14.5, 16, 13, 7, 23]

if student == s1[0]:
    s=s1
    sum=s[1] +s[2]+s[3]+s[4]+s[5]
    print(s[0],":",sum)
elif student == s2[0]:
    s=s2
    sum=s[1] +s[2]+s[3]+s[4]+s[5]
    print(s[0],":",sum)
elif student == s3[0]:
    s=s3
    sum=s[1] +s[2]+s[3]+s[4]+s[5]
    print(s[0],":",sum)
else:
    print("Student is not recorded 0")
