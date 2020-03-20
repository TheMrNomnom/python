"""
adj1="awesome"
adj2="annoying"
adj3="crazy"
place1="England"
place2="New York"
place3="Manchester"
noun1="TV"
noun2="hammer"
noun3="chair"


adjList = ["wild", "fluffy", "hilarious"]

minIndex=0
maxIndex=len(adjList)-1

from random import randint

index1 = randint(minIndex, maxIndex)


adj1 = adjList[index1]

# You will need: the len() command, a list, importing randint.
# Think about the parameters the randint() function takes.


sentence1= "Last year, I went on a "+adj3+" trip to "+place1+"."
sentence2= "The weather there was "+adj1+", and I couldn't wait to eat a big "+noun1+" while I was there."
sentence3="Next year, I want to go to "+place1+", because I've always wanted to see the "+adj3+" "+noun3+"."
sentence4 = "When I was young, I had a " + noun2 + "."
print(sentence1)
print(sentence2)
print(sentence3)
print(sentence4)


minindex=0
maxindex=len(adjList)-1

index1=randint(minindex,maxindex)
adj1=adjList[index1]

index2=randint(minindex,maxindex)
adj2=adjList[index2]

index3=randint(minindex,maxindex)
adj3=adjList[index3]





1.  defining the minimum and maximum possible index values (lines 39 and 40). Because indexing begins with 0, the highest number that we can index is always the length of the list minus 1.
2. defining an index which takes a random number with these minimum and maximum values (line 42)
3. storing the adjective at this index as the variable to be used (line 43)
4. repeating this three times
"""



from random import randint

adjList=["wild","fluffy","hilarious"]
placeList=["Chicago","China","Brazil"]
nounList=["telephone", "karate", "toilet"]

minindex=0
maxindex=len(adjList)-1

index1=randint(minindex,maxindex)
adj1=adjList[index1]

index2=randint(minindex,maxindex)
adj2=adjList[index2]

index3=randint(minindex,maxindex)
adj3=adjList[index3]

minindex=0
maxindex=len(placeList)-1

index1=randint(minindex,maxindex)
place1=placeList[index1]
index2=randint(minindex,maxindex)
place2=placeList[index2]
index3=randint(minindex,maxindex)
place3=placeList[index3]

minindex=0
maxindex=len(adjList)-1

index1=randint(minindex,maxindex)
noun1=nounList[index1]
index2=randint(minindex,maxindex)
noun2=nounList[index2]
index3=randint(minindex,maxindex)
noun3=nounList[index3]

sentence1= "Last year, I went on a "+adj1+" trip to "+place1+"."
sentence2= "The weather there was "+adj2+", and I couldn't wait to eat a big "+noun1+" while I was there."
sentence3="Next year, I want to go to "+place2+", because I've always wanted to see the "+adj3+" "+noun2+"."
print (sentence1,sentence2,sentence3)
