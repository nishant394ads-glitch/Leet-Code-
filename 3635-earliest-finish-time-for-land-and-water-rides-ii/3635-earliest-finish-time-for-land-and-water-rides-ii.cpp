class Solution {
public:
    long long solveQuery(
        long long x,
        vector<int>& start,
        vector<int>& prefMinDur,
        vector<long long>& suffMinSum
    ) {
        int n = start.size();

        int pos = upper_bound(start.begin(), start.end(), x) - start.begin();

        long long ans = LLONG_MAX;

        // start <= x
        if (pos > 0) {
            ans = min(ans, x + (long long)prefMinDur[pos - 1]);
        }

        // start > x
        if (pos < n) {
            ans = min(ans, suffMinSum[pos]);
        }

        return ans;
    }

    int earliestFinishTime(vector<int>& landStartTime,
                           vector<int>& landDuration,
                           vector<int>& waterStartTime,
                           vector<int>& waterDuration) {

        int n = landStartTime.size();
        int m = waterStartTime.size();

        // ----- preprocess water rides -----
        vector<pair<int,int>> water;
        for (int i = 0; i < m; i++) {
            water.push_back({waterStartTime[i], waterDuration[i]});
        }
        sort(water.begin(), water.end());

        vector<int> wStart(m);
        vector<int> wPrefDur(m);
        vector<long long> wSuffSum(m);

        for (int i = 0; i < m; i++) {
            wStart[i] = water[i].first;

            if (i == 0)
                wPrefDur[i] = water[i].second;
            else
                wPrefDur[i] = min(wPrefDur[i - 1], water[i].second);
        }

        for (int i = m - 1; i >= 0; i--) {
            long long cur =
                (long long)water[i].first + water[i].second;

            if (i == m - 1)
                wSuffSum[i] = cur;
            else
                wSuffSum[i] = min(wSuffSum[i + 1], cur);
        }

        // ----- preprocess land rides -----
        vector<pair<int,int>> land;
        for (int i = 0; i < n; i++) {
            land.push_back({landStartTime[i], landDuration[i]});
        }
        sort(land.begin(), land.end());

        vector<int> lStart(n);
        vector<int> lPrefDur(n);
        vector<long long> lSuffSum(n);

        for (int i = 0; i < n; i++) {
            lStart[i] = land[i].first;

            if (i == 0)
                lPrefDur[i] = land[i].second;
            else
                lPrefDur[i] = min(lPrefDur[i - 1], land[i].second);
        }

        for (int i = n - 1; i >= 0; i--) {
            long long cur =
                (long long)land[i].first + land[i].second;

            if (i == n - 1)
                lSuffSum[i] = cur;
            else
                lSuffSum[i] = min(lSuffSum[i + 1], cur);
        }

        long long ans = LLONG_MAX;

        // Land -> Water
        for (int i = 0; i < n; i++) {
            long long landFinish =
                (long long)landStartTime[i] + landDuration[i];

            ans = min(ans,
                      solveQuery(landFinish,
                                 wStart,
                                 wPrefDur,
                                 wSuffSum));
        }

        // Water -> Land
        for (int i = 0; i < m; i++) {
            long long waterFinish =
                (long long)waterStartTime[i] + waterDuration[i];

            ans = min(ans,
                      solveQuery(waterFinish,
                                 lStart,
                                 lPrefDur,
                                 lSuffSum));
        }

        return (int)ans;
    }
};