//Tic Tac Toe

#include<iostream>

using namespace std;

static int board[3][3];
static int turn=1;

static void printBoard() {
  for(int i=0; i<3; i++) {
    for(int j=0; j<3; j++) {
      if(board[i][j]==1) {
        cout << "X ";
      }
      else if(board[i][j]==2) {
        cout << "O ";
      }
      else {
        cout << "_ ";
      }
    }
    cout << endl;
  }
}

static int checkForWinner() {
  if((board[0][0]==board[0][1])&&(board[0][0]==board[0][2])&&board[0][0]!=0) {
    return board[0][0];
  }
  else if((board[1][0]==board[1][1])&&(board[1][0]==board[1][2])&&board[1][0]!=0) {
    return board[1][0];
  }
  else if((board[2][0]==board[2][1])&&(board[2][0]==board[2][2])&&board[2][0]!=0) {
    return board[2][0];
  }



  else if((board[0][0]==board[1][0])&&(board[0][0]==board[2][0])&&board[0][0]!=0) {
    return board[0][0];
  }
  else if((board[0][1]==board[1][1])&&(board[0][1]==board[2][1])&&board[0][1]!=0) {
    return board[0][1];
  }

  else if((board[0][2]==board[1][2])&&(board[0][2]==board[2][2])&&board[0][2]!=0) {
    return board[0][2];
  }



  else if((board[0][0]==board[1][1])&&(board[0][0]==board[2][2])&&board[0][0]!=0) {
    return board[0][0];
  }
  else if((board[2][0]==board[1][1])&&(board[2][0]==board[0][2])&&board[2][0]!=0) {
    return board[2][0];
  }



  return 0;
}


static void makeMove() {
  int x, y;

  cout << "Please enter the row" << endl;
  cin >> x;

  cout << "Please enter the column" << endl;
  cin >> y;

  x--;
  y--;

  if(board[x][y]!=0) {
    cout << "Position already taken" << endl;
    makeMove();
  }
  else {
    board[x][y]=turn;
    if(turn==1) {
      turn=2;
    }
    else {
      turn=1;
    }
  }
}

int main()
{
  for(int i=0; i<3; i++) {
    for(int j=0; j<3; j++) {
      board[i][j]=0;
    }
  }

  bool gameRunning = true;
  int count=0;

  while(gameRunning==true && count<9)
  {
    printBoard();
    makeMove();
    if(checkForWinner()!=0) {
      gameRunning=false;
    }
    count++;
  }

  printBoard();
  if(count == 9) {
    cout << "It's a tie!" << endl;
  }
  else {
    cout << "Congratulations player " << checkForWinner() << endl;
  }

}
