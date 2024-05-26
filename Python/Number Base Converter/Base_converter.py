hexa = {
    "A":10,
    "B":11,
    "C":12,
    "D":13,
    "E":14,
    "F":15,
    "G":16,
    "H":17,
    "I":18,
    "J":19,
    "K":20,
    "L":21,
    "M":22,
    "N":23,
    "O":24,
    "P":25,
    "Q":26,
    "R":27,
    "S":28,
    "T":29,
    "U":30,
    "V":31,
    "W":32,
    "X":33,
    "Y":34,
    "Z":35    
    }

rehexa = {
    10:"A",
    11:"B",
    12:"C",
    13:"D",
    14:"E",
    15:"F",
    16:"G",
    17:"H",
    18:"I",
    19:"J",
    20:"K",
    21:"L",
    22:"M",
    23:"N",
    24:"O",
    25:"P",
    26:"Q",
    27:"R",
    28:"S",
    29:"T",
    30:"U",
    31:"V",
    32:"W",
    33:"X",
    34:"Y",
    35:"Z"
    }

choice = input("For Conversion of Bases, input \"C\"\n                 OR\nFor Addition and subtraction of Bases, input \"AS\": ")
if choice == "C":
    print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
    print("If current base exceeds 36, insert commas between individual digits. Example--> 39,14,2,5 instead of 391425\nClick enter to continue.")
    input("")    
    while 1 == 1:
        print("")
        print("10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33 34 35")
        print("|  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |")
        print("A  B  C  D  E  F  G  H  I  J  K  L  M  N  O  P  Q  R  S  T  U  V  W  X  Y  Z\n")
        basenum = input("Enter the digits: ")
        base1 = int(input("Enter the current base: "))
        base2 = int(input("Enter the base you want to convert to: "))
        
        lists = []
        list2 = []
        special = []
        total = 0
        total1 = 0
        total2 = 0
        
        if base1 == 2 or base1 == 3 or base1 == 4 or base1 == 5 or base1 == 6 or base1 == 7 or base1 == 8 or base1 == 9 or base1 == 10:
            for run in basenum:
                lists += run
            leng = len(lists)
            for run in range(leng):
                total += int(lists[run])*(base1**(leng -1 - run))   
                        
        elif base1 > 36:
            lists = basenum.split(",")
            leng = len(lists)
            for run in lists:
                try:
                    int(run)
                except:
                    pos = lists.index(run)
                    lists[pos] = hexa[run]
            for run in range(leng):
                total += int(lists[run])*(base1**(leng -1 - run)) 
                
        else:
            for run in basenum:
                if run in hexa:
                    special += run
                lists += run
            for run in special:
                pos = lists.index(run)
                lists[pos] = hexa[run]
            leng = len(lists)
            for run in range(leng):
                total += int(lists[run])*(base1**(leng -1 - run))        
            
                
        #convertion 2
        special = []
        list2.insert(0, str(total%base2))
        q = total//base2
        while q >= base2:
            list2.insert(0, str(q%base2))
            q = q//base2
        list2.insert(0, str(q))
        if base2 > 36:
            print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\nAns:")
            print(list2)        
        elif base2 > 10:
            for run in list2:
                if int(run) > 9:
                    special.append(run)
            for run in special:
                pos = list2.index(run)
                list2[pos] = rehexa[int(run)]
            print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\nAns:" + "".join(list2))
        else:
            print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\nAns:" + "".join(list2))
            
            
