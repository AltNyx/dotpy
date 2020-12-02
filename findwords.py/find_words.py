constrain_list = {}
letter_dict = {}


def wordList(word_len):
    file_object = open("english3.txt", 'r')
    return [line.strip('\n') for line in file_object if len(line.strip('\n')) == word_len]

def checkLetterPos(word):
    for index, letter in list(letter_dict.items()):
        if word[index] != letter:
            return False
    return True

def checkWord(word):
    for letter in word:
        if letter not in constrain_list:
            return False
    return True

def findWords():
    n = int(input("Enter length of word:"))
    print("Enter ith letter (type '0' to skip)")
    for i in range(1, n + 1):
        letter_dict[i - 1] = input(f"Enter {i} letter:")
    
    for key, value in list(letter_dict.items()):
        if value == '0':
            del letter_dict[key]

    letter = None
    print("Enter letters the word should contain (type '0' to skip)")
    while letter != '0':
        letter = input("Enter letter:")
        constrain_list[letter] = 1
    del constrain_list['0'] # to remove the '0'

    #adding positional letters also to constraint list
    for value in letter_dict.values():
        constrain_list[key] = 1

    all_words = wordList(n)

    #words that contain letter at the right position
    filtered_list = []
    for word in all_words:
        if checkLetterPos(word):
            filtered_list.append(word)
    
    #removing words that do not contain the specified letters
    return list(filter(checkWord, filtered_list))

def main():
    print(findWords())

if __name__ == "__main__":
    main()
    

