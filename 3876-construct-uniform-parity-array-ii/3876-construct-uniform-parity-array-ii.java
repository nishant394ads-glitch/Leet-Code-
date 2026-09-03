class Solution {
    public boolean uniformArray(int[] nums1) {
        int min = nums1[0];

        for (int x : nums1) {
            min = Math.min(min, x);
        }

        // Minimum cannot be changed using a positive difference.
        // If minimum is even, every element must already be even.
        if (min % 2 == 0) {
            for (int x : nums1) {
                if (x % 2 != 0) {
                    return false;
                }
            }
        }

        return true;
    }
}