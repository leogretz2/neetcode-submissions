class Solution:
    # extra # at end (?)
    def encode(self, strs: List[str]) -> str:
        encoded = ""
        for s in strs:
            encoded += str(len(s)) + '#' + s
        return encoded

    def decode(self, s: str) -> List[str]:
        strs = []
        current = ""
        while len(s):
            # finds first instance
            firstHash = s.find('#')
            wordLength = int(s[:firstHash])
            word = s[firstHash+1:firstHash+1+wordLength]
            strs += [word]
            # do another non-destructive version
            s = s[firstHash+1+wordLength:]
        # for c in s:
        #     if c != '\t':
        #         current += c
        #     else:
        #         strs += [current]
        #         current = ""
        return strs