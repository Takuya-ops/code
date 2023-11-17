package main

import (
	"fmt"
	"sample/hsd" //go mod initで指定した名前/packageのディレクトリの順で書く。
)

func main() {
	fmt.Println("Hello")
	hsd.Distance()

}
