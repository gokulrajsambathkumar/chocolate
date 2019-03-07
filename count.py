a = int(input("Please Enter any Number: "))
Count = 0
while(a> 0):
   a = a // 10
   Count = Count + 1

print("\n Number of Digits in a Given Number = %d" %Count)
