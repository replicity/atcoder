package main

import "fmt"

func main() {
	var X int
	fmt.Scan(&X)

	t := X % 100
	ans := 100 - t
	fmt.Println(ans)
}
