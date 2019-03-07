#While this is a vary basic algorithm, I would like to write another piece which generates a large csv file
#recording the results and plotting them, everaging out the success/failure of the computer
from random import randint

rand = randint(1,1000) # GENERATES THE RANDOM NUMBER FOR THE COMPUTER TO GUESS

guess = randint(1,1000) # GENERATES A RANDOM NUMBER FOR THE COMPUTER TO BEGIN GUESSING

print("Computer picks ",rand)
print("Computer guess ",guess) #Initial guess. At no point do these variables equal each other.

high = 1000
low = 1
n = 0 # just a counter variable


while guess != rand:       # The HIGH, and LOW variables are the ones which are trained against the computer's guessing variable.
	                       # When the initial GUESS variable takes on their values, divided by 2, it will eventually 
	                       # converge on the desired result.
	if guess > rand:
		high = guess
	elif guess < rand:
		low = guess + 1

		
	print("COMPUTER PICKS: ",rand,' ',"COMPUTER GUESSES: ",guess)
	
	n = n + 1
	
	guess = (high + low) // 2
	

print("COMPUTER PICKS: ",rand,' ',"COMPUTER GUESSES: ",guess)
print("Took ",n," guesses")
