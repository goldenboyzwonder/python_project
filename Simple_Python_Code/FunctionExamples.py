#CREATING A SIMPLE FUNCTION
def test(name): #<--Function name and parameter name
    '''Creating function with name=test with a parameter of name'''
    
    print(f"Hello World from {name}!!")#<--prints a comment
    '''the function is simple and only prints the name and string'''
    
test("Jacob")#<--calling the function with an argument


a = "David"
def f(i):
    print(f"{i}, Welcome to your dashboard")
f(a)