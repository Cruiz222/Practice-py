package main

import "fmt"

func find_max(number []int) int {
	max := number[0]

	for _, num := range number {
		if num > max {
			max = num
		}
	}
	return max
}

func main() {
	num := []int{12, 43, 56, 74, 89}
	fmt.Println(find_max(num))
}
