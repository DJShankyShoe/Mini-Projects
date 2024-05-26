#include <stdio.h>
#include <stdlib.h>
#include <string.h>

typedef struct {
    char *word;
    char *guess;  // This is 'word' but with underlines where not guessed, yet
    int lives;
} hangman;

hangman player1() {
    char *word = malloc(50);
    char *guess = calloc(100, 1);
    char *strLives;
    int lives;

    system("cls");
    printf("----------------- HANGMAN -----------------\n\nPlayer 1 - Enter a word to be guessed: ");
    fgets(word, 50, stdin);

    word[strcspn(word, "\n")] = '\0';  // remove (possibly) trailing newline
    
    for (int i = 0; word[i]; i++) {
        guess[i * 2] = '_';
        guess[i * 2 + 1] = ' ';
    }

    printf("How many lives should the player have: ");
    fgets(strLives, 10, stdin);
    lives = atoi(strLives);
    
    return (hangman) { word, guess, lives };
}


void player2(hangman *data)
{   

    char userGuess[2];

    int bool = 1;
    while (bool){

        system("cls");
        printf("Player 2, guess the word, one character at a time!\nYou have %d lives remaning\n\n", data->lives);
        printf("%s\nYour Guess: ", data->guess);

        int c;
        fgets(userGuess, 2, stdin);
        while ((c = fgetc(stdin)) != '\n' && c != EOF);

        int temp_count = 0;
        for (int i = 0; i < data->word[i]; i++){
            if (userGuess[0] == data->word[i]){
                data->guess[i * 2] = userGuess[0];
            } else {
                temp_count += 1;
            }
        }

        if (temp_count == strlen(data->word)){
            data->lives -= 1;
        }

        bool = 0;
        for (int i = 0; i < data->word[i]; i++){
            
            if (data->guess[i * 2] == '_'){
                bool = 1;
                break;
            }
        }

        if (data->lives < 1){
            bool = 0;
        }

    }

    if (data->lives == 0){
        printf("\n\n------------- YOU RAN OUT OF LIVES!! ------------- \n\n");
    } else {
        printf("\n\n------------- YOU WON!! ------------- \n\n");
    }

    printf("The word: %s\n\n\n", data->word);
}


int main()
{   
    hangman game = player1();
    player2(&game);

    free(game.word);
    free(game.guess);

    char *end;
    fgets(end, 3, stdin);

    return 0;
}