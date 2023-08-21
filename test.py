

from typing import List

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        strs_table={}
        for string in strs:
            sorted_string= ''.join(sorted(string))
            print(sorted_string)

            
            
Solution().groupAnagrams(["eat","tea","tan","ate","nat","bat"])

# insert-delete-getrandom-o1-duplicates-allowed/

import random

class RandomizedCollection:

    def __init__(self):
        self.stack=[]

    def insert(self, val: int) -> bool:
        if val not in self.stack:
            self.stack.append(val)
            return True  
        else:      
            self.stack.append(val)
            return False


    def remove(self, val: int) -> bool:
        if val in self.stack:
            self.stack.remove(val)
            return True
        else:
            return False

    def getRandom(self) -> int:
        return random.choice(self.stack)


# Your RandomizedCollection object will be instantiated and called as such:
# obj = RandomizedCollection()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()


## number of islands

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0

        count =0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j]=="1":
                    self.dfs(grid,i,j)
                    count+=1

        return count


    def dfs(self,grid,i,j):
        if i<0 or j<0 or i>=len(grid) or j>=len(grid[0]) or grid[i][j] !="1":
            return
        grid[i][j]="#"
        self.dfs(grid,i+1,j)
        self.dfs(grid,i-1,j)
        self.dfs(grid,i,j+1)
        self.dfs(grid,i,j-1)
        

## insert-delete-getrandom-o1


class RandomizedSet:

    def __init__(self):
        self.data_map={}
        self.data=[]

    def insert(self, val: int) -> bool:
        if val in self.data_map:
            return False
        
        self.data_map[val]=len(self.data)

        self.data.append(val)

        return True

    def remove(self, val: int) -> bool:
        if not val in self.data_map:
            return False
        
        last_elem_in_list=self.data[-1]
        index_of_elem_to_remove = self.data_map[val]

        self.data_map[last_elem_in_list]= index_of_elem_to_remove
        self.data[index_of_elem_to_remove]=last_elem_in_list

        self.data[-1]=val

        self.data.pop()

        self.data_map.pop(val)

        return True

    def getRandom(self) -> int:
        return random.choice(self.data)


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()


import random

class RandomizedSet:

    def __init__(self):
        # Initialize Set
        self.sets = set()

    def insert(self, val: int) -> bool:
        # If n is present in set then return false
        if val in self.sets : 
            return False
        
        # If n is not present in set then add it to the set.
        self.sets.add(val)
        return True

    def remove(self, val: int) -> bool:
        # If n is in set then remove n else return false
        if val in self.sets:
            self.sets.remove(val)
            return True
        return False

    def getRandom(self) -> int:
        # Return random number using random module
        return random.choice(list(self.sets))

## lru-cache

class LRUCache:

    def __init__(self, capacity: int):
        self.dic={}
        self.capacity = capacity

    def get(self, key: int) -> int:
        if key not in self.dic:
            return -1
        val = self.dic.pop(key)
        self.dic[key]=val
        return val

    def put(self, key: int, value: int) -> None:
        if key in self.dic:
            self.dic.pop(key)
        else:
            if self.capacity == len(self.dic):
                print(next(iter(self.dic)))
                del self.dic[next(iter(self.dic))]
        self.dic[key]=value

        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)