print("Hello")
name = input("Type your name")
print("Welcome",name,"to this game")

print("You have been living in prison for 5 years.")
print("One day, you found a chance to escape. Then you are trying to escape.")

answer = input("You are nearly to escape the prison. You found two ways. And you have to choose right or left.Type Right or Left")

if answer == "Left":
    answer = input("You face with police officer then you are starting fight with him and you grabed his gun. You can Shoot or Run.")
    if answer == "Shoot":
        print("You made a gun shot sound and other secruitys come to you and you lose.")
    elif answer == "Run":
        print("Officer called for help and you have captured.")
    else:
        print("Not in valid options, you lose")

elif answer == "Right":
    answer = input("You found other prisoners and they tell you to come with them. You can follow or unfollow. Type F for follow and U for unfollow.")
    if answer == "F":
        print("You has betrayed by them and captured by police, you lose.")
    elif answer == "U":
        print("You move alone then you escape.")
        print("You have escaped from the prison. And polices are searching you.")

        answer = input("Now you have escaped and you have to decide where would like to go?Type City for city and Village for country side.")
        if answer == "City":
            answer = input("Now decide how would you go to city?By foot or by car. Type F for by foot and Type C for by car.")
            if answer == "C":
                print("You don't have car. So you stop the car on road and rob the car. Then you got arrested by police at the check point. You lose.")
            elif answer == "F":
                print("You die because of lacking food and water. You lose.")
            else:
                print("Not in valid options, you lose.")
        elif answer == "Village":
            print("Congratulation!, you have completely escape from prison.")
        else:
            print("Not in valid option, you lose")
    else:
            print("Not in valid options, you lose.")
    
else:
    print("Not in valid options, you lose")

print("Thanks for playing," ,name,)