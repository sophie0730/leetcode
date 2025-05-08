package main

type TimeMap struct {
	KeyMap map[string][]Pair
}

type Pair struct {
	val       string
	timestamp int
}

func Constructor() TimeMap {
	return TimeMap{
		KeyMap: make(map[string][]Pair),
	}
}

func (this *TimeMap) Set(key string, value string, timestamp int) {
	pairObj := Pair{
		val:       value,
		timestamp: timestamp,
	}

	if _, ok := this.KeyMap[key]; !ok {
		this.KeyMap[key] = make([]Pair, 0)
	}
	this.KeyMap[key] = append(this.KeyMap[key], pairObj)
}

func (this *TimeMap) Get(key string, timestamp int) string {
	if _, ok := this.KeyMap[key]; !ok {
		return ""
	}
	arr := this.KeyMap[key]
	if arr[0].timestamp > timestamp {
		return ""
	}

	left := 0
	right := len(arr) - 1

	for left < right {
		mid := left + (right-left)/2
		if arr[mid].timestamp == timestamp {
			return arr[mid].val
		} else if arr[mid].timestamp > timestamp {
			right = mid - 1
		} else {
			left = mid + 1
		}
	}

	if arr[left].timestamp > timestamp {
		return arr[left-1].val
	}
	return arr[left].val
}

/**
 * Your TimeMap object will be instantiated and called as such:
 * obj := Constructor();
 * obj.Set(key,value,timestamp);
 * param_2 := obj.Get(key,timestamp);
 */
