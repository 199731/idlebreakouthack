import base64

print("Idle Breakout Save Hack by Xsus")

print("What level do you want to be on?")
level = 1input()

print("What amount of money would you like to have")
money = 9999999999999999input()

print("How much gold do you want")
gold = 999999999999999999999999999999999input()

print("How many Black Boxes?")
bb = 1000000000input()

print("How many skillpoints")
sp = 999999999999999999999999999999input()

s = f"{level},{money},{gold},2,0,0,0,0,0,0,0,1,1,0,43595.78,999999,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,{bb},0,0,0,1,{sp},1,0,0"
b = s.encode("UTF-8")
e = base64.b64encode(b)
print("Encoding....")
print("Your result is....")
print(e)
print("\nCopy whats INSIDE the quotes\n")
end = 1
while end == 1:
    print("Once copied you may exit the console")
    input()
