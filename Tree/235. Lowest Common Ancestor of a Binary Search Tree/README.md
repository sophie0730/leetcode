## 解題思路
這題如果能了解二元平衡樹的特性就可以解了。

一個二元平衡樹的左節點必定會小於根節點；右節點必定會大於根節點

根據題目敘述，其實就是要找到p和q的根節點為何

因此只要該節點小於p和q，就往左邊移動（讓值變小）
若大於p和q，就往右邊移動
直到找到兩者的根節點為止

## 時間複雜度
O(h), h為樹的深度

## 空間複雜度
O(1)