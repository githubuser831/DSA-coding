class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        alpha = ["a", "b", "c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","y","x","z"]
        res = []
        ser = []
        a = len(alpha)
        for i in range(a):
            res.append(s.count(alpha[i]))
            ser.append(t.count(alpha[i]))
        r = len(res)
        s = len(ser)
        if r != s:
            return False
        else:
            for j in range(r):
                if res[j] != ser[j]:
                    return False
            return True
