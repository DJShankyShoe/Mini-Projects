def decipher(cipher,decipher):
    data = ""
    if cipher[decipher] in "z{7Ge" :
        data += "A"
    elif cipher[decipher] in "7;V5e" :
        data += "B"
    elif cipher[decipher] in "-sESL" :
        data += "C"
    elif cipher[decipher] in "uk(N|" :
        data += "D"
    elif cipher[decipher] in ".3}pY" :
        data += "E"
    elif cipher[decipher] in "j]'[#" :
        data += "F"
    elif cipher[decipher] in "3aRDo" :
        data += "G"
    elif cipher[decipher] in "vS]LV" :
        data += "H"
    elif cipher[decipher] in "\\x]61" :
        data += "I"
    elif cipher[decipher] in "))_C-" :
        data += "J"
    elif cipher[decipher] in "75fmJ" :
        data += "K"
    elif cipher[decipher] in "kSvVn" :
        data += "L"
    elif cipher[decipher] in "@4_$j" :
        data += "M"
    elif cipher[decipher] in "B2'4b" :
        data += "N"
    elif cipher[decipher] in "[{/n|" :
        data += "O"
    elif cipher[decipher] in "m-fR>" :
        data += "P"
    elif cipher[decipher] in "sd68." :
        data += "Q"
    elif cipher[decipher] in "&b$lu" :
        data += "R"
    elif cipher[decipher] in "XJp6n" :
        data += "S"
    elif cipher[decipher] in "*#?i0" :
        data += "T"
    elif cipher[decipher] in "%B<pr" :
        data += "U"
    elif cipher[decipher] in "Tjga<" :
        data += "V"
    elif cipher[decipher] in "UK$+p" :
        data += "W"
    elif cipher[decipher] in "4ZtVy" :
        data += "X"
    elif cipher[decipher] in "f]#XJ" :
        data += "Y"
    elif cipher[decipher] in "y[D'3" :
        data += "Z"
    elif cipher[decipher] in "WO8qB" :
        data += "a"
    elif cipher[decipher] in "_#)^@" :
        data += "b"
    elif cipher[decipher] in "UN3Cw" :
        data += "c"
    elif cipher[decipher] in "-/x*K" :
        data += "d"
    elif cipher[decipher] in "^>QSO" :
        data += "e"
    elif cipher[decipher] in "+'9Vf" :
        data += "f"
    elif cipher[decipher] in "%z?n>" :
        data += "g"
    elif cipher[decipher] in "5o97!" :
        data += "h"
    elif cipher[decipher] in " jJRT" :
        data += "i"
    elif cipher[decipher] in "}3^6J" :
        data += "j"
    elif cipher[decipher] in "O-uF]" :
        data += "k"
    elif cipher[decipher] in "nDeZA" :
        data += "l"
    elif cipher[decipher] in "(?A+7" :
        data += "m"
    elif cipher[decipher] in "w7mqU" :
        data += "n"
    elif cipher[decipher] in "3z\\20" :
        data += "o"
    elif cipher[decipher] in "dKDD?" :
        data += "p"
    elif cipher[decipher] in "cW4M+" :
        data += "q"
    elif cipher[decipher] in "IpD|;" :
        data += "r"
    elif cipher[decipher] in "UT;l>" :
        data += "s"
    elif cipher[decipher] in "x@X\\Q" :
        data += "t"
    elif cipher[decipher] in "-q\\dY" :
        data += "u"
    elif cipher[decipher] in "<J<UH" :
        data += "v"
    elif cipher[decipher] in "} )z!" :
        data += "w"
    elif cipher[decipher] in "a&0@w" :
        data += "x"
    elif cipher[decipher] in "7M/fi" :
        data += "y"
    elif cipher[decipher] in "s.v*K" :
        data += "z"
    elif cipher[decipher] in "NeEp(" :
        data += "1"
    elif cipher[decipher] in "=5>$m" :
        data += "2"
    elif cipher[decipher] in "XH$>d" :
        data += "3"
    elif cipher[decipher] in "D$x5=" :
        data += "4"
    elif cipher[decipher] in "Z7%%!" :
        data += "5"
    elif cipher[decipher] in "jf.4/" :
        data += "6"
    elif cipher[decipher] in "5v5yq" :
        data += "7"
    elif cipher[decipher] in "D(gu$" :
        data += "8"
    elif cipher[decipher] in "l$?&W" :
        data += "9"
    elif cipher[decipher] in "6q]&L" :
        data += "0"
    elif cipher[decipher] in "cIqB{" :
        data += "-"
    elif cipher[decipher] in "0n2nM" :
        data += "="
    elif cipher[decipher] in "vwQj]" :
        data += "["
    elif cipher[decipher] in "oR9h=" :
        data += "]"
    elif cipher[decipher] in "/W.*N" :
        data += "\\"
    elif cipher[decipher] in "UX/(J" :
        data += ";"
    elif cipher[decipher] in "#OE@(" :
        data += "'"
    elif cipher[decipher] in "zNVk9" :
        data += ","
    elif cipher[decipher] in "B4ivH" :
        data += "."
    elif cipher[decipher] in "&Zw4X" :
        data += "/"
    elif cipher[decipher] in "1nfT%" :
        data += "!"
    elif cipher[decipher] in "+xZX$" :
        data += "@"
    elif cipher[decipher] in "1MN3 " :
        data += "#"
    elif cipher[decipher] in "d! #s" :
        data += "$"
    elif cipher[decipher] in "&=z7)" :
        data += "%"
    elif cipher[decipher] in "I9a/>" :
        data += "^"
    elif cipher[decipher] in "_P?CC" :
        data += "&"
    elif cipher[decipher] in "C|6Z:" :
        data += "*"
    elif cipher[decipher] in "oo!U_" :
        data += "("
    elif cipher[decipher] in "cvKu^" :
        data += ")"
    elif cipher[decipher] in "U[U6+" :
        data += "_"
    elif cipher[decipher] in "i!0wX" :
        data += "+"
    elif cipher[decipher] in "K@ngh" :
        data += "{"
    elif cipher[decipher] in "WV+0j" :
        data += "}"
    elif cipher[decipher] in "*{)#B" :
        data += "|"
    elif cipher[decipher] in "e;uAO" :
        data += ":"
    elif cipher[decipher] in "(97Aj" :
        data += "<"
    elif cipher[decipher] in "8p*oU" :
        data += ">"
    elif cipher[decipher] in "|LD&i" :
        data += "?"
    elif cipher[decipher] in "zAx07" :
        data += " "
    return data
