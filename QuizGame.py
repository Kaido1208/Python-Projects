print("Welcome to my One Piece Quiz!")

playing = input("Do you want to play a One Piece game? ")

if playing.lower() != "yes":
    quit()
print("Cool! Now let's play a game!")
score = 0

answer = input("Question 1: What is Luffy's current bounty? ")
if answer == "3 billion beri":
    print("Correct!")
    score += 1
else : 
    print("That's not correct")

answer = input("Question 2: Who is Luffy's first mate? ")
if answer == "Roronoa Zoro":
    print("Correct!")
    score += 1
else : 
    print("That's not correct")

answer = input("Question 3: What is Luffy's last name? ")
if answer == "Monkey":
    print("Correct!")
    score += 1
else : 
    print("That's not correct")

answer = input("Question 4: Who is the Author of One Piece? ")
if answer == "Eichiiro Oda":
    print("Correct!")
    score += 1
else : 
    print("That's not correct")

answer = input("Question 5: How old is Luffy now? ")
if answer == "19":
    print("Correct!")
    score += 1
else : 
    print("That's not correct")

print("Here's your score: " + str(score))
print("Here's your score percentage: " + str((score / 5) * 100) + "%.")