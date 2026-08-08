import java.util.*;

class Solution {
    public int[] validSequence(String word1, String word2) {
        int n = word1.length();
        int m = word2.length();

        // exact[j] = latest index where word2[j..] can
        // be matched exactly.
        int[] exact = new int[m + 1];
        Arrays.fill(exact, -1);
        exact[m] = n;

        int p = n - 1;

        for (int j = m - 1; j >= 0; j--) {
            while (p >= 0 && word1.charAt(p) != word2.charAt(j)) {
                p--;
            }

            if (p < 0) break;

            exact[j] = p;
            p--;
        }

        // Store positions of every character in word1.
        ArrayList<Integer>[] positions = new ArrayList[26];

        for (int i = 0; i < 26; i++) {
            positions[i] = new ArrayList<>();
        }

        for (int i = 0; i < n; i++) {
            positions[word1.charAt(i) - 'a'].add(i);
        }

        /*
         * one[j] = latest index from which word2[j..]
         * can be matched with at most ONE mismatch.
         */
        int[] one = new int[m + 1];
        Arrays.fill(one, -1);
        one[m] = n;

        // runStart[i] = beginning of the consecutive run
        // containing word1[i].
        int[] runStart = new int[n];

        if (n > 0) {
            runStart[0] = 0;

            for (int i = 1; i < n; i++) {
                if (word1.charAt(i) == word1.charAt(i - 1)) {
                    runStart[i] = runStart[i - 1];
                } else {
                    runStart[i] = i;
                }
            }
        }

        for (int j = m - 1; j >= 0; j--) {

            int best = -1;

            /*
             * Case 1:
             * Use the mismatch at word2[j].
             *
             * Then word2[j+1..] must match exactly.
             */
            int limit = exact[j + 1];

            if (limit != -1 && limit > 0) {
                int k = limit - 1;

                if (word1.charAt(k) != word2.charAt(j)) {
                    best = Math.max(best, k);
                } else {
                    // Find latest position before limit
                    // whose character differs.
                    best = Math.max(best, runStart[k] - 1);
                }
            }

            /*
             * Case 2:
             * Match word2[j] exactly.
             * The mismatch happens somewhere later.
             */
            limit = one[j + 1];

            if (limit != -1) {
                int k = latestOccurrence(
                    positions[word2.charAt(j) - 'a'],
                    limit
                );

                best = Math.max(best, k);
            }

            one[j] = best;
        }

        // Greedily construct lexicographically smallest indices.
        int[] answer = new int[m];

        int prev = -1;
        boolean usedMismatch = false;

        for (int j = 0; j < m; j++) {

            boolean found = false;

            for (int i = prev + 1; i < n; i++) {

                // Exact character
                if (word1.charAt(i) == word2.charAt(j)) {

                    boolean possible;

                    if (usedMismatch) {
                        // No mismatch left.
                        possible = exact[j + 1] > i;
                    } else {
                        // One mismatch can still be used later.
                        possible = one[j + 1] > i;
                    }

                    if (possible) {
                        answer[j] = i;
                        prev = i;
                        found = true;
                        break;
                    }
                }

                // Use mismatch here
                else if (!usedMismatch && exact[j + 1] > i) {

                    answer[j] = i;
                    prev = i;
                    usedMismatch = true;
                    found = true;
                    break;
                }
            }

            if (!found) {
                return new int[0];
            }
        }

        return answer;
    }

    // Returns the largest value < limit.
    private int latestOccurrence(ArrayList<Integer> list, int limit) {

        int left = 0;
        int right = list.size() - 1;
        int answer = -1;

        while (left <= right) {

            int mid = left + (right - left) / 2;

            if (list.get(mid) < limit) {
                answer = list.get(mid);
                left = mid + 1;
            } else {
                right = mid - 1;
            }
        }

        return answer;
    }
}