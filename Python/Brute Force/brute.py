import time

caps = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
non_caps = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
common_chara = ['!','@','#','$','%','&','*','?']
uncommon_chara = ['-','+','[',']','\\',':',';','"','\'','<',',','>','.','/','(',')','~','`','^',]

select = [caps,non_caps,numbers,common_chara,uncommon_chara]

pos1 = -1
pos2 = 0
pos3 = 0
pos4 = 0
pos5 = 0
pos6 = 0
pos7 = 0
pos8 = 0
pos9 = 0
pos10 = 0
pos11 = 0
pos12 = 0
pos13 = 0
pos14 = 0

num2 = 0
num3 = 0
num4 = 0
num5 = 0
num6 = 0
num7 = 0
num8 = 0
num9 = 0
num10 = 0
num11 = 0
num12 = 0
num13 = 0
num14 = 0

print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\nWelcome to password generator. This password generator creates all possible password types.\nIf you wish to obtain common password list, you can visit the site --> https://github.com/danielmiessler/SecLists/tree/master/Passwords\n\n\n\n\n")
print("Key in the password length range. Maximum password length is 14. Few examples are shown below.\n**NOTE, The smaller the range, humongous amount of time and space is conserved**\n\nIf password length range is between 1 to 8, key in --> 1,8\nIf you know the exact password range which you think is 6, key in --> 6,6")

pass_range = input("Input password length range: ")
pass_range = pass_range.split(",")

if int(pass_range[0]) < 1 or int(pass_range[0]) > int(pass_range[1]) or int(pass_range[1]) > 14:
    print("\n\n\n\nInvalid password range")
else:
    print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n1.Create personalized password character list\n2.Choose from given password character options\n")
    user = input("Select an option 1 or 2: ")
    if user == "1":
        print("\n\n\n\n\n\\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\nKey in you characterized password. The length of characters can't be lesser than " + pass_range[1] + ". An example are shown below\n**NOTE, The smaller the length of chracters, humongous amount of time and space is conserved**\n\nIf you think that characters \"$etinaD\" are involved key in $etinaD")
        chara = input("> ")
        if len(chara) < int(pass_range[1]):
            print("Invalid password length")
        else:
            pass_list1 = []
            pass_list0 = []
            for char in chara:
                pass_list1.append(char)
            pass_list0 = [''] + pass_list1
            pass_list = [pass_list0, pass_list1]
    elif user == "2":
        print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\nMore than 1 option can be selected\n**NOTE, The lesser the amount of options you select, humongous amount of time and space is conserved**\n\n")
        print("1.Captial Letters\n2.Non-Captial Letters\n3.Numbers\n4.Common Characters e.g --> !@$\n5.Uncommon Characters e.g --> *^~\n\n")
        option = input("e.g (If you wish to select option 2 and 3, key in 23)\nSelect Option(s): ")
        pass_list1 = []
        pass_list0 = []        
        for run in option:
            pass_list1 += select[int(run) -1]
        pass_list0 = [''] + pass_list1
        pass_list = [pass_list0, pass_list1]   
    else:
        print("invalid option")

file = open("pass_data.txt", "w")

sum = 0
size = 0
temp = 0


for run in range(int(pass_range[0]) - 1, int(pass_range[1])):
    sum += len(pass_list1)*len(pass_list1)**run
    temp = len(pass_list1)*len(pass_list1)**run
    size += temp*(run+1)
size += sum*2

for run in range(2,int(pass_range[0]) + 1):
    temp = "num" + str(run)
    exec("%s = %d" % (temp,1))

input("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\nNumber of passwords generating: " + str(sum) + "\n\nEstimated time till completion (Based on average computer speed)\nSeconds: " + str(round(sum/600000,3)) + "\nMinutes: " + str(round((sum/600000)/60,3)) + "\nHours: " + str(round((sum/600000)/3600,3)) + "\nDays: " + str(round((sum/600000)/86400,3)) + "\nMonths: " + str(round((sum/600000)/2592000,3)) + "\nYears: " + str(round((sum/600000)/31104000,3)) + "\n\nRequired Space\nSize in Kb: " + str(round(size/1000,3)) + "\nSize in Mb: " + str(round(size/1000000,3)) + "\nSize in GB: " + str(round(size/1000000000,3)) + "\n\nHit enter to continue")
#print(sum)
#print(size)
print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\nGenerating Password List..........")
start_time = time.time()

