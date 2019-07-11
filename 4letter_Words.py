sentence="This is four word letter in list"

print(sentence)

sent=sentence.split()
print(sent,end="\n"*2)

for word in sent:
    if len(word)!=4:
        pass 
    else:
        pylist=[]
        pylist.append(word)

        print(pylist,end="\n")

        
        
       
        
        
        
        
        
        
