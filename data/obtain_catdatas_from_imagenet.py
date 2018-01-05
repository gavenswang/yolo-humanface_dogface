import os
from os import listdir

k9name = open('9k.names')
k9tree = open('9k.tree')

count = 0

catfileList = []
catfilemark = set()
k9treeList = []
for tree in k9tree:
    line = tree[:-1].split(' ')
    k9treeList.append([line[0],line[1]])
    
for name in k9name:
    if name.strip('\n') == 'cat':
        catfileList.append(k9treeList[count][0])
        catmark = count
        catfilemark.add(str(catmark))
    count+=1
#lenfile = len(catfilemark)
while True:
    lenfile = len(catfilemark)   
    #print(lenfile) 
    for temp in k9treeList:
            
            if temp[1] in catfilemark:
                #print("yes")
                
                catmark = k9treeList.index(temp)
                #print("********",catmark)
                catfilemark.add(str(catmark))
    #print(catfilemark)
    lenlist = len(catfilemark)
    #print("....",lenlist)
    if lenlist == lenfile:
        break

#print(catfilemark)
        
        
k9tree.seek(0)
#print(catmark)
for tree in k9tree:
    line = tree[:-1].split(' ')
    if line[1] in catfilemark:
        catfileList.append(line[0])
print(catfileList)
k9name.close()
k9tree.close()
    
    
