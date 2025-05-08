#include <bits/stdc++.h>
using namespace std;

vector<vector<vector<char>>>solution;

bool isSafe(vector<vector<char>> &mat, int row, int col){

    for(int c=0; c<col; c++){
        if(mat[row][c] == 'Q') return false;
    }

    int i=row, j=col;
    while(i>=0 && j>=0){
        if(mat[i--][j--] == 'Q') return false;
    }

    i=row, j=col;
    while(i<mat.size() && j>=0){
        if(mat[i++][j--] == 'Q') return false;
    }

    return true;
}

void solveNqueens(int n, int row, int col, vector<vector<char>> &mat){

    if(col == n){
        solution.push_back(mat);
        return;
    }

    for(int r=0;r<n;r++){
        if(isSafe(mat, r, col)){
            mat[r][col] = 'Q';
            solveNqueens(n, r, col+1, mat);
            mat[r][col] = '.';

        }
    }
}

void printSolution(vector<vector<vector<char>>>solution){

    for(int i=0;i<solution.size();i++){
        cout<<"Solution #"<<i+1<<endl;
        for(const auto &row : solution[i]){
            for (char cell : row){
                cout<<cell<<" ";
            }
            cout<<endl;

        }
        cout<<endl;

    }
}




int main(){

    int n;
    cout<<"Enter the size of matrix (n X n): ";
    cin>>n;

    vector<vector<char>>mat(n, vector<char>(n,'.'));

    solveNqueens(n, 0, 0, mat);
    printSolution(solution);
    cout<<"Total Solutions: "<<solution.size()<<endl;


    
    return 0;
}