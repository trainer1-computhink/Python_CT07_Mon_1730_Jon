# print("Hello from lesson 3")

# import time

# for i in range(10, 0, -1):
#     print(i)
#     time.sleep(1)

# print("liftoff!")

# ## Task 3: Multiplication Quiz
# **Task: Ms Tan, your math teacher knows that you are a
# programming whiz,
# she has asked you to help code a multiplication quiz for
# the class to practice.**

# Here are her requirements:
# 1. Students have to answer 15 questions in total
# 2. Students have 3 lives (chances). i.e. they can get the
#    question wrong 3 times.
# 3. The questions will be in this format: "What is 3 x 19? ". 
# 4. The numbers for each question will be randomly generated
#    and between the range of 2 to 20.
# 5. If the student answers correctly, move on to the next
#    question
# 6. If the student answers wrongly, minus 1 life, and ask
#     the question again.
# 7. If the student has no more lives, exit and print
#     "GO AND SEE MS TAN FOR REMEDIAL"
import random

# variable type
# string: "abc"
# int: whole number
# float: decimal

no_of_qns = 5
no_of_lives = 3

# for loop: is for those situation whereby we know how many times to repeat
# while loop: is for those situation whereby we only know the condition to stop repeating


for i in range(no_of_qns):
    num1 = random.randint(2,20) #variable type : int
    num2 = random.randint(2,20) #variable type : int 
    correct_ans = num1 * num2
    answer = 0
    # ask the question
    while answer != correct_ans:
        print("no of lives = " + str(no_of_lives))
        answer = int(input("What is " + str(num1) + " x " + str(num2) + "? :"))
        if answer != correct_ans:
            no_of_lives -= 1
        if no_of_lives == 0:
            break

    if no_of_lives == 0:
        print("GO AND SEE MS TAN FOR REMEDIAL")
        break

# print("All correct with " + str(no_of_lives) + " left")


