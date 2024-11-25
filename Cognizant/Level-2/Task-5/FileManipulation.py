file = open("ex.txt","r")
d = dict()
    
for line in file:
    line = line.strip()
    line = line.lower()
    words = line.split(" ")
    for word in words:
        if word in d:
            d[word]+=1
        else:
            d[word] = 1
            
a=list(d.keys())
a.sort()
for key in a:
    print(key,"occurences =",d[key])
    