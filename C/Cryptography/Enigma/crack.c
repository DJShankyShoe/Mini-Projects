#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>

#include "enigma.h"

int arrLen = 20;


double IOC(char *text, double ioc){

    double count, len = strlen(text);
    ioc = 0;

    for (int i = 0; i < 26; i++){
        count = 0;
        for (int x = 0; x < len; x++){
            if (alpha[i] == text[x]){
                count ++;
            }
        }
        ioc += (count/len) * ((count - 1)/(len-1));
    }

    return ioc;
}


char** RotorBrute(char *text, char *finalRotor[]){

    char *rotorAll[] = {rotor1, rotor2, rotor3, rotor4, rotor5};
    char output[strlen(text)], *rotorCur[4], userInput[2];
    double iocVal;
    int userChoice;

    // 60 -> total number of possible rotor positions
    double IOCputNG[60];
    int IOCmapNG[60*3];

    // rotor configurations
    int rotorOffset[] = {0,0,0};
    static char plugbaord[] = {'\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0'}; // Configure plugbord mapping

    // I just learnt halfway that the value of text changes as it was being returned from the function EnigmaCipher thus i have to perform this step to store the orignal value of text
    char actualText[strlen(text)];
    strcpy(actualText, text);

    // generate all possible rotor positions x-z
    int r = 0;
    for (int x = 0; x < 5; x++){
        for (int y = 0; y < 5; y++){
             if (y != x){
                for (int z = 0; z < 5; z++){
                    if (z != x && z != y){

                        rotorCur[0] = rotorAll[x]; rotorCur[1] = rotorAll[y]; rotorCur[2] = rotorAll[z]; rotorCur[3] = reflector;
                        strcpy(output, EnigmaCipher(text, rotorOffset, rotorCur, plugbaord)); // Halfway, I learnt the value of text changes after calling EnigmaCipher as it return the parameter
                        iocVal = IOC(output, 0);

                        // Restoring value of text
                        strcpy(text, actualText);

                        IOCputNG[r] = iocVal;
                        IOCmapNG[r * 3 + 0] = x; IOCmapNG[r * 3 + 1] = y; IOCmapNG[r * 3 + 2] = z;

                        r++;
                    }
                }
             }
        }
    }

    // sorting IOC values by descending order
    double a;
    int b,c,d;

    for (int i = 0; i < 60; ++i) {
        for (int j = i + 1; j < 60; ++j) 
        {
            if (IOCputNG[i] < IOCputNG[j]) 
            {
                a = IOCputNG[i];
                IOCputNG[i] = IOCputNG[j];
                IOCputNG[j] = a;
                
                b = IOCmapNG[i * 3 + 0]; c = IOCmapNG[i * 3 + 1]; d = IOCmapNG[i * 3 + 2];
                IOCmapNG[i * 3 + 0] = IOCmapNG[j * 3 + 0]; IOCmapNG[i * 3 + 1] = IOCmapNG[j * 3 + 1]; IOCmapNG[i * 3 + 2] = IOCmapNG[j * 3 + 2];
                IOCmapNG[j * 3 + 0] = b; IOCmapNG[j * 3 + 1] = c; IOCmapNG[j * 3 + 2] = d;
            }
        }
    }


    // Printing the top 20 IOC values for the user to choose rotor
    system("cls");
    printf("Rotor   IOC       |  No\n-----------------------\n");
    for (int i = 0; i < arrLen; i++){
        printf("%d%d%d ->  %f  |  %d\n", IOCmapNG[i * 3 + 0] + 1, IOCmapNG[i * 3 + 1] + 1, IOCmapNG[i * 3 + 2] + 1, IOCputNG[i], i+1);
    }
    printf("\n\nNo: ");

    // Converting user input from Str to Int
    int t;
    fgets(userInput, 2, stdin);
    while ((t = fgetc(stdin)) != '\n' && t != EOF);
    userChoice = atoi(userInput);
    system("cls");


    // Storing Rotor Combination based on user choice
    userChoice --;
    finalRotor[0] = rotorAll[IOCmapNG[userChoice * 3 + 0]];
    finalRotor[1] = rotorAll[IOCmapNG[userChoice * 3 + 1]];
    finalRotor[2] = rotorAll[IOCmapNG[userChoice * 3 + 2]];
    finalRotor[3] = reflector;


    return finalRotor;
}


