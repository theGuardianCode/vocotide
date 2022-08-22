import time
from funcs import get_word
import schedule

def job():
    print("new word on the way")
    random_word, definitions = get_word()

    while len(definitions) == 0:
        random_word, definitions = get_word()

    with open("API/request.txt", 'w') as file:
        file.write(random_word + "\n")
        for i in range(len(definitions)):
            if i == len(definitions) - 1:
                file.write(definitions[i])
            else:
                file.write(definitions[i] + "\n")

if __name__ == "__main__":
    # schedule.every().day().at("08:00").do(generate)
    schedule.every(30).seconds.do(job)

    while True:
        schedule.run_pending()
        time.sleep(1)
