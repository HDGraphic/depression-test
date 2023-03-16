for question in questions:
    print(question)
    answer = input("Enter your answer (0-3): ")
    while not answer.isdigit() or int(answer) not in [0, 1, 2, 3]:
        answer = input("Invalid answer. Please enter a number from 0 to 3: ")
    answers.append(int(answer))
