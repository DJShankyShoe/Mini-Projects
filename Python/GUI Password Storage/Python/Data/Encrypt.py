def encrypt(phrase):  
    import cipher 
    import decipher
    import hexa_rehexa    
    data = ""
    try:
        zero = {
            1:"*",
            2:"D",
            3:"p",
            4:"#",
            5:":",
            6:"(",
            7:"%",
            8:"O",
            9:"n"
            }                      
        for tcipher in phrase:
            data += cipher.cipher(tcipher)                                
        special = []
        lists = []
        list2 = []
        total = 0
        accept = 0
        base1 = 92
        base2 = 91
        for run in data:
            lists += run
        for run in lists:
            pos = lists.index(run)
            lists[pos] = hexa_rehexa.hexa[run]
        try:
            if lists[0] == 0:
                accept = 1
        except:
            pass
        leng = len(lists)
        for run in range(leng):
            total += int(lists[run])*(base1**(leng -1 - run))
        diff1 = len(str(total))
        lists = []
        for run in str(total):
            lists.append(run)
        for run in range(5):
            lists.insert(0, lists[-1])
            lists.pop(-1)
        total = int("".join(lists)) 
        diff2 = len(str(total))
        special = []
        list2.insert(0, str(total%base2))
        q = total//base2
        while q >= base2:
            list2.insert(0, str(q%base2))
            q = q//base2
        list2.insert(0, str(q))    
        for run in range(len(list2)):
            pos = list2[run]
            list2[run] = hexa_rehexa.rehexa[int(pos)]
        if diff1 - diff2 > 0:
            list2.append("`")
            list2.append(zero[diff1 - diff2])
        if accept == 1:
            list2.insert(0, "`")  
        total = "".join(list2)
    except(ValueError):
        print("\n\n\n\n\n\n\n\n\n\n\nError")
    return total
def decrypt(phrase):
    import cipher 
    import decipher
    import hexa_rehexa    
    try:
        zero = {
            "*":1,
            "D":2,
            "p":3,
            "#":4,
            ":":5,
            "(":6,
            "%":7,
            "O":8,
            "n":9
            }        
        data = ""
        store = []
        cipher = []
        special = []
        lists = []
        list2 = []
        total = 0
        base1 = 91
        base2 = 92 
        upd = 0
        accept = 0
        for run in phrase:
            lists += run
        if "`" == lists[0]:
            lists.remove("`")
            accept = 1
        if "`" in lists:
            lists.remove("`")
            upd = zero[lists[-1]]
            lists.pop()
        for run in lists:
            pos = lists.index(run)
            lists[pos] = hexa_rehexa.hexa[run]
        leng = len(lists)
        for run in range(leng):
            total += int(lists[run])*(base1**(leng -1 - run))
        lists = []
        for run in str(total):
            lists.append(run)
        if upd > 0:
            for run in range(upd):
                lists.append(str(0))
        for run in range(5 - upd):
            lists.append(lists[0])
            lists.pop(0)
        total = int("".join(lists))       
        special = []
        list2.insert(0, str(total%base2))
        q = total//base2
        while q >= base2:
            list2.insert(0, str(q%base2))
            q = q//base2
        list2.insert(0, str(q))
        for run in range(len(list2)):
            pos = list2[run]
            list2[run] = hexa_rehexa.rehexa[int(pos)]
        if accept == 1:
            list2.insert(0, hexa_rehexa.rehexa[0])
        total = "".join(list2)
        for run in total:
            store.append(run)
        for run in range(0,len(store),5):
            cipher.append(store[run] + store[run + 1] + store[run + 2] + store[run + 3] + store[run + 4])
        for tdecipher in range(len(cipher)):
            data += decipher.decipher(cipher,tdecipher)                         
    except ZeroDivisionError:
        print("\n\n\n\n\n\n\nInvalid Message")
    return data