def brute():
    try:
        pos8 = 0
        pos9 += 1
        num8 = 1
        data = pass_list[num14][pos14] + pass_list[num13][pos13] + pass_list[num12][pos12] + pass_list[num11][pos11] + pass_list[num10][pos10] + pass_list[num9][pos9] + pass_list[num8][pos8] + pass_list[num7][pos7] + pass_list[num6][pos6] + pass_list[num5][pos5] + pass_list[num4][pos4] + pass_list[num3][pos3] + pass_list[num2][pos2] + pass_list[1][pos1]
    except:
        try:
            pos9 = 0
            pos10 += 1
            num0 = 1
            data = pass_list[num14][pos14] + pass_list[num13][pos13] + pass_list[num12][pos12] + pass_list[num11][pos11] + pass_list[num10][pos10] + pass_list[num9][pos9] + pass_list[num8][pos8] + pass_list[num7][pos7] + pass_list[num6][pos6] + pass_list[num5][pos5] + pass_list[num4][pos4] + pass_list[num3][pos3] + pass_list[num2][pos2] + pass_list[1][pos1]
        except:
            try:
                pos10 = 0
                pos11 += 1
                num10 = 1
                data = pass_list[num14][pos14] + pass_list[num13][pos13] + pass_list[num12][pos12] + pass_list[num11][pos11] + pass_list[num10][pos10] + pass_list[num9][pos9] + pass_list[num8][pos8] + pass_list[num7][pos7] + pass_list[num6][pos6] + pass_list[num5][pos5] + pass_list[num4][pos4] + pass_list[num3][pos3] + pass_list[num2][pos2] + pass_list[1][pos1]
            except:
                try:
                    pos11 = 0
                    pos12 += 1
                    num11 = 1
                    data = pass_list[num14][pos14] + pass_list[num13][pos13] + pass_list[num12][pos12] + pass_list[num11][pos11] + pass_list[num10][pos10] + pass_list[num9][pos9] + pass_list[num8][pos8] + pass_list[num7][pos7] + pass_list[num6][pos6] + pass_list[num5][pos5] + pass_list[num4][pos4] + pass_list[num3][pos3] + pass_list[num2][pos2] + pass_list[1][pos1]
                except:
                    try:
                        pos12 = 0
                        pos13 += 1
                        num12 = 1
                        data = pass_list[num14][pos14] + pass_list[num13][pos13] + pass_list[num12][pos12] + pass_list[num11][pos11] + pass_list[num10][pos10] + pass_list[num9][pos9] + pass_list[num8][pos8] + pass_list[num7][pos7] + pass_list[num6][pos6] + pass_list[num5][pos5] + pass_list[num4][pos4] + pass_list[num3][pos3] + pass_list[num2][pos2] + pass_list[1][pos1]
                    except:
                        pos13 = 0
                        pos14 += 1
                        num13 = 1
                        data = pass_list[num14][pos14] + pass_list[num13][pos13] + pass_list[num12][pos12] + pass_list[num11][pos11] + pass_list[num10][pos10] + pass_list[num9][pos9] + pass_list[num8][pos8] + pass_list[num7][pos7] + pass_list[num6][pos6] + pass_list[num5][pos5] + pass_list[num4][pos4] + pass_list[num3][pos3] + pass_list[num2][pos2] + pass_list[1][pos1]



