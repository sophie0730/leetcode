# Notes
### 時間複雜度
- 基本的Linked List操作，時間複雜度：
    - 查詢：O(n)
    - Add node at Head: O(1)
    - Add node at specific index: O(n)
    - Delete node at specific index: O(n)

### 記憶體配置
- 當我們要宣告一個新的struct時，如果在function裏直接宣告，他會在function的記憶體(stack)中再另外assign一塊記憶體放置struct (pass by value)
- 如果我們想要加快運算速度，並針對原始的struct做修改，在宣告時，要將struct的指標傳入到變數當中，再將這個指標assign到Next
```
newNode := &MyLinkdedList{
    Val: val,
    Next: nil
}
this.Next = newNode
```

### sentinel node for constuctor
因為我們的資料結構是長這樣的：
```go
type MyLinkedList struct {
	Val  int
	Next *MyLinkedList
}
```
如果我們想要添加head node, 當該LinkedList沒有head node時，只靠這個資料結構會報錯，我們需要額外加一個struct來去紀錄head
```go
type LinkedList struct {
    head *Node
}

type Node struct {
    Val int
    Next *Node
}
```

如果不想要這麼麻煩，一開始在construct的時候可以加入一個sentinel node，他實際上不會被使用，在搜尋的時候跳過他即可

```go
func Constructor() MyLinkedList {
	return MyLinkedList{
		Val:  -999,
		Next: nil,
	} //建立一個sentinel node

}

func (this *MyLinkedList) Get(index int) int {
	if index < 0 {
		return -1
	}
	ptr := this.Next //略過sentinel node
	i := 0
	for ptr != nil {
		if i == index {
			return ptr.Val
		}
		ptr = ptr.Next
		i++
	}
 //...
}
```

要加入head node時，不管一開始有沒有head，加在sentinel node後面就行了
```go
func (this *MyLinkedList) AddAtHead(val int) {
	newNode := &MyLinkedList{
		Val:  val,
		Next: this.Next, //直接指向sentinel node指向的那個node，加在他的前面（是nil也無仿）
	}
	this.Next = newNode //不管怎樣 我直接加在sentinel node後面就好
}
```


### 例外狀況
- 當使用迴圈走到指定的index時，要注意例外狀況與邊界，要記得我們不能操控一個空的記憶體，所以當：
```
ptr.Next = ptr.Next.Next
```
如果ptr或者ptr.Next為nil，就會出錯