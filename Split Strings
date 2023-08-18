def solution(s):
    if s == []:
        return s
    s = list(s)
    
    if len(s) % 2 != 0:
        s.append("_")
        s = ["".join(s[i:i+2]) for i in range(0, len(s), 2)]
        return s
        
    s = ["".join(s[i:i+2]) for i in range(0, len(s), 2)]
    return s
