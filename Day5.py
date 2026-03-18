#1.print number 1 to 10  using for loop
for i in range(1, 11):
    print(i, end=' ')

#2.print even num from 1 to 20
for i in range(2,21,2):
    print(i, end=' ')

#3.print odd num from 1 to 15
for i in range(1,16,2):
    print(i, end=' ')
for i in range(21,3,-2):
    print(i,end=' ')

#4.print each charchter of the string
text = "Hello"

for char in text:
    print(char)

#5.prin all items to the list
data =["data","science","all"]
for items in data:
    print(items)


#6.find the sum of number from 1 to 10
total = 0
for i in range(1, 11):
    total += i
print(total)

#7.print multiplication table of 5
for i in range(1, 11):
    print("5 x", i, "=", 5 * i)

#8.count how many vowles are in string
text = "Hello World"
count = 0

for char in text:
    if char.lower() in "aeiou":
        count += 1

print("Number of vowels:", count)

#9.print numbers in reverse  order from 10 to 1.
for i in range(10, 0, -1):
    print(i)

#10.print squere of number from 1 to 5
for i in range(1, 6):
    print(i ** 2)

