## 解題思路
假設題目給定的樹長這樣：
```
    1
   / \
  2   3
 /
4
```
透過遞迴的方式，分別計算左子樹和右子樹的最大深度，每一層往下延伸，直到碰到空節點（也就是終止條件）
兩邊取較大的深度，然後加上1，因為要包含root那一層

在遞迴中，
maxDepth(1)會呼叫：
- maxDepth(2) -> maxDepth(4) -> maxDepth(none)回傳0 -> 所以maxDepth(4) 回傳1, maxDepth(2)回傳2
- maxDepth(3)回傳1

- maxDepth(1) = max(maxDepth(2), maxDepth(3)) == max(1, 2) + 1 = 3

時間複雜度: O(n) 每個節點只會訪問一次，每次訪問都是常數操作
空間複雜度: O(h) 每次call function都會增加一個call stack, stack的深度就是樹的高度