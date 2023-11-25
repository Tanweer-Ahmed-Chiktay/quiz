print("--------Quiz---------")

play = input("Would you like to continue to the game: (yes/no)")

if play != "yes":
    quit()

print("Let's Start")

questions = ["Who was the president of South Africa in 2022? ", "Who was the president of the United States in 2021? ", "In which country is Cape Town? ", "Which electric car company made the Model X? ", "Which mountain is Cape Town famous for? "]
answers = ["Cyril Ramaphosa", "Joe Biden", "South Africa", "Tesla", "Table Mountain"]

for x in range(len(questions)):
    user_ans = input(questions[x])
    if user_ans == answers[x]:
        print("Correct")
    else:
        print("Incorrect. The correct answer is " + answers[x])



