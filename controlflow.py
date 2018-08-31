rating = 3.2


# I can nest if statements inoder to achieve control flow:
if rating <= 5 and rating > 4:
    if rating >= 4.5:
        if rating == 5:
            print("Perfect")
        else:
            print("Excellent")
    else:
        print("great")
elif rating <=4 and rating >2:
    print ("good")
elif rating <= 2 and rating > 0:
    print("bad")
else:
    print("error")


# I can also use while loops to achieve control flow
f = 1

# I can create an infinite loop which can be broken by an if statement
# I can use the infinite while when I do not know the length of the elements I am using
while(True):
    print(f)

    if(f == 10):
        break
    f += 1

# if I know the length of the elements in my data structure, I should use a for loop
numbers = [1,2,3,4,5]

for each in numbers:
    print(each)

for index in range(len(numbers)):
    print(numbers[index])
