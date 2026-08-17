class Solution {

    private int[] prefix;
    private int[] stoneValue;
    private Integer[][] dp;

    public int stoneGameV(int[] stoneValue) {
        this.stoneValue = stoneValue;

        int n = stoneValue.length;

        prefix = new int[n + 1];

        for (int i = 0; i < n; i++) {
            prefix[i + 1] = prefix[i] + stoneValue[i];
        }

        dp = new Integer[n][n];

        return dfs(0, n - 1);
    }

    private int dfs(int l, int r) {

        // Only one stone
        if (l >= r) {
            return 0;
        }

        // Already calculated
        if (dp[l][r] != null) {
            return dp[l][r];
        }

        int ans = 0;

        int leftSum = 0;
        int rightSum = prefix[r + 1] - prefix[l];

        for (int k = l; k < r; k++) {

            leftSum += stoneValue[k];
            rightSum -= stoneValue[k];

            // Left side is smaller
            if (leftSum < rightSum) {

                /*
                 * Even without considering the next DP result,
                 * choosing this split can give at most 2 * leftSum.
                 *
                 * If ans is already >= 2 * leftSum,
                 * this split cannot improve the answer.
                 */
                if (ans >= 2 * leftSum) {
                    continue;
                }

                ans = Math.max(
                    ans,
                    leftSum + dfs(l, k)
                );
            }

            // Right side is smaller
            else if (leftSum > rightSum) {

                /*
                 * As k increases:
                 * rightSum only becomes smaller.
                 *
                 * Therefore, if the current right side cannot
                 * beat ans, no later right side can beat it either.
                 */
                if (ans >= 2 * rightSum) {
                    break;
                }

                ans = Math.max(
                    ans,
                    rightSum + dfs(k + 1, r)
                );
            }

            // Both sides are equal
            else {

                ans = Math.max(
                    ans,
                    leftSum + dfs(l, k)
                );

                ans = Math.max(
                    ans,
                    rightSum + dfs(k + 1, r)
                );
            }
        }

        return dp[l][r] = ans;
    }
}