class Solution {
public:
    vector<vector<string>> groupAnagrams(vector<string>& strs) {
        unordered_map<string,vector<string>> ana;
        vector<vector<string>> sol;
        vector<string> one;
        for(string s:strs){
            string k = s;
            sort(k.begin(),k.end());
            ana[k].push_back(s); 
        }

        for(auto& s:ana){
            sol.push_back(s.second);
        }
        return sol;
    }
};