#part 2

                
choice = "AS"        
if choice == "AS":
    print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
    print("If current base exceeds 36, insert commas between individual digits. Example--> 39,14,2,5 instead of 391425\nClick enter to continue.")
    input("")
    print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
    print("Advanced options will allow you to input different bases for different digits and ouput a different base.")
    while 1 == 1:
        print("")
        advop = input ("For advanced options input \"Y\" else \"N\": ")
        print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
        print("10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33 34 35")
        print("|  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |")
        print("A  B  C  D  E  F  G  H  I  J  K  L  M  N  O  P  Q  R  S  T  U  V  W  X  Y  Z\n")
        if advop == "Y":
            num1 = input("Enter the 1st digit: ")
            base1 = int(input("Enter the 1st base: "))
            num2 = input("Enter the 2nd digit: ")
            base2 = int(input("Enter the 2nd base: "))
            out = int(input("Choose what base you want to convert to: "))
            op = input("Choose your operator - or + : ")
        else:
            num1 = input("Enter the 1st digit: ")
            num2 = input("Enter the 2nd digit: ")
            base1 = int(input("Enter the base: "))
            op = input("Choose your operator - or + : ")
        
        lists = []
        list2 = []
        special = []
        total = 0
        total1 = 0
        total2 = 0        
        
        if base1 == 2 or base1 == 3 or base1 == 4 or base1 == 5 or base1 == 6 or base1 == 7 or base1 == 8 or base1 == 9 or base1 == 10:
            for run in num1:
                lists += run
            leng = len(lists)
            for run in range(leng):
                total1 += int(lists[run])*(base1**(leng -1 - run))
            lists = []
            
            if advop == "N":
                for run in num2:
                    lists += run
                leng = len(lists)
                for run in range(leng):
                    total2 += int(lists[run])*(base1**(leng -1 - run))
                lists = []
                
                
                
        elif base1 > 36:
            lists = num1.split(",")
            leng = len(lists)
            for run in lists:
                try:
                    int(run)
                except:
                    pos = lists.index(run)
                    lists[pos] = hexa[run]            
            for run in range(leng):
                total1 += int(lists[run])*(base1**(leng -1 - run))
            lists = []            
                
            if advop == "N":
                lists = num2.split(",")
                leng = len(lists)
                for run in lists:
                    try:
                        int(run)
                    except:
                        pos = lists.index(run)
                        lists[pos] = hexa[run]                
                for run in range(leng):
                    total2 += int(lists[run])*(base1**(leng -1 - run))
                lists = []        
                    
                 
                    
        else:
            for run in num1:
                if run in hexa:
                    special += run
                lists += run
            for run in special:
                pos = lists.index(run)
                lists[pos] = hexa[run]
            leng = len(lists)
            for run in range(leng):
                total1 += int(lists[run])*(base1**(leng -1 - run))
            lists = []
            special = []
            
            if advop == "N":
                for run in num2:
                    if run in hexa:
                        special += run
                    lists += run
                for run in special:
                    pos = lists.index(run)
                    lists[pos] = hexa[run]
                leng = len(lists)
                for run in range(leng):
                    total2 += int(lists[run])*(base1**(leng -1 - run))
                lists = []
                special = []       
                
                
                    
        if advop == "Y":       
            if base2 == 2 or base2 == 3 or base2 == 4 or base2 == 5 or base2 == 6 or base2 == 7 or base2 == 8 or base2 == 9 or base2 == 10:
                for run in num2:
                    lists += run
                leng = len(lists)
                for run in range(leng):
                    total2 += int(lists[run])*(base2**(leng -1 - run))   
                    
            elif base2 > 36:
                lists = num2.split(",")
                leng = len(lists)
                for run in lists:
                    try:
                        int(run)
                    except:
                        pos = lists.index(run)
                        lists[pos] = hexa[run]                
                for run in range(leng):
                    total2 += int(lists[run])*(base2**(leng -1 - run))                     
            
            else:
                for run in num2:
                    if run in hexa:
                        special += run
                    lists += run
                for run in special:
                    pos = lists.index(run)
                    lists[pos] = hexa[run]
                leng = len(lists)
                for run in range(leng):
                    total2 += int(lists[run])*(base2**(leng -1 - run))
                            
                
                                                  
        if op == "+":
            total = total1 + total2
        else:
            if total1 > total2:
                total = total1 - total2
            else:
                total = total2 - total1
                
                
    
    
    #conversion
        if advop == "Y":
            special = []
            list2.insert(0, str(total%out))
            q = total//out
            while q >= out:
                list2.insert(0, str(q%out))
                q = q//out
            list2.insert(0, str(q))
            if out > 36:
                print("\\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\nAns:")
                print(list2)            
            elif out > 10:
                for run in list2:
                    if int(run) > 9:
                        special.append(run)
                for run in special:
                    pos = list2.index(run)
                    list2[pos] = rehexa[int(run)]
                print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\nAns:" + "".join(list2))
            else:
                print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\nAns:" + "".join(list2))
                
                
                
        else:
            special = []
            list2.insert(0, str(total%base1))
            q = total//base1
            while q >= base1:
                list2.insert(0, str(q%base1))
                q = q//base1
            list2.insert(0, str(q))
            if base1 > 36:
                print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\nAns:")
                print(list2)             
            elif base1 > 10:
                for run in list2:
                    if int(run) > 9:
                        special.append(run)
                for run in special:
                    pos = list2.index(run)
                    list2[pos] = rehexa[int(run)]
                print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\nAns:" + "".join(list2))
            else:    
                print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\nAns:" + "".join(list2))
                
                
#Creator ==> Well Wisher =)