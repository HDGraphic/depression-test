    for question in questions:
        print(question)
        answer = input("Enter your answer (0-3): ")
        if not answer.isdigit() or int(answer) not in [0, 1, 2, 3]:
            print("Invalid answer. The program will now terminate.")
            exit()
        else:
            answers.append(int(answer))
            score += int(answer)
    
    return score
