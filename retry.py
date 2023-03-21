def main():
    while True:
        introduction()
        score = questions()
        results(score)
        retry = input("Do you want to take the test again? (y/n): ")
        if retry.lower() != "y":
            break
