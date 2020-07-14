n=int(input("Enter the number of fibinocci numbers needed: "))
new=0
x1=0
x2=1
print("the fibinocci numbers are: ")
count=1
while count <= n:
    print(x1,"\t")
    new=x1+x2
    x1=x2
    x2=new
    count=count+1