int* OffsetBrute(char *text, char *finalRotor[], int *finalOffset){

    char userInput[2];
    int userChoice;
    char *rotorAll[] = {rotor1, rotor2, rotor3, rotor4, rotor5};

    char output[strlen(text)];
    char actualText[strlen(text)];
    strcpy(actualText, text);

    // rotor Configuration
    int offset[3];
    static char plugbaord[] = {'\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0'}; // Configure plugbord mapping

    // Creating combinations of Offsets
    double *iocList = malloc(sizeof(double) * 26 * 26  * 26);
    int *iocMapList = malloc(sizeof(int) * 26 * 26 *26 * 3);
    int percentVal = (26*26*26)/100, percent = 1, r = 0;

    for (int x = 0; x < 26; x++){
        for (int y = 0; y < 26; y++){
            for (int z = 0; z < 26; z++){

                offset[0] = x;
                offset[1] = y;
                offset[2] = z;

                // restore original value of text
                strcpy(output, EnigmaCipher(text, offset, finalRotor, plugbaord));
                strcpy(text, actualText);

                // store result values
                iocList[r] = IOC(output, 0);
                iocMapList[r * 3 + 0] = x; iocMapList[r * 3 + 1] = y; iocMapList[r * 3 + 2] = z;

                r ++;
            }

            // Create Percentage Progress UI
            if (r > percentVal){
                    percentVal += (26*26*26)/100;
                    system("cls");
                    printf("Generating Offsets ....\n%d%% complete", percent);
                    percent += 1;
            }
        }
    }


    // sorting IOC values by descending order
    double d;
    int e,f,g;

    for (int i = 0; i < 17576; ++i) {
        for (int j = i + 1; j < 17576; ++j) 
        {
            if (iocList[i] < iocList[j]) 
            {
                d = iocList[i];
                iocList[i] = iocList[j];
                iocList[j] = d;

                e = iocMapList[i * 3 + 0]; f = iocMapList[i * 3 + 1]; g = iocMapList[i * 3 + 2];
                iocMapList[i * 3 + 0] = iocMapList[j * 3 + 0]; iocMapList[i * 3 + 1] = iocMapList[j * 3 + 1]; iocMapList[i * 3 + 2] = iocMapList[j * 3 + 2];
                iocMapList[j * 3 + 0] = e; iocMapList[j * 3 + 1] = f; iocMapList[j * 3 + 2] = g;
            }
        }
    }


    // Printing the top 20 IOC values for the user to choose offset conf
    system("cls");
    printf("No  |  IOC            Offset\n------------------------------\n");
    for (int i = 0; i < arrLen; i++){
        printf("%d   |  %f    <- %d %d %d\n", i+1, iocList[i], iocMapList[i * 3 + 0], iocMapList[i * 3 + 1], iocMapList[i * 3 + 2]);
    }
    printf("\n\nNo: ");

    // Converting user input from Str to Int
    int c;
    fgets(userInput, 2, stdin);
    while ((c = fgetc(stdin)) != '\n' && c != EOF);
    userChoice = atoi(userInput);
    system("cls");

    // Storing Rotor Combination based on user choice
    userChoice --;
    finalOffset[0] = iocMapList[userChoice * 3 + 0];
    finalOffset[1] = iocMapList[userChoice * 3 + 1];
    finalOffset[2] = iocMapList[userChoice * 3 + 2];

    free(iocList);
    free(iocMapList);


    return finalOffset;
}


