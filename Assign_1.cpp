#include <bits/stdc++.h>
using namespace std;

void bfsRecursive(int n, vector<vector<int>> &edgeList , queue<int> q, unordered_set<int>visited){

    visited.insert(n);
    cout<<n<<" ";

    for(int neighbour: edgeList[n]){
        if(visited.find(neighbour) == visited.end()){
            q.push(neighbour);
            visited.insert(neighbour);
        }
    }

    if(!q.empty()){
        int next_node = q.front();
        q.pop();
        bfsRecursive(next_node, edgeList, q, visited);
    }

}


void dfsRecursive(vector<vector<int>> &adj , vector<bool> &visited, int n){

    visited[n] = true;
    cout << n << " "; 

    for(int i: adj[n]){

        if(visited[i] == false){
            dfsRecursive(adj, visited, i);
        }
    }

}

int main(){

    int nodes;
    cout<<"Enter the number of nodes: ";
    cin>>nodes;

    vector<vector<int>> edgeList(nodes);

    for(int i=0;i<nodes;i++){
        int data = 0;
        do{
            cout<<"Enter the nodes connected with "<<i<<" : ";
            cin>>data;
            if(data != -1){
                edgeList[i].push_back(data);
            }

        }while(data != -1);
    }

    queue<int> q;
    unordered_set<int>visited;

    bfsRecursive(0, edgeList, q, visited);
    cout<<endl;

    vector<bool>visit(nodes, 0);

    dfsRecursive(edgeList, visit, 0);


    return 0;
}