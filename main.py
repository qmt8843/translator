import re

#Function to get user input without extra spaces
def user_input(request):
    text = input(request)
    text.strip()
    return text

#Function checks for suffix mutations to words (i.e., s, ed, est, ly, ect.)
def replace_simple_ending(text):
    with open("./ending.txt") as ending_file: 
        ending_lines = ending_file.readlines()
        for end in ending_lines:
            end_tokens = end.split("|")
            end_rg1 = fr"\B{end_tokens[0].strip()}\b"
            end_rg2 = fr"{end_tokens[1].strip()}"
            text = re.sub(end_rg1, end_rg2, text, flags=re.IGNORECASE)

#Function translates ownership noun and conjugates word following it
def replace_ownership(text, current):
    with open("./ownership.txt") as owner_file:
        owner_lines = owner_file.readlines()
        for line in owner_lines:
            owner_tokens = line.strip().split("|")
            print(owner_tokens)
            owner_rg1 = fr"{owner_tokens[0].strip()} ({current})\b" 
            text = re.sub(owner_rg1, rf"\1{owner_tokens[1].strip()}", text, flags=re.IGNORECASE)

def regex_function(text):
    #This function coverts each word (with a translation) in text with its counterpart
    #English words are put in english.txt
    #Non-english words (Naumarian) are put in non.txt
    #Any regex for smartly regocnizing changed to root words is held withing this function
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
                if english_lines[index] != '#' and non_lines[index] != '#': #Allows for comments within word text documents
                    english_regex = fr"\b{english_lines[index].strip()}\b"
                    non_regex = fr"{non_lines[index].strip()}"
                    replace_ownership(converted_text, english_lines[index].strip())
                    converted_text = re.sub(english_regex, non_regex, converted_text, flags=re.IGNORECASE)
                    replace_simple_ending(converted_text)
                    
                    
                    
    print("Output: ", converted_text, "\n")

def add_word():
    #This function adds a word and its translation to their appropriate files
    english = user_input("Enter new English word: ")
    if english.lower() == "quit" or english.lower() == "q" or english.lower() == "exit":
        print("Quitting...\n")
        return 0
    non = user_input("Enter Naumarian word: ")
    if non.lower() == "quit" or non.lower() == "q" or non.lower() == "exit":
        print("Quitting...\n")
        return 0
    with open("./english.txt") as english_file:
        lines = english_file.readlines()
        lines[0] = int(lines[0])+1
        new =  english
        english_file.write(new)
    with open("./non.txt") as non_file:
        lines = non_file.readlines()
        lines[0] = int(lines[0])+1
        new = non
        english_file.write(new)
    print("Word added!\n")
    return 1

def main():
    while(True):
        print("Make a choice:\n1. Translate\n2. Add word")
        choice = user_input(">>")
        if(choice == "1"):
            text = user_input("Type a sentence in English: ")
            regex_function(text)
        elif(choice == "2"):
            add_word()
        elif(choice.lower() == "quit" or choice.lower() == "q" or choice.lower() == "exit"):
            print("Quitting...")
            break
        else:
            print('\033[31m'+"Invalid choice!\n"+'\033[0m')

if __name__ == "__main__":
    main()