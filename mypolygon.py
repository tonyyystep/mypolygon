import turtle
bob = turtle.Turtle()
print(bob)
def square(t, lenght):
  
    for i in range(4):
        print('Hello')
        bob.fd(lenght)
        bob.lt(90)
        

def polygon(t, n, z):
  
    for i in range(n):
        bob.fd(z)
        bob.lt(360/n)

polygon(bob, 10, 100)
turtle.mainloop()