char* plugBoardBrute(char *text, char *finalRotor[], int *finalOffset, char *finalPlugboard){

    char userInput[2];
    int userChoice;

    double iocListE[13];
    int iocListMapE[13];

    // created this varible to store possible plugboard settings
    char tmpPlugboard[13];
    char estPlugboard[26];
    for (int a = 0; a < 26; a++){
        estPlugboard[a] = '\0';
        tmpPlugboard[a/2] = '\0';
    }

    char output[strlen(text)];
    char actualText[strlen(text)];
    strcpy(actualText, text);

    char semiPlug[] = {'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'};
    static char plugbaord[] = {'\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0'}; // Configure plugbord mapping

    // producing IOC of different plugbaord settings (one char at a time)
    for (int x = 0; x < 13; x++){
        for (int y = 0; y < 13; y++){

            plugbaord[y] = semiPlug[x];

            strcpy(output, EnigmaCipher(text, finalOffset, finalRotor, plugbaord));
            strcpy(text, actualText);

            plugbaord[y] = '\0';

            iocListE[y] = IOC(output, 0);
            iocListMapE[y] = y;
        }

        // sorting IOC values by descending order
        double d;
        int e;

        for (int i = 0; i < 13; ++i) {
            for (int j = i + 1; j < 13; ++j) 
            {
                if (iocListE[i] < iocListE[j]) 
                {
                    d = iocListE[i];
                    iocListE[i] = iocListE[j];
                    iocListE[j] = d;

                    e = iocListMapE[i];
                    iocListMapE[i] = iocListMapE[j];
                    iocListMapE[j] = e;
                }
            }
        }

        // storing the top IOC char position on the plugbaord
        double topIoc[13];
        if ((estPlugboard[iocListMapE[0] * 2 + 1] == '\0') || (iocListE[0] > topIoc[iocListMapE[0]])){

            estPlugboard[iocListMapE[0] * 2 + 1] = semiPlug[x];
            topIoc[iocListMapE[0]] = iocListE[0];

        }
    }


    // Getting total no of plugbaord maps
    int lenPlug = 0;
    int combo = 1;
    for (int i = 0; i < 13; i++){
        if (estPlugboard[iocListMapE[i] * 2 + 1] != '\0'){
            lenPlug ++;
            combo = combo * 2;
        }
    }

    // combinations of all passible wallplug settings
    double *iocListF = malloc(sizeof(double) * combo);
    char *iocListMapF = calloc(combo * 13, sizeof(char));


    // create array to store variations of wall plugs
    int variation[combo];
    for (int i = 0; i < lenPlug; i++){
        variation[i] = 0;
    }


    // Creating wallplug from wallplug variations & storing them into global array
    int count;
    int bool;
    int repCount;
    for (int x = 0; x < combo; x++){

        repCount = 0;
        for (int z = 0; z < 13; z++){

            if (estPlugboard[z * 2 + 1] != '\0'){
                tmpPlugboard[z] = estPlugboard[z * 2 + variation[repCount]];
                iocListMapF[x * 13 + z] = estPlugboard[z * 2 + variation[repCount]];
                repCount ++;
            }
        }

        // restore original value of text
        strcpy(output, EnigmaCipher(text, finalOffset, finalRotor, tmpPlugboard));
        strcpy(text, actualText);

        // Storing IOC valus in array
        iocListF[x] = IOC(output, 0);


        // Creating variations for wall plug
        variation[0] ++;
        count = 0;
        bool = 1;

        while (bool && count < lenPlug){

            if (variation[count] == 2){
                variation[count] = 0;
                variation[count + 1] ++;
            } else {
                bool = 0;
            }

            count ++;
        }
    }

    // sorting IOC values by descending order
    double d;
    char e[13];

    for (int i = 0; i < combo; ++i) {
        for (int j = i + 1; j < combo; ++j) 
        {
            if (iocListF[i] < iocListF[j]) 
            {
                d = iocListF[i];
                iocListF[i] = iocListF[j];
                iocListF[j] = d;


                memcpy(e, iocListMapF + (i * 13), 13 * sizeof(char));
                memcpy(iocListMapF + (i * 13), iocListMapF + (j * 13), 13 * sizeof(char));
                memcpy(iocListMapF + (j * 13), e, 13 * sizeof(char));
            }
        }
    }

    // Decides X where X is the number of Top IOC values
    int topVal;
    if (combo > arrLen){
        topVal = arrLen;
    } else {
        topVal = combo;
    }

    // Printing the top X IOC values for the user to choose offset conf
    system("cls");
    printf("No  |  IOC          Plugboard\n---------------------------------\n");

    for (int i = 0; i < topVal; i++){
        printf("%d   |  %f     ", i+1, iocListF[i]);

        for (int y = 0; y < 13; y++){
            if (iocListMapF[i * 13 + y] == '\0'){
                printf("_");
            } else{
                printf("%c", iocListMapF[i * 13 + y]);
            }
        }
        printf("\n");

    }
    printf("\n\nNo: ");

    // Converting user input from Str to Int
    int c;
    fgets(userInput, 2, stdin);
    while ((c = fgetc(stdin)) != '\n' && c != EOF);
    userChoice = atoi(userInput);
    system("cls");

    // Storing User selected Plugboard
    memcpy(finalPlugboard, iocListMapF + 13 * (userChoice - 1), 13 * sizeof(char));


    free(iocListF);
    free(iocListMapF);

    return finalPlugboard;
}


