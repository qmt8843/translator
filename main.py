import re

#Function to get user input without extra spaces
def user_input(request):
    text = input(request)
    text.strip()
    return text

def regex_function(text):
    count = 0
    converted_text = text
    with open("./english.txt") as english_file:
        line_count = int(english_file.readline())
        english_lines = english_file.readlines()
        with open("./non.txt") as non_file:
            non_line_count = int(non_file.readline())
            if line_count != non_line_count:
                print("Translator files not synced!")
                return None
            non_lines = non_file.readlines()
            for index in range(line_count):
                converted_text = re.sub(english_lines[index].strip(), non_lines[index].strip(), converted_text, flags=re.IGNORECASE)

    print("Output:\n", converted_text)

def add_word():
    english = user_input("Enter new English word: ")
    non = user_input("Enter Naumarian word: ")
    with open("./english.txt") as english_file:
        lines = english_file.readlines()
        lines[0] = int(lines[0])+1
        new = "^"+english+"$"
        english_file.write(new)
    with open("./non.txt") as non_file:
        lines = non_file.readlines()
        lines[0] = int(lines[0])+1
        new = "^"+non+"$"
        english_file.write(new)
    print("Word added!")

def main():
    text = user_input("Type a sentence in English: ")
    regex_function(text)
    #add_word()

if __name__ == "__main__":
    main()