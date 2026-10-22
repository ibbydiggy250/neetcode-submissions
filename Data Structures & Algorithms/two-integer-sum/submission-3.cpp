class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        unordered_map<int,int> c;
        vector<int> sol;
        for(int i=0;i<nums.size();i++){
            int need = target - nums[i];
            if(c.count(need)){
                sol.push_back(c[need]);
                sol.push_back(i);
                return sol;
            }
            c[nums[i]] = i;
        }
        return sol;
    }
};
