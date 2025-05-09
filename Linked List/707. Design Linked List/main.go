package main

type MyLinkedList struct {
	Val  int
	Next *MyLinkedList
}

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

	return -1
}

func (this *MyLinkedList) AddAtHead(val int) {
	newNode := &MyLinkedList{
		Val:  val,
		Next: this.Next,
	}
	this.Next = newNode //不管怎樣 我直接加在sentinel node後面就好
}

func (this *MyLinkedList) AddAtTail(val int) {
	ptr := this
	for ptr.Next != nil {
		ptr = ptr.Next
	}
	ptr.Next = &MyLinkedList{
		Val:  val,
		Next: nil,
	}
}

func (this *MyLinkedList) AddAtIndex(index int, val int) {
	if index < 0 {
		return
	}

	if index == 0 {
		this.AddAtHead(val)
		return
	}

	ptr := this
	i := 0

	for ptr != nil && i < index {
		ptr = ptr.Next
		i++
	}
	if ptr == nil {
		return
	}

	newNode := &MyLinkedList{
		Val:  val,
		Next: ptr.Next,
	}

	ptr.Next = newNode
}

func (this *MyLinkedList) DeleteAtIndex(index int) {
	if index < 0 {
		return
	}

	ptr := this
	i := 0

	for ptr.Next != nil && i < index { //確保下一輪的ptr不會是nil
		ptr = ptr.Next
		i++
	}

	if ptr.Next == nil { //當我要刪除的節點是nil時
		return
	}

	ptr.Next = ptr.Next.Next
}

/**
 * Your MyLinkedList object will be instantiated and called as such:
 * obj := Constructor();
 * param_1 := obj.Get(index);
 * obj.AddAtHead(val);
 * obj.AddAtTail(val);
 * obj.AddAtIndex(index,val);
 * obj.DeleteAtIndex(index);
 */
