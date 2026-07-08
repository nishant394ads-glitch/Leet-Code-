class Solution {
public:
    static const int MOD = 1000000007;

    vector<int> sumAndMultiply(string s, vector<vector<int>>& queries) {
        int n = s.size();

        vector<int> pos;
        vector<int> digit;

        for (int i = 0; i < n; i++) {
            if (s[i] != '0') {
                pos.push_back(i);
                digit.push_back(s[i] - '0');
            }
        }

        int k = pos.size();

        vector<long long> pow10(k + 1, 1);
        for (int i = 1; i <= k; i++)
            pow10[i] = (pow10[i - 1] * 10) % MOD;

        vector<long long> hash(k + 1, 0);
        vector<long long> prefSum(k + 1, 0);

        for (int i = 0; i < k; i++) {
            hash[i + 1] = (hash[i] * 10 + digit[i]) % MOD;
            prefSum[i + 1] = prefSum[i] + digit[i];
        }

        vector<int> ans;

        for (auto &q : queries) {
            int l = q[0], r = q[1];

            int L = lower_bound(pos.begin(), pos.end(), l) - pos.begin();
            int R = upper_bound(pos.begin(), pos.end(), r) - pos.begin() - 1;

            if (L > R) {
                ans.push_back(0);
                continue;
            }

            int len = R - L + 1;

            long long x = (hash[R + 1] -
                          hash[L] * pow10[len] % MOD + MOD) % MOD;

            long long sum = prefSum[R + 1] - prefSum[L];

            ans.push_back((x * (sum % MOD)) % MOD);
        }

        return ans;
    }
};