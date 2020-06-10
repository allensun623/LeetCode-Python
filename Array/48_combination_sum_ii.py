class Solution(object):
    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        """
        My first solution
        """
        def find_sum(target, index, temp, results):
            while index < len(candidates):
                next_target = target - candidates[index]
                print("============")
                print("candidates", candidates)
                print("temp", temp)
                print("target", target)
                print("index", index)
                print("candidates[index]", candidates[index])
                print("next_target", next_target)
                print("results", results)
                if next_target < 0:
                    break
                elif next_target == 0:
                    results.append(temp+[candidates[index]])
                    break
                else:
                    results = find_sum(next_target, index+1, temp+[candidates[index]], results)
                
                index += 1
                        
            return results
            
        
        candidates.sort()
        return find_sum(target, 0, [], [])  