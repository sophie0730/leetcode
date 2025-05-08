## Problem Defined
設計一個資料結構，可以用來儲存time based key-value data, 每個key可以存多個不同timestamp的key-value, 並且可以依照key和time stamp拿到對應的value

要可以執行兩個動作：set data and get data

1. Data: key, (value, timestamp) 一對多的關係
2. Data Operation
    2.1 Set Data
        - 將value和timestamp存進對應的key
    2.2 Get Data
        - 取得在key中的value
        - 該value x必須符合time x <= timestamp, time x必須是符合該條件的最大值

## Building data structure