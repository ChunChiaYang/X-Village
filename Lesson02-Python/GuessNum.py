import random
answer = random.randint(1,100)
print(answer)
guess=int(input("Plz enter a number:"))

while guess!=answer:
    print("Input=",guess,"is not the answer")
    guess=int(input("Plz enter a number:"))
print("Input=",guess,"is equal to the answer")
