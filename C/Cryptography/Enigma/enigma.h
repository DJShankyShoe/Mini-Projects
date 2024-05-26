static char alpha[] =     {'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'};

static char rotor1[] =    {'E', 'S', 'O', 'V', 'P', 'Z', 'J', 'A', 'Y', 'Q', 'U', 'I', 'R', 'H', 'X', 'L', 'N', 'F', 'T', 'G', 'K', 'D', 'C', 'M', 'W', 'B'};
static char rotor2[] =    {'V', 'Z', 'B', 'R', 'G', 'I', 'T', 'Y', 'U', 'P', 'S', 'D', 'H', 'N', 'L', 'X', 'A', 'W', 'M', 'J', 'Q', 'O', 'F', 'E', 'C', 'K'};
static char rotor3[] =    {'J', 'P', 'G', 'V', 'O', 'U', 'M', 'F', 'Y', 'Q', 'B', 'E', 'N', 'H', 'Z', 'R', 'D', 'K', 'A', 'S', 'X', 'L', 'I', 'C', 'T', 'W'};
static char rotor4[] =    {'N', 'Z', 'J', 'H', 'G', 'R', 'C', 'X', 'M', 'Y', 'S', 'W', 'B', 'O', 'U', 'F', 'A', 'I', 'V', 'L', 'P', 'E', 'K', 'Q', 'D', 'T'};
static char rotor5[] =    {'F', 'K', 'Q', 'H', 'T', 'L', 'X', 'O', 'C', 'B', 'J', 'S', 'P', 'D', 'Z', 'R', 'A', 'M', 'E', 'W', 'N', 'I', 'U', 'Y', 'G', 'V'};
static char reflector[] = {'R', 'D', 'O', 'B', 'J', 'N', 'T', 'K', 'V', 'E', 'H', 'M', 'L', 'F', 'C', 'W', 'Z', 'A', 'X', 'G', 'Y', 'I', 'P', 'S', 'U', 'Q'};


// Make sures the array position after offset shift is between 0-25
int posReturn(int a){
    if (a > 25){
        a = a - 26;
    } else if (a < 0){
        a = 26 + a;
    }
    return a;
}


char rotorMap(int offset[], char letter, char *rotor[])
{   
    int type = 0, setReverse = 0, offsetV, offsetA;
    char FLetter;

    // Adds offset by 1 everytime the function is called
    offset[2]++;
    if (offset[2] > 26){
        offset[2] = 0;
        offset[1]++;
    }

    if (offset[1] > 26){
        offset[1] = 0;
        offset[0]++;
    }

    if (offset[0] > 26){
        offset[0] = 0;
    }

    for (int t = 0; t < 7; t++){

        // Get offset value for the current rotor
        if (type == 3){
            offsetV = 0;
        } else{
            offsetV = offset[2-type];
        }

        // Modify mapping values according to offset (Front to Back)
        if (type == 0){
            offsetA = 0;
        } else {
            offsetA = offset[3 - type];
        }

        // Modify mapping values according to offset (Back to Front)
        for (int c = 0; c < 26; c++){
            if (letter == alpha[c]){
                FLetter = alpha[posReturn(c + offsetV)];
            }
        }

        // mapping chars according to rotor
        for (int i = 0; i < 26; i++){

            // Checks whether to map from (front to back) or (back to front)
            if (setReverse){

                // Gets the char position after offset shift (back to front)
                if (rotor[type][i] == FLetter){
                    letter = alpha[i];
                    //printf("%c %d %d %d\n", letter, offsetV, offsetA, type);
                    letter = alpha[posReturn(i - offsetV)];
                    break;
                } 

            } else {

                // Gets the char position after offset shift (front to back)
                if (alpha[posReturn(i + offsetA)] == letter){
                    letter = rotor[type][posReturn(i + offsetV)];
                    //printf("%c %d %d %d\n", letter, offsetV, offsetA, type);
                    break;
                }
            }
        }

        // get direction of rotor mapping (back to front) or (front to back)
        if (type == 3){
            setReverse = 1;
        } else if (type == 0){
            setReverse = 0;
        }

        // get which rotor to map to ("type" being the rotor)
        if (setReverse){
            type--;
        } else {
            type++;
        }
    
    }

    //printf("%c", letter);
    return letter;
}


char plugboardMap(char letter, char *plugboard){

    char MLetter = '\0';

    // Get Plugboard Mapping
    for (int x = 0; x < 13; x++){
        if (alpha[x] == letter){
            MLetter = plugboard[x];
            break;
        } else if (plugboard[x] == letter){
            MLetter = alpha[x];
            break;
        }
    }
    
    // If char deoesn't exists in plugboard mapping, return same char
    if (MLetter != '\0'){
        letter = MLetter;
    }

    // printf("%c", letter);
    return letter;
}


char* EnigmaCipher(char* text, int *rotorOffset, char *rotor[], char *plugboard){

    int *offset = malloc(sizeof(int) * 3);
    offset[0] = rotorOffset[0], offset[1] = rotorOffset[1], offset[2] = rotorOffset[2];

    char cipher[strlen(text)];

    // Plugboard -> Rotor -> Plugboard -> Output
    for (int i = 0; i < strlen(text); i++){
        cipher[i] = plugboardMap(text[i], plugboard);
        cipher[i] = rotorMap(offset, cipher[i], rotor);
        cipher[i] = plugboardMap(cipher[i], plugboard);
    }

    strncpy(text, cipher, strlen(text));
    free(offset);

    return text;
}
