#include <bits/stdc++.h>
using namespace std;

struct Edge
{
    int u, v, weight;
};

bool compare(Edge a, Edge b){
    return a.weight < b.weight;
}

int findParent(vector<int> &parent, int node){
    if(parent[node] == node){
        return node;
    }
    return parent[node] = findParent(parent, parent[node]);
}

void kruskalMST(vector<Edge> edges, int V){

    sort(edges.begin(), edges.end(), compare);

    vector<int>parent(V);
    for(int i=0;i<V;i++){
        parent[i] = i;
    }

    cout<<"\nKruskal's MST: \nEdges\tWeight\n";
    int total=0;
    for(Edge e: edges){
        int pu = findParent(parent, e.u);
        int pv = findParent(parent, e.v);

        if(pu != pv){
            cout<<e.u<<" - "<<e.v<<"\t"<<e.weight<<endl;
            total += e.weight;
            parent[pu] = pv;
        }
    }


}



int main(){

    int V = 5;

    vector<Edge> edges = {
        {0, 1, 2}, {1, 2, 3}, {0, 3, 6}, {1, 3, 8},
        {1, 4, 5}, {2, 4, 7}, {3, 4, 9}
    };

    kruskalMST(edges, V);

    return 0;
}