int main(){

    char data[] = "MMGKVXFDNTDPFDVLCKMFUUTISOPLERXWYLJKMEJUARREMEKSPPWBDCRMZUDXTKIXVMVFRGSVINAMMSALWHFOEHMIBFDNXJQMGGIUQRCVTSWAMBAEIPFCLIOVFIJZJNMGLLSAQROKSALTLZFCPREVQVZFOYJUYPWHCRFFYKCEQQDNHYBXDCMPNZSZYDNOJBSZEEOXQNQOERUGKNASSYLCRZOQNWSRXHJHOZHARTYWOCNUXYZHWYMAQHPFJZHTEIGQNDAEAZGNCBWDXEMPVXFYKBDLGKFCJXBKFDZIRBKCTIUDAYTWGEERBNOVWOKSUFBPBJLQQSBRPKVAVTGIJDDUSQTYKMBVQHQPOMEWEPLXBXQSZLIUTFRHGNDRDUXPUTTLVGPMBANDRQGBPWKKBPTYDSRPYPBDVQNXVOYXDBCQNCPWIMOSXVIMXXYTIOEVMLJVCJWQKXTMCQMRERFSQJCFWROUVQSPYIJEYCCLYJTGHDRIUPQVWEHHLUYAGBHIZHUKOTPELDWQOABLKZSXVUOOXQYQJTXDRJRWDFQNOKIIVBSZBWOKLEIRXQEZCTLWDXNJKGQMXHFYADPUNMFMVVQGMYMYTBUYRLFMZVDILRQUXUQFUKBMMIQGNCBZNFCLXZFGTKWETEKHKJKVEKTMBDWPGJCTGEGPAXOZRDPRXYYRTXPRVKFIRVTYYXWAMYRZOTRIYXHLCWDXYPXFBSQVVPIJULWWZOJXYAWIPUTNLOUGKQADOIUIZGOWSQWQJLIIPJZOBGGEFMWKMIDMBUPGDETRKOFNMFRUETVITOKBILUEYEOAVXRDEGRNZWQIRDJQIOBETPTQJVXSGTADPQJNHOKYAAAWKWKVFQEPEFOYABVKXZGXDTGASISPDEMBSQDEUAQEQXRTAMJYRMXCCCFBUPAWYXKYIIAMATJCQAJHLORCZMJJJRAPSKWTSSEYEBXXKGXLZWJPKGWRQPFV"; // Text/Cipher goes here
    char *finalRotor[4];
    int finalOffset[3];
    char finalPlugboard[13];
    
    RotorBrute(data, finalRotor);
    OffsetBrute(data, finalRotor, finalOffset);
    plugBoardBrute(data, finalRotor, finalOffset, finalPlugboard);

    // Final Decryption
    printf("-------------------------------------- Decrypted Text --------------------------------------\n%s\n\n", EnigmaCipher(data, finalOffset, finalRotor, finalPlugboard));
    
    return 0;
}