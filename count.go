package main

import (
	"strings"
)

func count_vowels(texts string) int {
	words := strings.ToLower(texts)
	vowels := "aeiou"
	count := 0

	for _, letter := range words {
		if strings.ContainsRune(vowels, letter) {
			count++
		}
	}
	return count
}

func main() {
	fmt.println(count_vowels("hello, welcome"))
}
