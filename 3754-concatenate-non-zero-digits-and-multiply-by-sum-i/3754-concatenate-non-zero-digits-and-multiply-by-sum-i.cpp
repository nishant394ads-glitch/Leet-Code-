class Solution {
public:
    long long sumAndMultiply(int n) {
        long long x = 0, sum = 0;

        string s = to_string(n);

        for (char c : s) {
            if (c != '0') {
                int d = c - '0';
                x = x * 10 + d;
                sum += d;
            }
        }

        return x * sum;
    }
};