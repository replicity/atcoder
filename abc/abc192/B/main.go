package main

import (
	"fmt"
	"unicode"
)

func main() {
	var S string
	fmt.Scan(&S)
	for i, c := range S {
		if i%2 == 0 {
			if unicode.IsUpper(c) {
				fmt.Println("No")
				return
			}
		} else {
			if unicode.IsLower(c) {
				fmt.Println("No")
				return
			}
		}
	}

	fmt.Println("Yes")
	return
}
