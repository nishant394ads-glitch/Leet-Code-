class Solution {
public:

    struct TrieNode {
        int child[26];
        int bestIndex;
        int bestLen;

        TrieNode() {
            memset(child, -1, sizeof(child));
            bestIndex = -1;
            bestLen = INT_MAX;
        }
    };

    vector<TrieNode> trie;

    void updateNode(int node, int idx, int len) {
        if (len < trie[node].bestLen) {
            trie[node].bestLen = len;
            trie[node].bestIndex = idx;
        }
    }

    vector<int> stringIndices(vector<string>& wordsContainer,
                              vector<string>& wordsQuery) {

        trie.reserve(500000 + 5);
        trie.push_back(TrieNode()); // root

        // Build Trie
        for (int i = 0; i < wordsContainer.size(); i++) {

            string &s = wordsContainer[i];
            int len = s.size();

            int node = 0;

            updateNode(node, i, len);

            for (int j = len - 1; j >= 0; j--) {

                int c = s[j] - 'a';

                if (trie[node].child[c] == -1) {
                    trie[node].child[c] = trie.size();
                    trie.push_back(TrieNode());
                }

                node = trie[node].child[c];

                updateNode(node, i, len);
            }
        }

        vector<int> ans;

        // Process queries
        for (string &q : wordsQuery) {

            int node = 0;

            for (int j = q.size() - 1; j >= 0; j--) {

                int c = q[j] - 'a';

                if (trie[node].child[c] == -1)
                    break;

                node = trie[node].child[c];
            }

            ans.push_back(trie[node].bestIndex);
        }

        return ans;
    }
};