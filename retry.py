def main():
    while True:
        introduction()
        score = questions()
        results(score)
        retry = input("Do you want to take the test again? (y/n): ")
        while retry.lower() not in ['y', 'n']:
            retry = input("Invalid input. Please enter 'y' to retry or 'n' to exit: ")
        if retry.lower() == 'n':
            break
