def most_frequent(string):
    l=len(string)
    d = {}
    
    for i in range(l):
        d[string[i]] = 0
   
    for j in range(l):     
        for key,value in d.items() :
            if (string[j]==key):
                d[key]=d[key]+1
    
    res = {key: val for key, val in sorted(d.items(), key = lambda ele: ele[1], reverse = True)} 
    for key,value in res.items() :
        print(key,"=",value)
        
string=input("Input your string:")
most_frequent(string)
