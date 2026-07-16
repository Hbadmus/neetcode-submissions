class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # seeing if 2 strings have the same characters of each other
        # sorting : iterate and see if s(i) and t(i) are equal. sort log n, log n, o n (n log n) o(1)
        # hashmap : where you loop throigh both strings and places chacrters and
        # counts in the map then you check if the maps are equal to each other 
        # o (n) both

        map = {}

        if len(s) != len(t): return False

        for i in range(len(t)) :
            if s[i] in map :
                map[s[i]] += 1
            else :
                map[s[i]] = 1

            if t[i] in map :
                map[t[i]] -= 1
            else :
                map[t[i]] = -1
        
        return all(v == 0 for v in map.values())