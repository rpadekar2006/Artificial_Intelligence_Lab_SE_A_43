
print("*****Stream Selection*****")

print("Choose subject (Maths, Physics, Chemistry, AI,Graphic, Circuit, Programming,Robotic) ")

Subject1= input("Enter your first  Favourite Subject: ").capitalize()
Subject2= input("Enter your Second Favourite Subject: ").capitalize()

if(Subject1=="Maths" and Subject2=="Programming"):
	print("your branch s Compuer Engineering")
elif(Subject1=="Maths" and Subject2=="Physic"): 	
	print("your branch s Mechanical Engineering")
elif(Subject1=="Graphic" and Subject2=="Maths"):
	print("your branch s Civil Engineering")
elif(Subject1=="Maths" and Subject2=="Circuit"):
	print("your branch s electrical Engineering")
elif(Subject1=="Graphic" and Subject2=="Maths"):
	print("your branch s Civil Engineering")
elif(Subject1=="Programming" and Subject2=="AI"):
	print("your branch s AI&DS Engineering")
elif(Subject1=="Robotic" and Subject2=="AI"):
	print("your branch s AI&DS Engineering")

else:
	print("Invalid Input")

