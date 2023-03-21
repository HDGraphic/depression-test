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
