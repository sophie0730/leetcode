## 解題思路

因爲max heap的函式要到3.14版才有，所以也可以透過在value加上負數的方式，用min heap模擬出max_heap的效果
如果要使用max heap, 就是原有的method加上 `_max`就行