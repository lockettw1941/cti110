import random
##########################################################################################################
#Create a new Python code file named P5HW_LastnameFirstname.py
# (Change "LastnameFirstname" to your last and first names.)
# Add a title comment block to the top of the new Python file using the following form:
# A brief description of the project: this assignment is desibned to Quaiz student with math problems
# 5/2/2023
# CTI-110 P5HW - Math Quiz
# LockettWillie
############################################################################################################
def addRandom():
	n1=random.randint(0,1000)
	n2=random.randint(0,1000)
	print(f"{n1:>6}")
	print(f"+{n2:>5}")
	print("Enter answer")
	ans=int(input())
	while ans!=n1+n2:
	
		
		if ans<n1+n2:
			print("Sorry, guess is too low.")
		else:
			print("Sorry, guess is too high")

		ans=int(input("try again : "))
	print("Congratulations!!!! your answer is correct...")

def subRandom():
	n1=random.randint(0,1000)
	n2=random.randint(0,1000)
	print(f"{n1:>6}")
	print(f"-{n2:>5}")
	print("Enter answer")
	ans=int(input())
	while ans!=n1-n2:
	
		
		if ans<n1-n2:
			print("Sorry, guess is too low.")
		else:
			print("Sorry, guess is too high")
		ans=int(input("try again : "))
	print("Congratulations!!!! your answer is correct...")
if __name__=="__main__":

	while 1:

		print("MAIN MENU")
		print("----------------------")
		print("1) Add Random Numbers ")
		print("2) Subtract Random Numbers")
		print("3) Exit")
		num=int(input("Please choose one of the menu options: "))
		if num==3:
			print("Thank you for playing...")
			print("Bye!!")
			break
		if num==1:
			addRandom()
		if num==2:
			subRandom()