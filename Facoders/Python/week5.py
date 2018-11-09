student=input("Enter student's name: ")
s1= ['Ahmad', 18, 17, 19.5, 8, 25]
s2= ['Sami', 20, 20, 19, 9, 28]
s3= ['Faris', 14.5, 16, 13, 7, 23]
if student != s1[0] and student != s2[0] and student!= s3[0]:
    print("Student is not recorded 0")
else:
    if student== s1[0]:
        s=s1[1:]
    elif student == s2[0]:
        s=s2[1:]
    elif student == s3[0]:
        s=s3[1:]
    sum=0
    for i in s:
        sum= sum +i
    print(student+': '+str(sum))
