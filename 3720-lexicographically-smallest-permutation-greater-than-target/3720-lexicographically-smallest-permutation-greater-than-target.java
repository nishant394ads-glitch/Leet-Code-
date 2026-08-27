class Solution {
    public String lexGreaterPermutation(String s, String target) {
        int n = s.length();
        int[] freq = new int[26];

        for (char c : s.toCharArray()) {
            freq[c - 'a']++;
        }

        char[] ans = new char[n];

        // Match target prefix
        int i = 0;

        while (i < n) {
            int x = target.charAt(i) - 'a';

            if (freq[x] == 0)
                break;

            ans[i] = target.charAt(i);
            freq[x]--;
            i++;
        }

        // Try to make the string greater
        int start = (i == n) ? n - 1 : i;

        for (int j = start; j >= 0; j--) {

            // If this position was part of the matched prefix,
            // return its character to the available pool.
            if (j < i) {
                freq[target.charAt(j) - 'a']++;
            }

            int cur = target.charAt(j) - 'a';

            // Find the smallest available character > target[j]
            for (int c = cur + 1; c < 26; c++) {
                if (freq[c] > 0) {

                    ans[j] = (char) ('a' + c);
                    freq[c]--;

                    // Fill remaining positions with smallest letters
                    int pos = j + 1;

                    for (int k = 0; k < 26; k++) {
                        while (freq[k] > 0) {
                            ans[pos++] = (char) ('a' + k);
                            freq[k]--;
                        }
                    }

                    return new String(ans);
                }
            }
        }

        return "";
    }
}