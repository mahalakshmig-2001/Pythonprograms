from question import Question

question_prompt = [
    "What color is apple? \n a)Red \n b)Orange \n c)Yellow",
    "What color is Banana? \n a)Pink \n b)Orange \n c)Yellow",
    "What color is Strawberry? \n a)Green \n b)Red \n c)Yellow",
]

questions = [
   Question(question_prompt[0], "a"),
   Question(question_prompt[1], "c"),
   Question(question_prompt[2], "b")
]


def run(questions):
    score = 0
    for question in questions:
        answer = input(question.prompt)
        if answer == question.answer:
            score += 1
    print("you got " + str(score) + "/" + str(len(questions)) + "correct")


run(questions)