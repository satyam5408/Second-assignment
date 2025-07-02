
# First task
# Check the number whether it is even or odd

number = int(input("enter the number:"))

if number%2 == 0:
    print(number,"is a even number")

else:
    print(number,"is a odd number")


# Second task
# Sum of integer (1 to 50) using a while loop

num = 1
sum = 0

while num <= 50:
    sum += num
    num += 1

print("sum of interger(1 to 50):", sum)

# Sum of integer (1 to 50) using a for loop
sum = 0

for i in range(1, 51):
    sum += i
    
print(f"sum of 1 to 50 number is : {sum}")

