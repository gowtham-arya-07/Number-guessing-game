import random
print("you have 7 charcters")
low=int(input("enter lower number:"))
high=int(input("enter higher number:"))

num=random.randint(low,high)
ch=7
guess=0

while guess<ch:
    guess+=1
    guess=int(input("enter the gucess:"))

    if guess==num:
        print(num,"correct")
        exit()
            
    elif guess>=ch and guess!=num:
        print("better luck next time:")2
        

    elif guess<num:
        print("try high number:")

    elif guess>num:
        print("try lower number:")
        
        
    

