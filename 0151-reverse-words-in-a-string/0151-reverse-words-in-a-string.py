class Solution:
    def reverseWords(self, s: str) -> str:
        words = []

        word = ""

        for ch in s :
            if ch != " ":

                word += ch 

            elif word:

                words.append(word)
                word = ""

        if word:
            words.append(word)

        words.reverse()

        return " ".join(words)            