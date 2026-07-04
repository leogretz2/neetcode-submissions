class Solution:
    def isValid(self, s: str) -> bool:
        roundCount, curlyCount, bracketCount = 0,0,0
        lastOpen = []
        for c in s:
            print(c, lastOpen)
            match c:
                case '(':
                    roundCount += 1
                    lastOpen.append('(')
                case ')':
                    roundCount -= 1
                    if lastOpen and lastOpen[-1] == '(':
                        lastOpen.pop()
                    else:
                        return False
                case '{':
                    curlyCount += 1
                    lastOpen.append('{')
                case '}':
                    curlyCount -= 1
                    if lastOpen and lastOpen[-1] == '{':
                        lastOpen.pop()
                    else:
                        return False
                case '[':
                    bracketCount += 1
                    lastOpen.append('[')
                case ']':
                    bracketCount -= 1
                    if lastOpen and lastOpen[-1] == '[':
                        lastOpen.pop()
                    else:
                        return False

            if roundCount < 0 or curlyCount < 0 or bracketCount < 0:
                return False

        return roundCount == 0 and curlyCount == 0 and bracketCount == 0