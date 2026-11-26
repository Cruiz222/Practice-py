package main

import "fmt"

func findMinMax(numbers []int) (int, int) {
	min := numbers[0]
	max := numbers[0]

	for _, num := range numbers {
		if num > max {
			max = num
		}
		if num < min {
			min = num
		}
	}
	return max, min
}

func main() {
	num := []int{23, 5, 87, 8, 90}
	fmt.Println(findMinMax(num))
}
