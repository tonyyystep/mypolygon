import turtle
bob = turtle.Turtle()
print(bob)

def square(t):
  
    for i in range(t):
        print('Hello')
        bob.fd(100)
        bob.lt(90)
square(bob)
turtle.mainloop()