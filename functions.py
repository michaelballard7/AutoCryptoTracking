def function():
    print("Hello")

function()



def function(name = "Oliver"):
    print("Hell0 " + name)

function("michael")
function()

def function(number1, number2):
    number1 += 10
    number2 += 100

    return number1 + number2

print(function(100, 10))
