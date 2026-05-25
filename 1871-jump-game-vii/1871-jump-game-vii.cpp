class Solution {
public:
    bool canReach(string s, int minJump, int maxJump) {
        int n = s.size();
        
        vector<bool> reachable(n, false);
        reachable[0] = true;
        
        int count = 0;
        
        for (int i = 1; i < n; i++) {
            
            if (i - minJump >= 0 && reachable[i - minJump])
                count++;
            
            if (i - maxJump - 1 >= 0 && reachable[i - maxJump - 1])
                count--;
            
            if (s[i] == '0' && count > 0)
                reachable[i] = true;
        }
        
        return reachable[n - 1];
    }
};