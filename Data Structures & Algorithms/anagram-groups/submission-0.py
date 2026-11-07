from collections import Counter

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagram_buckets = defaultdict(list)
    
        for word in strs:
            # Create a fixed-size count array for the 26 letters of the alphabet
            count = [0] * 26
            
            for char in word:
                # 1. TODO: How do we increment the position in 'count' for this char?
                # Hint: ord(char) - ord('a') gives you a number from 0 to 25
                count[ord(char) - ord('a')] += 1

                pass
                
            # 2. TODO: Convert 'count' to a tuple so it can be a dictionary key, 
            # and append the original 'word' into anagram_buckets at that key.
            countTuple = tuple(count)
            anagram_buckets[countTuple].append(word)     
            pass
            
        # Return all the grouped lists together
        return list(anagram_buckets.values())