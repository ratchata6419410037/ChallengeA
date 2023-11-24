import random

random_number = random.randint(1, 100)

while True:
    user_guess = int(input("ทายตัวเลข (1-100): "))

    if user_guess == random_number:
        print("ยินดีด้วยคุณทายถูก!")
        break
    elif user_guess < random_number:
        print("คุณทายผิด ตัวเลขที่ป้อนน้อยไป")
    else:
        print("คุณทายผิด ตัวเลขที่ป้อนมากไป")