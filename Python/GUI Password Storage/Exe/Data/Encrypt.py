def encrypt(phrase):        
    
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
        
        hexa = {
            "A":40,
            "B":1,
            "C":91,
            "D":42,
            "E":22,
            "F":72,
            "G":9,
            "H":61,
            "I":56,
            "J":63,
            "K":29,
            "L":0,
            "M":81,
            "N":62,
            "O":71,
            "P":73,
            "Q":52,
            "R":19,
            "S":3,
            "T":17,
            "U":2,
            "V":18,
            "W":7,
            "X":69,
            "Y":78,
            "Z":67,
            "a":33,
            "b":76,
            "c":44,
            "d":37,
            "e":58,
            "f":20,
            "g":8,
            "h":24,
            "i":77,
            "j":23,
            "k":4,
            "l":55,
            "m":49,
            "n":48,
            "o":27,
            "p":13,
            "q":14,
            "r":16,
            "s":79,
            "t":12,
            "u":80,
            "v":5,
            "w":6,
            "x":39,
            "y":89,
            "z":90,
            "1":15,
            "2":21,
            "3":51,
            "4":60,
            "5":34,
            "6":53,
            "7":85,
            "8":36,
            "9":88,
            "0":32,
            "-":43,
            "=":41,
            "[":65,
            "]":25,
            "\\":74,
            ";":83,
            "'":26,
            ",":50,
            ".":66,
            "/":82,
            "!":35,
            "@":68,
            "#":70,
            "$":64,
            "%":84,
            "^":54,
            "&":57,
            "*":11,
            "(":30,
            ")":10,
            "_":46,
            "+":31,
            "{":75,
            "}":59,
            "|":28,
            ":":87,
            "<":45,
            ">":38,
            "?":86,
            " ":47,
            }
        
        rehexa = {
            40:"A",
            1:"B",
            91:"C",
            42:"D",
            22:"E",
            72:"F",
            9:"G",
            61:"H",
            56:"I",
            63:"J",
            29:"K",
            0:"L",
            81:"M",
            62:"N",
            71:"O",
            73:"P",
            52:"Q",
            19:"R",
            3:"S",
            17:"T",
            2:"U",
            18:"V",
            7:"W",
            69:"X",
            78:"Y",
            67:"Z",
            33:"a",
            76:"b",
            44:"c",
            37:"d",
            58:"e",
            20:"f",
            8:"g",
            24:"h",
            77:"i",
            23:"j",
            4:"k",
            55:"l",
            49:"m",
            48:"n",
            27:"o",
            13:"p",
            14:"q",
            16:"r",
            79:"s",
            12:"t",
            80:"u",
            5:"v",
            6:"w",
            39:"x",
            89:"y",
            90:"z",
            15:"1",
            21:"2",
            51:"3",
            60:"4",
            34:"5",
            53:"6",
            85:"7",
            36:"8",
            88:"9",
            32:"0",
            43:"-",
            41:"=",
            65:"[",
            25:"]",
            74:"\\",
            83:";",
            26:"'",
            50:",",
            66:".",
            82:"/",
            35:"!",
            68:"@",
            70:"#",
            64:"$",
            84:"%",
            54:"^",
            57:"&",
            11:"*",
            30:"(",
            10:")",
            46:"_",
            31:"+",
            75:"{",
            59:"}",
            28:"|",
            87:":",
            45:"<",
            38:">",
            86:"?",
            47:" ",
            }        
        
        data = ""
        
        for cipher in phrase:
            
            #cipher key
            
            if cipher in "A" :
                data += "?jxE$"
            elif cipher in "B" :
                data += "B<KW6"
            elif cipher in "C" :
                data += ">;9*,"
            elif cipher in "D" :
                data += "pkK5I"
            elif cipher in "E" :
                data += "x_kU:"
            elif cipher in "F" :
                data += "ZPEFM"
            elif cipher in "G" :
                data += "j0hRX"
            elif cipher in "H" :
                data += "XG%ga"
            elif cipher in "I" :
                data += "/9-Eh"
            elif cipher in "J" :
                data += "0|I7)"
            elif cipher in "K" :
                data += "hPOy%"
            elif cipher in "L" :
                data += ")=m|)"
            elif cipher in "M" :
                data += "VZvN_"
            elif cipher in "N" :
                data += "e2P!y"
            elif cipher in "O" :
                data += "LA+!["
            elif cipher in "P" :
                data += "z%QiB"
            elif cipher in "Q" :
                data += "ZK<#t"
            elif cipher in "R" :
                data += "] <(C"
            elif cipher in "S" :
                data += "VKitA"
            elif cipher in "T" :
                data += "d, Zh"
            elif cipher in "U" :
                data += "Gp4.r"
            elif cipher in "V" :
                data += "m+<V="
            elif cipher in "W" :
                data += "uqG)^"
            elif cipher in "X" :
                data += "NjR'U"
            elif cipher in "Y" :
                data += "7aL|F"
            elif cipher in "Z" :
                data += "cu9s!"
            elif cipher in "a" :
                data += "a\\T7v"
            elif cipher in "b" :
                data += "|c13S"
            elif cipher in "c" :
                data += "M[)hQ"
            elif cipher in "d" :
                data += "b'{;l"
            elif cipher in "e" :
                data += "LE0Gi"
            elif cipher in "f" :
                data += "+2dkh"
            elif cipher in "g" :
                data += "Tt!wE"
            elif cipher in "h" :
                data += "xX3%4"
            elif cipher in "i" :
                data += ",W4zw"
            elif cipher in "j" :
                data += ">9OXm"
            elif cipher in "k" :
                data += "0]}Z#"
            elif cipher in "l" :
                data += "1AnIg"
            elif cipher in "m" :
                data += "mctCO"
            elif cipher in "n" :
                data += "c7<Ub"
            elif cipher in "o" :
                data += "k=n#9"
            elif cipher in "p" :
                data += "55h+4"
            elif cipher in "q" :
                data += ">rxSO"
            elif cipher in "r" :
                data += "9+^$n"
            elif cipher in "s" :
                data += "(-3_:"
            elif cipher in "t" :
                data += ";he0B"
            elif cipher in "u" :
                data += "y}Y!("
            elif cipher in "v" :
                data += "?%#T<"
            elif cipher in "w" :
                data += "GCK_}"
            elif cipher in "x" :
                data += "/^i|B"
            elif cipher in "y" :
                data += "2rqDo"
            elif cipher in "z" :
                data += "ASDX+"
            elif cipher in "1" :
                data += "+L2S'"
            elif cipher in "2" :
                data += "h-D7u"
            elif cipher in "3" :
                data += "0'1&w"
            elif cipher in "4" :
                data += "NomlK"
            elif cipher in "5" :
                data += "q+EWi"
            elif cipher in "6" :
                data += "Rh4<2"
            elif cipher in "7" :
                data += "sFNQo"
            elif cipher in "8" :
                data += "0nB:]"
            elif cipher in "9" :
                data += "84QxL"
            elif cipher in "0" :
                data += ";;bFy"
            elif cipher in "-" :
                data += "'!T^e"
            elif cipher in "=" :
                data += "<fU4e"
            elif cipher in "[" :
                data += "owKI*"
            elif cipher in "]" :
                data += ",1by*"
            elif cipher in "\\" :
                data += "81GIl"
            elif cipher in ";" :
                data += "bTI[b"
            elif cipher in "'" :
                data += "d2fL:"
            elif cipher in "," :
                data += "vm!^9"
            elif cipher in "." :
                data += "-ZWvI"
            elif cipher in "/" :
                data += "SQ@}a"
            elif cipher in "!" :
                data += ".UjHV"
            elif cipher in "@" :
                data += "0_/'4"
            elif cipher in "#" :
                data += "xUU\\."
            elif cipher in "$" :
                data += "_Z5j?"
            elif cipher in "%" :
                data += "]HDLC"
            elif cipher in "^" :
                data += "4KD%+"
            elif cipher in "&" :
                data += "v#z?#"
            elif cipher in "*" :
                data += "f|Fyk"
            elif cipher in "(" :
                data += "?W[>A"
            elif cipher in ")" :
                data += "/q\\&)"
            elif cipher in "_" :
                data += "zG|&>"
            elif cipher in "+" :
                data += "-Tbd8"
            elif cipher in "{" :
                data += "NE^,-"
            elif cipher in "}" :
                data += "BRv?d"
            elif cipher in "|" :
                data += ",ocw!"
            elif cipher in ":" :
                data += "iiDgM"
            elif cipher in "<" :
                data += "elt]@"
            elif cipher in ">" :
                data += "OXDqN"
            elif cipher in "?" :
                data += "UZ7)F"
            elif cipher in " " :
                data += "rJ^D*"                                  
                
            #cipher key  
        
        
        
        #base 
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
            lists[pos] = hexa[run]
        try:
            if lists[0] == 0:
                accept = 1
        except:
            pass
        leng = len(lists)
        for run in range(leng):
            total += int(lists[run])*(base1**(leng -1 - run))
        diff1 = len(str(total))
        
        #shuffle 
            
        lists = []
        for run in str(total):
            lists.append(run)
        for run in range(5):
            lists.insert(0, lists[-1])
            lists.pop(-1)
        total = int("".join(lists)) 
        diff2 = len(str(total))
            
        #conversion  
        
        special = []
        list2.insert(0, str(total%base2))
        q = total//base2
        while q >= base2:
            list2.insert(0, str(q%base2))
            q = q//base2
        list2.insert(0, str(q))    
        for run in range(len(list2)):
            pos = list2[run]
            list2[run] = rehexa[int(pos)]
        if diff1 - diff2 > 0:
            list2.append("`")
            list2.append(zero[diff1 - diff2])
        if accept == 1:
            list2.insert(0, "`")
            
                
        total = "".join(list2)
        


        #print("\n\n\n\n\n\n\n\n\nYour scrambled message is\n\n" + str(total))
    except(ValueError):
        print("\n\n\n\n\n\n\n\n\n\n\nError")
    
    return total


