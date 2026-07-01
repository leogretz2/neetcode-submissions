class Solution:
    # extra # at end (?)
    def encode(self, strs: List[str]) -> str:
        encoded = ""
        for s in strs:
            encoded += str(len(s)) + '#' + s
        return encoded

    def decode(self, s: str) -> List[str]:
        strs = []
        offset = 0
        while offset < len(s):
            # finds first instance
            newOffset = offset + s[offset:].find('#')
            # print(offset, s[:offset], s)

            wordLength = int(s[offset:newOffset])
            word = s[newOffset+1:newOffset+1+wordLength]
            strs += [word]
            offset = newOffset + wordLength + 1
            # do another non-destructive version
            # s = s[firstHash+1+wordLength:]
        return strs