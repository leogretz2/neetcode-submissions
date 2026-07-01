class Solution:
    # doesn't solve ""
    def encode(self, strs: List[str]) -> str:
        encoded = ""
        for s in strs:
            
            encoded += s + '\t'
        return encoded

    def decode(self, s: str) -> List[str]:
        strs = []
        current = ""
        for c in s:
            if c != '\t':
                current += c
            else:
                strs += [current]
                current = ""
        return strs