def pos(n):
    lst=list()
    newlst=list()
    
    if count==0:
        print("Input: list1 = ")
    else:
        print("Input: list2 = ")
        
    for i in range(0,n):
        b=int(input())
        lst.append(b)
    for i in range(0,n):
        if lst[i]>0:
            newlst.append(lst[i])
    print("Output: ",newlst)

n=int(input("Enter the number of elements in list1: "))
count=0
pos(n)
m=int(input("Enter the number of elements in list2: "))
count+=1
pos(m)
