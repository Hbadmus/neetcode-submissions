class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # brute force nested loop to check each number agsinst evry other num in list
        # compliment approch, get the number we are looking for and see if its in the list
        # but we need to keep in mind that we are returning the index so we need to keep track of that as well
        # This approch was o(n) because there is a nested loop we can do better
        # if i replace sec loop with a map we can just check if comp is in map if it is return index
        # search for an array is o(n) while search for a map is o(1) so making the array a map helps decrease time although it does inscrese space
        # tried a mapp solution and it only works if all the nums in the list are unique

        map = {}
            

        for i in range(len(nums)) : # giving us a new compliment 
            comp = target - nums[i]
            if comp in map :
                return [map[comp], i]
            else :
                map[nums[i]] = i

        return []