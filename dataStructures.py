# Tuples

# tupleNumber = (12,34,43,56)
# tupleString = ("Michael","Is","Becoming","A","Beast")
# tupleMulti = (12,"thirty four", 43 ,"fifty six")
#
# print(len(tupleNumber))
# print(max(tupleNumber))
# print(min(tupleNumber))
#
#
# print(len(tupleMulti))
#
#
# print(len(tupleString))
# print(max(tupleString))
# print(min(tupleString))
#
# print(tupleNumber.index(34)) # I can search for the index of an existing element inside a tuple
#
#


# lists
# listNumber = [1,2,3,4]
# ListString = ["Michael", "Anthony", "Ballard"]
# listNumber.append(7) # add an element to the end of my list
# listNumber.insert(1,6) # choose an element position and insert a value
# listNumber[0] = 130 # change a specific elements value
#
# # del listNumber[2] # delete a specific index
# # print(listNumber)
# # print(listNumber[:3]) # slice specific elements from my list
# # print(listNumber[-1:])
# # print(listNumber[1:-1])
#
#
# multiList = [listNumber, ListString] # creates a new variable that stores a list of list
# print(multiList)
# print(multiList[0][0]) # access element from a specific element from within a nested list
# print(multiList[1][0]) # access element from a specific element from within a nested list
# listNumber += ListString # combines to lists into one list
# print(listNumber)


# dictionaries
#
# dict = {1:'one', 2:'two', "apple":"green"}
# print(dict[2])
# print(dict["apple"])
#
# dict[1] = "set a new value"
# print(dict)

# Sets
# sets can only have the same element one time
set = {1,2,3,4}
set.add(7)  # I can add an element to a set with the add method
print(set)
set.remove(1) # remove a specific value from a set
