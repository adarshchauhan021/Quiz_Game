print("Welcome to my computer quiz!")

playing=input("Do you want to play? ")
print(playing)

if playing.lower() != "yes":
  quit()

print("OKAY! Let's play ")
score=0

answer = input("What does CPU stand for? ")
if answer.lower() == "central processing unit":
  print('Correct!')
  score+=1
else:
  print("Incorrect")

answer = input("What does ALU stand for? ")
if answer.lower() == "Arithematic Logic unit":
  print('Correct!')
  score+=1
else:
  print("Incorrect")

answer = input("What does I&O stand for? ")
if answer.lower() == "input and output":
  print('Correct!')
  score+=1
else:
  print("Incorrect")

# print no. of questions correct
print("You got " +str(score)+" question correct!")

# print average 
print("You got " +str((score/3)*100) + "%.")