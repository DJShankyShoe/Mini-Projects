global lists
global dirpath
lists = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', '1', '2', '3', '4', '5', '6', '7', '8', '9', '0', '-', '=', '[', ']', '\\\\', ';', "'", ',', '.', '/', '!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '_', '+', '{', '}', '|', ':', '<', '>', '?', ' ']
import random 
import os
dirpath = os.getcwd()
def cipher():
    global randoms
    randoms = []
    test = open(dirpath.replace("\\", "/").replace("C:", "") + "/Data/cipher.py", "w")
    test.write("def cipher(cipher):\n    data = \"\"\n")
    for run in range(len(lists)):
        letter1 = lists[random.randint(0, len(lists)-1)]
        letter2 = lists[random.randint(0, len(lists)-1)]
        letter3 = lists[random.randint(0, len(lists)-1)]
        letter4 = lists[random.randint(0, len(lists)-1)]
        letter5 = lists[random.randint(0, len(lists)-1)]
        while letter1 + letter2 + letter3 + letter4 + letter5 in randoms:
            letter1 = lists[random.randint(0, len(lists)-1)]
            letter2 = lists[random.randint(0, len(lists)-1)]
            letter3 = lists[random.randint(0, len(lists)-1)]
            letter4 = lists[random.randint(0, len(lists)-1)]
            letter5 = lists[random.randint(0, len(lists)-1)]
        randoms.append(letter1 + letter2 + letter3 + letter4 + letter5)
        if run == 0:
            let = "if"
        else:
            let = "elif"
        test.write("    " + let + " cipher in \"" + lists[run] + "\" :\n        data += \"" + letter1 + letter2 + letter3 + letter4 + letter5 + "\"" + "\n")
    test.write("    return data\n")
    test.close
def decipher():
    test = open(dirpath.replace("\\", "/").replace("C:", "") + "/Data/decipher.py", "w")
    test.write("def decipher(cipher,decipher):\n    data = \"\"\n")
    for run in range(len(lists)):
        if run == 0:
            let = "if"
        else:
            let = "elif"
        #test = open("decipher.py", "w")
        test.write("    " + let + " cipher[decipher] in \"" + randoms[run] + "\" :\n        data += \"" + lists[run] + "\"" + "\n")
    test.write("    return data\n")
    test.close
def hexa_rehexa():
    randoms = []
    test = open(dirpath.replace("\\", "/").replace("C:", "") + "/Data/hexa_rehexa.py", "w")
    test.write("hexa = {")
    for run in range(len(lists)):
        num = random.randint(0, len(lists)-1)
        while num in randoms:
            num = random.randint(0, len(lists)-1)
        randoms.append(num)
        #test = open("hexa_rehexa.py", "a")
        test.write("\n    \"" + lists[run] + "\":" + str(num) + ",")
    test.write("\n    }\n\n")
    test.close()
    test = open(dirpath.replace("\\", "/").replace("C:", "") + "/Data/hexa_rehexa.py", "a")
    test.write("rehexa = {")
    for run in range(len(lists)):   
        #test = open("hexa_rehexa.py", "a")
        test.write("\n    " + str(randoms[run]) + ":" + "\"" + lists[run] + "\",")
    test.write("\n    }")
    test.close()