#CTI-110
#P4HW1 - Score List
#Willie Lockett
# 4/26/2023
####################################################################
#For assignment P4HW1, you will build on P2HW2 assignment.
#Instead of an individual statement to collect each score, 
#the program will use a loop. Also, after displaying score average 
#(after dropping lowest score) , the program is to display a letter 
#grade for the calculated average.
#####################################################################


#individual statement to collect each score
nos=int(input("Number of scores : "))

#create list to store scores
scoreslist=[]

#the program will use a for loop to take scores as inputs
for i in range(1,nos+1):
    
    #while loop to take input until user enters correct input
    while True:
        try:
            #taking score as input from user
            score=int(input("Enter score{}: ".format(i)))
            
            #checking if score is between 0 and 100
            if score>=0 and score<=100:
                
                #if yes, then appends to list
                scoreslist.append(score)
                break
            #if not, then prints this and asks for input again
            else:
                print("Invalid score.Enter value between 0 and 100")
        except:
            continue

#after displaying score average (after dropping lowest score) 
print("\nlist of entered scores: ")
print(scoreslist)

#printing lowest score entered 
lowestscore=min(scoreslist)
print("\nLowest score entered: {}".format(lowestscore))

#printing modified list after dropping lowest score
scoreslist.remove(lowestscore)
print("\nList after dropping lowest score: ")
print(scoreslist)

#printing average of modified scoreslist
avgofscoreslist=sum(scoreslist)/len(scoreslist)
print("\nAverage of modified list is: {}".format(avgofscoreslist))

#the program is to display a letter 
print("\nLetter grade of average of modified scoreslist: ")
if avgofscoreslist>80 and avgofscoreslist<=100:
    print("Letter grade: A")
elif avgofscoreslist>60 and avgofscoreslist<=80:
    print("Letter grade: B") 
elif avgofscoreslist>40 and avgofscoreslist<=60:
    print("Letter grade: C")
elif avgofscoreslist>20 and avgofscoreslist>=40:
    print("Letter grade: D")
else:
    print("Letter grade: E")
