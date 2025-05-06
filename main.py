import random
target = random.randint(1,100)
while True:
  user = int(input("Enter a Number(1,100): "))
  if(user < target):
    print("Too Low!")
  elif(user > target ):
    print("Too High!")
  else:
    print("Correct guess ")
    break
 