for num in range(sum):
    try:
        pos1+=1
        data = pass_list[num14][pos14] + pass_list[num13][pos13] + pass_list[num12][pos12] + pass_list[num11][pos11] + pass_list[num10][pos10] + pass_list[num9][pos9] + pass_list[num8][pos8] + pass_list[num7][pos7] + pass_list[num6][pos6] + pass_list[num5][pos5] + pass_list[num4][pos4] + pass_list[num3][pos3] + pass_list[num2][pos2] + pass_list[1][pos1]
    except:
        try:
            pos1 = 0
            pos2 += 1
            data = pass_list[num14][pos14] + pass_list[num13][pos13] + pass_list[num12][pos12] + pass_list[num11][pos11] + pass_list[num10][pos10] + pass_list[num9][pos9] + pass_list[num8][pos8] + pass_list[num7][pos7] + pass_list[num6][pos6] + pass_list[num5][pos5] + pass_list[num4][pos4] + pass_list[num3][pos3] + pass_list[num2][pos2] + pass_list[1][pos1]
        except:
            try:
                pos2 = 0
                pos3 += 1
                num2 = 1
                data = pass_list[num14][pos14] + pass_list[num13][pos13] + pass_list[num12][pos12] + pass_list[num11][pos11] + pass_list[num10][pos10] + pass_list[num9][pos9] + pass_list[num8][pos8] + pass_list[num7][pos7] + pass_list[num6][pos6] + pass_list[num5][pos5] + pass_list[num4][pos4] + pass_list[num3][pos3] + pass_list[num2][pos2] + pass_list[1][pos1]
            except:
                try:
                    pos3 = 0   
                    pos4 += 1
                    num3 = 1
                    data = pass_list[num14][pos14] + pass_list[num13][pos13] + pass_list[num12][pos12] + pass_list[num11][pos11] + pass_list[num10][pos10] + pass_list[num9][pos9] + pass_list[num8][pos8] + pass_list[num7][pos7] + pass_list[num6][pos6] + pass_list[num5][pos5] + pass_list[num4][pos4] + pass_list[num3][pos3] + pass_list[num2][pos2] + pass_list[1][pos1]
                except:
                    try: 
                        pos4 = 0
                        pos5 += 1
                        num4 = 1
                        data = pass_list[num14][pos14] + pass_list[num13][pos13] + pass_list[num12][pos12] + pass_list[num11][pos11] + pass_list[num10][pos10] + pass_list[num9][pos9] + pass_list[num8][pos8] + pass_list[num7][pos7] + pass_list[num6][pos6] + pass_list[num5][pos5] + pass_list[num4][pos4] + pass_list[num3][pos3] + pass_list[num2][pos2] + pass_list[1][pos1]
                    except:
                        try:
                            pos5 = 0
                            pos6 += 1
                            num5 = 1
                            data = pass_list[num14][pos14] + pass_list[num13][pos13] + pass_list[num12][pos12] + pass_list[num11][pos11] + pass_list[num10][pos10] + pass_list[num9][pos9] + pass_list[num8][pos8] + pass_list[num7][pos7] + pass_list[num6][pos6] + pass_list[num5][pos5] + pass_list[num4][pos4] + pass_list[num3][pos3] + pass_list[num2][pos2] + pass_list[1][pos1]
                        except:
                            try:
                                pos6 = 0
                                pos7 += 1
                                num6 = 1
                                data = pass_list[num14][pos14] + pass_list[num13][pos13] + pass_list[num12][pos12] + pass_list[num11][pos11] + pass_list[num10][pos10] + pass_list[num9][pos9] + pass_list[num8][pos8] + pass_list[num7][pos7] + pass_list[num6][pos6] + pass_list[num5][pos5] + pass_list[num4][pos4] + pass_list[num3][pos3] + pass_list[num2][pos2] + pass_list[1][pos1]
                            except:
                                try:
                                    pos7 = 0
                                    pos8 += 1
                                    num7 = 1
                                    data = pass_list[num14][pos14] + pass_list[num13][pos13] + pass_list[num12][pos12] + pass_list[num11][pos11] + pass_list[num10][pos10] + pass_list[num9][pos9] + pass_list[num8][pos8] + pass_list[num7][pos7] + pass_list[num6][pos6] + pass_list[num5][pos5] + pass_list[num4][pos4] + pass_list[num3][pos3] + pass_list[num2][pos2] + pass_list[1][pos1]
                                except:
                                    brute()
                                #
                            #
                        #
                    #
                #
            #
        #
    #
                                            
    file.write(data + "\n")
    # print(data)
    
end_time = time.time()
    
def time_convert(sec):
    mins = sec // 60
    sec = sec % 60
    hours = mins // 60
    mins = mins % 60
    print("Time Lapsed = {0}:{1}:{2}".format(int(hours),int(mins),sec))

print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\nCompleted")
time_convert(end_time - start_time)