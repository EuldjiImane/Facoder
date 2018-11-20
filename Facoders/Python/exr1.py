def number_list():
    list=[]
    n='Add'
    while n !='Done' :
        new=int(input('enter a number: '))
        list.append(new)
        n=input('add or Done')
    list2=[list[0],list[-1]]
    return list2
print(number_list())
