class Solution:
    def encode(self, strs: List[str]) -> str:
        encoded = ""
        for s in strs:
            encoded += str(len(s)) + '#' + s
        return encoded

    def decode(self, s: str) -> List[str]:
        strs = []
        offset = 0
        while offset < len(s):
            # finds first instance starting at offset
            hashIdx = s.find('#', offset)
            
            wordLength = int(s[offset:hashIdx])
            word = s[hashIdx+1:hashIdx+1+wordLength]
            strs.append(word)
            offset = hashIdx + wordLength + 1
        return strs