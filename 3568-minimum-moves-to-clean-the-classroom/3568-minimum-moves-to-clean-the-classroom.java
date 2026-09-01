import java.util.*;

class Solution {
    public int minMoves(String[] classroom, int energy) {
        int m = classroom.length;
        int n = classroom[0].length();

        List<int[]> litter = new ArrayList<>();
        int startR = 0, startC = 0;

        // Find S and all L cells
        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                char ch = classroom[i].charAt(j);

                if (ch == 'S') {
                    startR = i;
                    startC = j;
                } else if (ch == 'L') {
                    litter.add(new int[]{i, j});
                }
            }
        }

        int k = litter.size();

        // No litter to collect
        if (k == 0) {
            return 0;
        }

        // Map each litter cell to its bit index
        int[][] litterIndex = new int[m][n];
        for (int[] row : litterIndex) {
            Arrays.fill(row, -1);
        }

        for (int i = 0; i < k; i++) {
            int r = litter.get(i)[0];
            int c = litter.get(i)[1];
            litterIndex[r][c] = i;
        }

        int fullMask = (1 << k) - 1;

        /*
         * visited[r][c][energy][mask]
         *
         * energy ranges from 0 to energy
         * mask ranges from 0 to (1 << k) - 1
         */
        boolean[][][][] visited =
                new boolean[m][n][energy + 1][1 << k];

        Queue<State> queue = new ArrayDeque<>();

        queue.offer(new State(startR, startC, energy, 0));
        visited[startR][startC][energy][0] = true;

        int[] dr = {-1, 1, 0, 0};
        int[] dc = {0, 0, -1, 1};

        int moves = 0;

        while (!queue.isEmpty()) {
            int size = queue.size();

            while (size-- > 0) {
                State cur = queue.poll();

                int r = cur.r;
                int c = cur.c;
                int e = cur.energy;
                int mask = cur.mask;

                if (mask == fullMask) {
                    return moves;
                }

                // If energy is 0, cannot make another move
                // unless standing on R. But R resets immediately
                // when entered, so normally we never keep 0 on R.
                if (e == 0) {
                    continue;
                }

                for (int d = 0; d < 4; d++) {
                    int nr = r + dr[d];
                    int nc = c + dc[d];

                    if (nr < 0 || nr >= m || nc < 0 || nc >= n) {
                        continue;
                    }

                    if (classroom[nr].charAt(nc) == 'X') {
                        continue;
                    }

                    // Moving costs 1 energy
                    int newEnergy = e - 1;
                    int newMask = mask;

                    char cell = classroom[nr].charAt(nc);

                    // Collect litter
                    if (cell == 'L') {
                        int index = litterIndex[nr][nc];
                        newMask |= (1 << index);
                    }

                    // Reset energy
                    if (cell == 'R') {
                        newEnergy = energy;
                    }

                    if (!visited[nr][nc][newEnergy][newMask]) {
                        visited[nr][nc][newEnergy][newMask] = true;
                        queue.offer(
                            new State(nr, nc, newEnergy, newMask)
                        );
                    }
                }
            }

            moves++;
        }

        return -1;
    }

    static class State {
        int r;
        int c;
        int energy;
        int mask;

        State(int r, int c, int energy, int mask) {
            this.r = r;
            this.c = c;
            this.energy = energy;
            this.mask = mask;
        }
    }
}