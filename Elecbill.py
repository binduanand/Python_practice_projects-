name = input("Enter Consumer Name")
n = int(input("Enter Number of units consumed"))
if n==0:
  bill=100
elif n<=200:
  bill = n*0.8
elif n>200 and n<=300:
  bill = 200*0.8 + (n-200)*0.9
elif n>300:
  bill= 200*0.8 + 100*0.9 + (n-300)*1.0

if bill>400:
  sur = bill*15/100.0
else:
  sur = 0

print("Consumer Name:",name)
print("Units Consumed:",n)
print("Bill:",bill)
print("Service charge:",sur)
print("Total Bill:",bill+sur)

 

  