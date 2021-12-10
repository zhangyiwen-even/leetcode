package main
import "fmt"
func Swap(arr []int, i, j int) {
	arr[i], arr[j] = arr[j], arr[i]
}

func MaoPaoSort(arr []int) {
	for i := 0; i < len(arr); i++ {
        for j := i j < len(arr)-i; j++ {
			if arr[j] < arr[j-1] {
				Swap(arr,j,j-1)
			}
		}
	}
}

func main() {
	arr := []int{5,3,1,2,6,4}
	MaoPaoSort(arr)
	fmt.Println(arr)
}