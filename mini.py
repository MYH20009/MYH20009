import random
import art
print (art.logo)
head_tail= [art.head_logo, art.tail_logo]
user = int(input("Enter your guess number 0 = head and 1 = tail > "))
sys_cho= random.randint(0,1)
print("Your choice = ")
print(head_tail[user])
print("System choice = ")
print(head_tail[sys_cho])
if user==sys_cho:
    print("You won !!")
else:
    print("You lost !!")
