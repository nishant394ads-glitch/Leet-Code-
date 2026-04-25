import java.util.Arrays;

class Solution {
    public int maxDistance(int side, int[][] points, int k) {
        Arrays.sort(points, (a, b) -> Integer.compare(to1D(a[0], a[1], side), to1D(b[0], b[1], side)));
        int n = points.length;
        
        int lo = 1, hi = 2 * side, ans = 0;
        while (lo <= hi) {
            int mid = lo + (hi - lo) / 2;
            if (canPlace(points, n, k, mid)) {
                ans = mid;
                lo = mid + 1;
            } else {
                hi = mid - 1;
            }
        }
        return ans;
    }
    
    private int to1D(int x, int y, int side) {
        if (y == 0)         return x;
        else if (x == side) return side + y;
        else if (y == side) return 2 * side + (side - x);
        else                return 3 * side + (side - y);
    }
    
    private int manhattan(int[][] pts, int i, int j) {
        return Math.abs(pts[i][0] - pts[j][0]) + Math.abs(pts[i][1] - pts[j][1]);
    }
    
    private boolean canPlace(int[][] pts, int n, int k, int mid) {
        // Build nxt[i] = next index after i (in doubled circular array) with dist >= mid
        // O(n) two-pointer: for each i, find first j in (i, i+n) with manhattan >= mid
        // nxt IS monotone non-decreasing when built over doubled array correctly
        int[] nxt = new int[2 * n];
        
        int r = 1;
        for (int i = 0; i < 2 * n; i++) {
            if (r < i + 1) r = i + 1;
            while (r < i + n && manhattan(pts, i % n, r % n) < mid) {
                r++;
            }
            nxt[i] = r; // sentinel i+n if nothing found
        }
        // r is global and never decreases — this is O(n) total across all i
        // because r traverses [0, 4n) at most once total
        
        // Binary lifting: up[j][i] = position after 2^j greedy jumps from i
        int LOG = 5; // 2^5 = 32 >= k (k <= 25)
        int[][] up = new int[LOG][2 * n];
        for (int i = 0; i < 2 * n; i++) {
            up[0][i] = nxt[i];
        }
        for (int j = 1; j < LOG; j++) {
            for (int i = 0; i < 2 * n; i++) {
                int prev = up[j-1][i];
                up[j][i] = (prev < 2 * n) ? up[j-1][prev] : 2 * n;
            }
        }
        
        // For each start in [0,n), lift k-1 jumps, check wrap-around
        for (int start = 0; start < n; start++) {
            int cur = start;
            int remaining = k - 1;
            for (int j = LOG - 1; j >= 0; j--) {
                if (remaining >= (1 << j)) {
                    int jumped = up[j][cur];
                    if (jumped < 2 * n) {
                        cur = jumped;
                        remaining -= (1 << j);
                    }
                }
            }
            // remaining must be 0, cur within circle, last->start >= mid
            if (remaining == 0 
                && cur < start + n 
                && manhattan(pts, cur % n, start) >= mid) {
                return true;
            }
        }
        return false;
    }
}