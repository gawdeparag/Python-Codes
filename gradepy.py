def entry():	
    print("Enter marks obtained in 5 subjects: ")
    mark1 = int(input('Enter marks of 1st subject'))
    mark2 = int(input('Enter marks of 2nd subject'))
    mark3 = int(input('Enter marks of 3rd subject'))
    mark4 = int(input('Enter marks of 4th subject'))
    mark5 = int(input('Enter marks of 5th subject'))
def grade():
    sum = mark1 + mark2 + mark3 + mark4 + mark5
    average = sum/5
    print("Your average is",average)
    if (average>=74 and average<=100):
    		if average == 74:
    				average = average + 1
		print('Your Average is:',average)
		print("Your Grade is Distinction")
    elif (average>=59 and average<=73):
		if (average==59):
	    	average=average+1
		print("Your Average is:",average)
		print("Your Grade is First Class")
    elif (average>=49 and average<=58):
		if (average==49):
	    	average=average+1
		print("Your Average is:",average)
		print("Your Grade is Second class")
    elif (average>=39 and average<=48):
		if (average==39):
	    	average=average+1
		print("Your Average is:",average)
		print("Your Grade is Third class")
    elif (average==0 and average<=38):
		print("Your Average is:",average)
		print("Your Grade is Fail")

entry()