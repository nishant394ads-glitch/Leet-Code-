class Solution {
public:
    vector<int> pathExistenceQueries(int n, vector<int>& nums, int maxDiff, vector<vector<int>>& queries) {
        vector<pair<int,int>> a;
        for(int i = 0; i < n; i++)
            a.push_back({nums[i], i});
        sort(a.begin(), a.end());

        vector<int> pos(n);
        for(int i = 0; i < n; i++)
            pos[a[i].second] = i;

        // far[i] = farthest sorted index reachable in one edge
        vector<int> far(n);
        int j = 0;
        for(int i = 0; i < n; i++) {
            while(j + 1 < n && a[j + 1].first - a[i].first <= maxDiff)
                j++;
            far[i] = j;
        }

        // Binary lifting
        const int LOG = 18;
        vector<vector<int>> up(LOG, vector<int>(n));

        for(int i = 0; i < n; i++)
            up[0][i] = far[i];

        for(int k = 1; k < LOG; k++) {
            for(int i = 0; i < n; i++) {
                up[k][i] = up[k - 1][ up[k - 1][i] ];
            }
        }

        vector<int> ans;

        for(auto &q : queries) {
            int l = pos[q[0]];
            int r = pos[q[1]];

            if(l > r) swap(l, r);

            if(l == r) {
                ans.push_back(0);
                continue;
            }

            if(far[l] == l) {
                ans.push_back(-1);
                continue;
            }

            int cur = l;
            int steps = 0;

            for(int k = LOG - 1; k >= 0; k--) {
                if(up[k][cur] < r) {
                    cur = up[k][cur];
                    steps += (1 << k);
                }
            }

            if(far[cur] < r)
                ans.push_back(-1);
            else
                ans.push_back(steps + 1);
        }

        return ans;
    }
};