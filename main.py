def introduction():
      print('-------------------------------------------------------------------------')
      print("              Welcome to the depression detection test")
      print('-------------------------------------------------------------------------')
      print('Please answer the following questions using a scale of 0 to 3, where:\n0 = Never, 1 = Several days, 2 = half the days or more, 3 = Almost every day.\n')

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
        while not answer.isdigit() or int(answer) not in [0, 1, 2, 3]:
            answer = input("Invalid answer. Please enter a valid number (0-3): ")
        answers.append(int(answer))
        score += int(answer)
    
    return score
        
            
def results(score):
    print(f"\nYour total score is {score}.")
    if score < 5:
        print("You have minimal symptoms of depression.")
    elif score < 10:
        print("You have mild symptoms of depression.")
    elif score < 15:
        print("You have moderate symptoms of depression.")
    else:
        print("You have severe symptoms of depression.") 

def main():
    while True:
        introduction()
        score = questions()
        results(score)
        retry = input("Do you want to take the test again? (y/n): ")
        if retry.lower() != "y":
            break
        
main()
