#1 /usr/bin/python3

from funcs import get_word

def job():
    print("job started");
    random_word, definitions = get_word()

    while len(definitions) == 0:
        random_word, definitions = get_word()
    
    print(f'Word: {random_word}')

    with open("./API/request.txt", 'w') as file:
        file.write(random_word + "\n")
        for i in range(len(definitions)):
            if i == len(definitions) - 1:
                file.write(definitions[i])
                print("wrote last line")
            else:
                file.write(definitions[i] + "\n")
                print("wrote to file")

if __name__ == "__main__":
    job()

# build and test docker image