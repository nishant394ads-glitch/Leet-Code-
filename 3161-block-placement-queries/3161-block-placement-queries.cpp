class Fenwick {
public:
    vector<int> bit;
    int n;

    Fenwick(int n) : n(n) {
        bit.assign(n + 1, 0);
    }

    void update(int idx, int val) {
        idx++;
        while (idx <= n) {
            bit[idx] = max(bit[idx], val);
            idx += idx & -idx;
        }
    }

    int query(int idx) {
        idx++;
        int res = 0;
        while (idx > 0) {
            res = max(res, bit[idx]);
            idx -= idx & -idx;
        }
        return res;
    }
};

class Solution {
public:
    vector<bool> getResults(vector<vector<int>>& queries) {
        int mx = 0;

        for (auto &q : queries) {
            mx = max(mx, q[1]);
        }

        set<int> obs = {0, mx + 1};

        for (auto &q : queries) {
            if (q[0] == 1) {
                obs.insert(q[1]);
            }
        }

        Fenwick bit(mx + 2);

        auto addGap = [&](int pos, int gap) {
            bit.update(pos, gap);
        };

        for (auto it = next(obs.begin()); it != obs.end(); ++it) {
            auto prv = prev(it);
            addGap(*it, *it - *prv);
        }

        vector<bool> ans;

        for (int i = (int)queries.size() - 1; i >= 0; --i) {
            auto &q = queries[i];

            if (q[0] == 2) {
                int x = q[1];
                int sz = q[2];

                auto it = obs.upper_bound(x);
                int right = *it;
                int left = *prev(it);

                int best = bit.query(left);
                best = max(best, x - left);

                ans.push_back(best >= sz);
            }
            else {
                int x = q[1];

                auto it = obs.find(x);
                auto l = prev(it);
                auto r = next(it);

                addGap(*r, *r - *l);

                obs.erase(it);
            }
        }

        reverse(ans.begin(), ans.end());
        return ans;
    }
};