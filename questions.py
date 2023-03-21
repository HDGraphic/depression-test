def questions():
    questions = ["Little interest or pleasure in doing things?", 
             "Feeling down, depressed, or hopeless?", 
             "Trouble falling or staying asleep, or sleeping too much?", 
             "Feeling tired or having little energy?", 
             "Poor appetite or overeating?", 
             "Feeling bad about yourself - or that you are a failure or have let yourself or your family down?", 
             "Trouble concentrating on things, such as reading the newspaper or watching television?", 
             "Moving or speaking so slowly that other people could have noticed. Or the opposite - being so fidgety or restless that you have been moving around a lot more than usual?", 
             "Thoughts that you would be better off dead or of hurting yourself in some way?"]
    
    score = 0
    answers = []
    
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
