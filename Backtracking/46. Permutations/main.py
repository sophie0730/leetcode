class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        if len(nums) == 1:
            return [nums[:]]

        res = []

        for _ in range(len(nums)):
            n = nums.pop()

            perm = self.permute(nums)

            for p in perm:
                p.append(n)

            res.extend(perm)
            nums.append(n)

        return res


# 這一題是要找到每個數字的不同排列組合
# 我們可以一次提取一個數字，針對剩下的數字做遞迴，就可以得到該數字＋剩下兩個數字不同排列組合的list
# 將這個list: perm,記錄到答案後
# 在把提取的數字加回到數組，接著回圈走到下一個數字，再去看下一個數字加上剩下兩個數字不同的排列組合

# [1,2,3]
#         /              |              \\
#     取1[2,3]        取2[3,1]        取3[1,2]
#     /    \\          /    \\          /    \\
# 取2[3] 取3[2]    取3[1] 取1[3]    取1[2] 取2[1]
#   |      |        |      |        |      |
# [3,2,1][2,3,1] [1,3,2][3,1,2] [2,1,3][1,2,3]

# Time Complexity: O(n * n!) 每個數組要製作O(n)時間，遞迴總共需花n!時間 n為數組個數
# Space Complexity: O(n) 遞迴的深度
