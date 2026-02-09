## 解題思路

如圖，課程的依賴關係可以畫成graph
當節點可以形成一個閉環時，就代表我們沒辦法完成所有課程

所以 我們可以使用set 來記錄走過的節點
這樣當有重複的節點出現在set時，我們就知道已經形成了一個閉環，return False

這一題使用dfs是因為我們要知道course的prerequistite, prerequisite的prerequisite有哪些
根據圖示，就要利用深度優先搜尋來找出這個關聯性
每找到一個prerequisite，就會檢查一遍這個節點是否出現在set當中


設 `V = numCourses`（節點數），`E = len(prerequisites)`（邊數
- Time Complexity: O(V+E) 課程總數量加上節點深度
  - 設 `V = numCourses`（節點數），`E = len(prerequisites)`（邊數)
  - 建圖：遍歷 `prerequisites`，**O(E)
  - DFS：每個節點最多訪問一次（完成後 `pre[course] = []` 剪枝），每條邊最多走一次，**O(V + E)
- Space Complexity: O(V+E)
  - pre` 鄰接表：儲存所有邊，O(V + E)
  - `taken` 集合：最多 O(V)
  - DFS 遞迴呼叫堆疊：最深 **O(V)
