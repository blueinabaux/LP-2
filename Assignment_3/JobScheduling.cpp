#include<bits/stdc++.h>
using namespace std;

vector<int> jobScheduling(vector<int> &deadline, vector<int> &profit){

    int n = deadline.size();
    int cnt = 0;
    int totalProfit = 0;

    vector<tuple<int,int>> jobs;
    for(int i=0;i<n;i++){
        jobs.push_back({profit[i], deadline[i]});
    }

    sort(jobs.begin(), jobs.end(), greater<tuple<int,int>>());

    int maxDeadline = *max_element(deadline.begin(), deadline.end());

    vector<int>slots(maxDeadline, 0);

    for(int i=0;i<n;i++){
        int currProfit = get<0>(jobs[i]);
        int currDeadline = get<1>(jobs[i]);

        int pos = min(maxDeadline, currDeadline) - 1;

        for(int j=pos; j>=0; j--){
            if(slots[j] == 0){
                slots[j] = 1;
                cnt++;
                totalProfit += currProfit;
                break;
            }
        }

    }

    return {cnt, totalProfit};
}

int main(){

    vector<int> deadline = {2,1,2,1,1};
    vector<int> profit = {100, 19 ,27,25,15};
    vector<int> ans = jobScheduling(deadline, profit);

    cout<<ans[0]<<" "<<ans[1]<<endl;


    return 0;
}