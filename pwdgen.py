import random

num = int(input("Number of passwords needed? "))
length = int(input("Length of the passwords? "))
chars = [chr(i) for i in range(33,122)]

pass_set=[]
while True:
  passw = ""
  for i in range(length):
    passw += random.choice(chars)
  pass_set.append(passw)
  num-=1
  if(num==0):
    break
print(pass_set)
