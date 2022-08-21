from funcs import get_word

if __name__ == "__main__":
    random_word, definitions = get_word()

    if len(definitions) == 0:
        random_word, definitions = get_word()

    with open("request.txt", 'w') as file:
        file.write(random_word + "\n")
        for i in range(len(definitions)):
            if i == len(definitions) - 1:
                file.write(definitions[i])
            else:
                file.write(definitions[i] + "\n")