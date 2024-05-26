#include <stdlib.h>
#include <stdio.h>
#include <windows.h>
#include <conio.h>
#include <pthread.h>


// Remove Crusor from terminal
void hidecursor(){
    HANDLE consoleHandle = GetStdHandle(STD_OUTPUT_HANDLE);
    CONSOLE_CURSOR_INFO info;
    info.dwSize = 100;
    info.bVisible = FALSE;
    SetConsoleCursorInfo(consoleHandle, &info);
}

void display(int *data, int size, int speed){
    system("cls");

    for (int x = 0; x < size; x++){
        if (data[x] == 0){
            printf("-");
        } else if (data[x] == 1){
            printf("-\n");
        } else if (data[x] == 2){
            printf("|");
        } else if (data[x] == 3){
            printf("|\n");
        } else if (data[x] == 4){
            printf(" ");
        } else if (data[x] == 5){
            printf("@");
        }else if (data[x] == 6){
            printf("$");
        } else {
            printf("error ");
        }
    }
    Sleep(speed);
    
}

void displaySet(int *data, int width, int height, int snakeLen, int *snakePos){

    int snakeCount = 0;
    
    for (int y = 0; y < height; y++){
        for (int x = 0; x < width; x++){

            // Set top & bottom frame "-"
            if (y == 0 || y == height - 1){
                if (x == width - 1){
                    data[width * y + x] = 1;

                }else{
                    data[width * y + x] = 0;
                }

            // Set snake body
            } else if ((y == height/2 && x == width/2) || (snakeCount > 0 && snakeCount < snakeLen)){

                // Storing snake cordinates
                snakePos[snakeCount] = width * y + x;

                // Set Snake Body
                data[width * y + x] = 5;
                snakeCount ++;

            } else {

                // Set side frame
                if (x == 0){
                    data[width * y + x] = 2;

                // Set side frame
                }else if (x == width - 1){
                    data[width * y + x] = 3;

                // Set blank spaces
                }else{
                    data[width * y + x] = 4;
                }
            }
        }
    }

    // Generate random pos for fruit
    srand(time(0));
    for (int x = 0; x < 5; x++){
        int randPos = (rand() % (width * height - width)) - width;
        data[randPos] = 6;
    }
}

void *listener(void *valueX){
    // left - 0
    // right - 1
    // up - 3
    // down - 4

    // Retrieving INT value of direction
    int *value = (int *)valueX;
    char ch;
    int key;

    while (1) {
        if (kbhit) {
            ch = getch();
            key = (int)ch;
            

            // Down
            if (key == 80) {
                if (4 - value[0] != 1 && 4 - value[0] != -1){
                    value[0] = 4;
                    // printf("down")
                }

            // Up
            } else if (key == 72){
                if (3 - value[0] != 1 && 3 - value[0] != -1){
                    value[0] = 3;
                    // printf("up");
                }

            // Left
            } else if (key == 75){
                if (0 - value[0] != 1 && 0 - value[0] != -1){
                    value[0] = 0;
                    // printf("left");
                }
            
            // Right
            } else if (key == 77){
                if (1 - value[0] != 1 && 1 - value[0] != -1){
                    value[0] = 1;
                    // printf("right");
                }

            // Esc
            } else if (key == 27){
                break;
            }
        }
    }
}

void move(int *data, int *value, int *snakePos, int width, int height){
    // left - 0
    // right - 1
    // up - 3
    // down - 4

    int head;
    int direction = value[0];
    int snakeLen = value[1];

    
    // Getting Array pos around the snake head for its next step
    if (direction == 0){
        head = snakePos[0] - 1;

    } else if (direction == 1) {
        head = snakePos[0] + 1;

    } else if (direction == 3) {
        head = snakePos[0] - width;

    } else if (direction == 4) {
        head = snakePos[0] + width;
    }


    if (data[head] == 6){
        // Generate random pos for fruit
        srand(time(0));
        int randPos = 0;

        while (data[randPos] != 4){
            randPos = (rand() % (width * height - width)) - width;
        }
        data[randPos] = 6;
        snakeLen ++;
        value[1] ++;
        printf("%d", value[1]);

    } else if (data[head] != 4){
        Sleep(2000);
        system("cls");
        printf("-------------------------------------------------------------- GAME OVER --------------------------------------------------------------");
        Sleep(2000);
        exit(0);

    } else {
        // Remove the last snake body (tail) for every step
        data[snakePos[snakeLen - 1]] = 4;
    }

    // Assigning the snake head its next head step position
    for (int x = snakeLen - 1; x > 0; x--){
        snakePos[x] = snakePos[x - 1];
    }
    snakePos[0] = head;
    // printf("%d\n", data[snakePos[0]]);

    
    // Update new head to display
    data[head] = 5;
    
}

int main(){

    // enable faster printing
    char buffer[7];
    setvbuf(stdout, buffer, _IOFBF, sizeof(buffer));


    int width = 150;
    int height = 35;
    int snakeLen = 20;

    // The lower the number, the faster the snake
    int speed = 1;

    int *data = malloc(height * width * sizeof(int));
    int *snakePos = calloc(height * width, sizeof(int));

    // 0 - direction
    // 1 - snake length
    int *value = malloc(2 * sizeof(int));
    value[0] = 0;
    value[1] = snakeLen;


    
    hidecursor();
    displaySet(data, width, height, snakeLen, snakePos);


    // Creating and running listener thread
    pthread_t thread_id;
    pthread_create(&thread_id, NULL, listener, value);
    

    while (1){
        display(data, height * width, speed);
        move(data, value, snakePos, width, height);
    }

    // pthread_exit(&thread_id);
    free(data);
    free(value);
    free(snakePos);

    return 0;
}