#Task 1

b=float(input("Input the radius of the circle: "))
r=b
area=(22/7)*r*r
print("The area of the circle with radius",b,"is :", area)

#Task 2

name=input(("\n\nInput the file name: "))
ext = name.split(".")
if ext[1]=="py":
    extn="'python'"
elif ext[1]=="java":
    extn="'java'"
elif ext[1]=="c":
    extn="'c'"
elif ext[1]=="cpp":
    extn="'cpp''"
else:
    extn="unknown"
    
print("The extension of the file is:", extn)