def decrypt(decipher):
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
        
        hexa = {
            "A":40,
            "B":1,
            "C":91,
            "D":42,
            "E":22,
            "F":72,
            "G":9,
            "H":61,
            "I":56,
            "J":63,
            "K":29,
            "L":0,
            "M":81,
            "N":62,
            "O":71,
            "P":73,
            "Q":52,
            "R":19,
            "S":3,
            "T":17,
            "U":2,
            "V":18,
            "W":7,
            "X":69,
            "Y":78,
            "Z":67,
            "a":33,
            "b":76,
            "c":44,
            "d":37,
            "e":58,
            "f":20,
            "g":8,
            "h":24,
            "i":77,
            "j":23,
            "k":4,
            "l":55,
            "m":49,
            "n":48,
            "o":27,
            "p":13,
            "q":14,
            "r":16,
            "s":79,
            "t":12,
            "u":80,
            "v":5,
            "w":6,
            "x":39,
            "y":89,
            "z":90,
            "1":15,
            "2":21,
            "3":51,
            "4":60,
            "5":34,
            "6":53,
            "7":85,
            "8":36,
            "9":88,
            "0":32,
            "-":43,
            "=":41,
            "[":65,
            "]":25,
            "\\":74,
            ";":83,
            "'":26,
            ",":50,
            ".":66,
            "/":82,
            "!":35,
            "@":68,
            "#":70,
            "$":64,
            "%":84,
            "^":54,
            "&":57,
            "*":11,
            "(":30,
            ")":10,
            "_":46,
            "+":31,
            "{":75,
            "}":59,
            "|":28,
            ":":87,
            "<":45,
            ">":38,
            "?":86,
            " ":47,
            }
        
        rehexa = {
            40:"A",
            1:"B",
            91:"C",
            42:"D",
            22:"E",
            72:"F",
            9:"G",
            61:"H",
            56:"I",
            63:"J",
            29:"K",
            0:"L",
            81:"M",
            62:"N",
            71:"O",
            73:"P",
            52:"Q",
            19:"R",
            3:"S",
            17:"T",
            2:"U",
            18:"V",
            7:"W",
            69:"X",
            78:"Y",
            67:"Z",
            33:"a",
            76:"b",
            44:"c",
            37:"d",
            58:"e",
            20:"f",
            8:"g",
            24:"h",
            77:"i",
            23:"j",
            4:"k",
            55:"l",
            49:"m",
            48:"n",
            27:"o",
            13:"p",
            14:"q",
            16:"r",
            79:"s",
            12:"t",
            80:"u",
            5:"v",
            6:"w",
            39:"x",
            89:"y",
            90:"z",
            15:"1",
            21:"2",
            51:"3",
            60:"4",
            34:"5",
            53:"6",
            85:"7",
            36:"8",
            88:"9",
            32:"0",
            43:"-",
            41:"=",
            65:"[",
            25:"]",
            74:"\\",
            83:";",
            26:"'",
            50:",",
            66:".",
            82:"/",
            35:"!",
            68:"@",
            70:"#",
            64:"$",
            84:"%",
            54:"^",
            57:"&",
            11:"*",
            30:"(",
            10:")",
            46:"_",
            31:"+",
            75:"{",
            59:"}",
            28:"|",
            87:":",
            45:"<",
            38:">",
            86:"?",
            47:" ",
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
        
        #base 
        
        for run in decipher:
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
            lists[pos] = hexa[run]
        leng = len(lists)
        for run in range(leng):
            total += int(lists[run])*(base1**(leng -1 - run))
            
                      
        #shuffle
        
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
        
        #conversion  
    
        special = []
        list2.insert(0, str(total%base2))
        q = total//base2
        while q >= base2:
            list2.insert(0, str(q%base2))
            q = q//base2
        list2.insert(0, str(q))
        for run in range(len(list2)):
            pos = list2[run]
            list2[run] = rehexa[int(pos)]
        if accept == 1:
            list2.insert(0, rehexa[0])
        total = "".join(list2)
        
        #decipher
        
        for run in total:
            store.append(run)
        for run in range(0,len(store),5):
            cipher.append(store[run] + store[run + 1] + store[run + 2] + store[run + 3] + store[run + 4])
        for decipher in range(len(cipher)):
            
            #decipher key
            
            if cipher[decipher] in "?jxE$" :
                data += "A"
            elif cipher[decipher] in "B<KW6" :
                data += "B"
            elif cipher[decipher] in ">;9*," :
                data += "C"
            elif cipher[decipher] in "pkK5I" :
                data += "D"
            elif cipher[decipher] in "x_kU:" :
                data += "E"
            elif cipher[decipher] in "ZPEFM" :
                data += "F"
            elif cipher[decipher] in "j0hRX" :
                data += "G"
            elif cipher[decipher] in "XG%ga" :
                data += "H"
            elif cipher[decipher] in "/9-Eh" :
                data += "I"
            elif cipher[decipher] in "0|I7)" :
                data += "J"
            elif cipher[decipher] in "hPOy%" :
                data += "K"
            elif cipher[decipher] in ")=m|)" :
                data += "L"
            elif cipher[decipher] in "VZvN_" :
                data += "M"
            elif cipher[decipher] in "e2P!y" :
                data += "N"
            elif cipher[decipher] in "LA+![" :
                data += "O"
            elif cipher[decipher] in "z%QiB" :
                data += "P"
            elif cipher[decipher] in "ZK<#t" :
                data += "Q"
            elif cipher[decipher] in "] <(C" :
                data += "R"
            elif cipher[decipher] in "VKitA" :
                data += "S"
            elif cipher[decipher] in "d, Zh" :
                data += "T"
            elif cipher[decipher] in "Gp4.r" :
                data += "U"
            elif cipher[decipher] in "m+<V=" :
                data += "V"
            elif cipher[decipher] in "uqG)^" :
                data += "W"
            elif cipher[decipher] in "NjR'U" :
                data += "X"
            elif cipher[decipher] in "7aL|F" :
                data += "Y"
            elif cipher[decipher] in "cu9s!" :
                data += "Z"
            elif cipher[decipher] in "a\\T7v" :
                data += "a"
            elif cipher[decipher] in "|c13S" :
                data += "b"
            elif cipher[decipher] in "M[)hQ" :
                data += "c"
            elif cipher[decipher] in "b'{;l" :
                data += "d"
            elif cipher[decipher] in "LE0Gi" :
                data += "e"
            elif cipher[decipher] in "+2dkh" :
                data += "f"
            elif cipher[decipher] in "Tt!wE" :
                data += "g"
            elif cipher[decipher] in "xX3%4" :
                data += "h"
            elif cipher[decipher] in ",W4zw" :
                data += "i"
            elif cipher[decipher] in ">9OXm" :
                data += "j"
            elif cipher[decipher] in "0]}Z#" :
                data += "k"
            elif cipher[decipher] in "1AnIg" :
                data += "l"
            elif cipher[decipher] in "mctCO" :
                data += "m"
            elif cipher[decipher] in "c7<Ub" :
                data += "n"
            elif cipher[decipher] in "k=n#9" :
                data += "o"
            elif cipher[decipher] in "55h+4" :
                data += "p"
            elif cipher[decipher] in ">rxSO" :
                data += "q"
            elif cipher[decipher] in "9+^$n" :
                data += "r"
            elif cipher[decipher] in "(-3_:" :
                data += "s"
            elif cipher[decipher] in ";he0B" :
                data += "t"
            elif cipher[decipher] in "y}Y!(" :
                data += "u"
            elif cipher[decipher] in "?%#T<" :
                data += "v"
            elif cipher[decipher] in "GCK_}" :
                data += "w"
            elif cipher[decipher] in "/^i|B" :
                data += "x"
            elif cipher[decipher] in "2rqDo" :
                data += "y"
            elif cipher[decipher] in "ASDX+" :
                data += "z"
            elif cipher[decipher] in "+L2S'" :
                data += "1"
            elif cipher[decipher] in "h-D7u" :
                data += "2"
            elif cipher[decipher] in "0'1&w" :
                data += "3"
            elif cipher[decipher] in "NomlK" :
                data += "4"
            elif cipher[decipher] in "q+EWi" :
                data += "5"
            elif cipher[decipher] in "Rh4<2" :
                data += "6"
            elif cipher[decipher] in "sFNQo" :
                data += "7"
            elif cipher[decipher] in "0nB:]" :
                data += "8"
            elif cipher[decipher] in "84QxL" :
                data += "9"
            elif cipher[decipher] in ";;bFy" :
                data += "0"
            elif cipher[decipher] in "'!T^e" :
                data += "-"
            elif cipher[decipher] in "<fU4e" :
                data += "="
            elif cipher[decipher] in "owKI*" :
                data += "["
            elif cipher[decipher] in ",1by*" :
                data += "]"
            elif cipher[decipher] in "81GIl" :
                data += "\\"
            elif cipher[decipher] in "bTI[b" :
                data += ";"
            elif cipher[decipher] in "d2fL:" :
                data += "'"
            elif cipher[decipher] in "vm!^9" :
                data += ","
            elif cipher[decipher] in "-ZWvI" :
                data += "."
            elif cipher[decipher] in "SQ@}a" :
                data += "/"
            elif cipher[decipher] in ".UjHV" :
                data += "!"
            elif cipher[decipher] in "0_/'4" :
                data += "@"
            elif cipher[decipher] in "xUU\\." :
                data += "#"
            elif cipher[decipher] in "_Z5j?" :
                data += "$"
            elif cipher[decipher] in "]HDLC" :
                data += "%"
            elif cipher[decipher] in "4KD%+" :
                data += "^"
            elif cipher[decipher] in "v#z?#" :
                data += "&"
            elif cipher[decipher] in "f|Fyk" :
                data += "*"
            elif cipher[decipher] in "?W[>A" :
                data += "("
            elif cipher[decipher] in "/q\\&)" :
                data += ")"
            elif cipher[decipher] in "zG|&>" :
                data += "_"
            elif cipher[decipher] in "-Tbd8" :
                data += "+"
            elif cipher[decipher] in "NE^,-" :
                data += "{"
            elif cipher[decipher] in "BRv?d" :
                data += "}"
            elif cipher[decipher] in ",ocw!" :
                data += "|"
            elif cipher[decipher] in "iiDgM" :
                data += ":"
            elif cipher[decipher] in "elt]@" :
                data += "<"
            elif cipher[decipher] in "OXDqN" :
                data += ">"
            elif cipher[decipher] in "UZ7)F" :
                data += "?"
            elif cipher[decipher] in "rJ^D*" :
                data += " "                         
                
            #decipher key
                
        
        #print("\n\n\n\n\n\n\n\nYour dechiper message is\n\n" + data)
    
    except:
        print("\n\n\n\n\n\n\nInvalid Message")
            
    return data