// 题目描述：
// 给定一个整数数组 nums 和一个目标值 target，请你在该数组中找出和为目标值的那 两个 整数，并返回他们的数组下标。
// 你可以假设每种输入只会对应一个答案。但是，数组中同一个元素不能使用两遍。
// 示例:

// 给定 nums = [2, 7, 11, 15], target = 9

// 因为 nums[0] + nums[1] = 2 + 7 = 9
// 所以返回 [0, 1]

package main

import "fmt"

func twoSum(nums []int, target int) []int {
	for k1, _ := range nums {
		for k2 := k1 + 1; k2 < len(nums); k2++ {
			if target == nums[k1]+nums[k2] {
				return []int{k1, k2}
			}
		}
	}
	return []int{}
}

func main() {
	nums := []int{2, 7, 11, 15}
	var target int = 26
	fmt.Printf("%d\n", twoSum(nums, target))
}
