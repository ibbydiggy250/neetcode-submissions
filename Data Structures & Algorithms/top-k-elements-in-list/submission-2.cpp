class Solution {
public:
    vector<int> topKFrequent(vector<int>& nums, int k) {
        unordered_map<int,int> s;
        priority_queue<pair<int,int>,
               vector<pair<int,int>>,
               greater<pair<int,int>>> pq;
        vector<int> sol;
        for(int num:nums){
            if(s.count(num)){
                s[num]++;
            }
            else{
                s[num] = 1;
            }
        }
        for(auto& c:s){
            pq.push({c.second,c.first});
            if(pq.size()>k){
                pq.pop();
            }
        }
        while(!pq.empty()){
            sol.push_back(pq.top().second);
            pq.pop();
        }
        return sol;

        
    }
};
