func reverse(x int) int {
	temp := x
	var ret int
	for {
		if temp == 0 {
			if ret > int(math.Pow(2, 31)-1) || ret < int(math.Pow(-2, 31)) {
				return 0
			}
			return ret
		} else {
			ret = ret*10 + temp%10
			temp = temp / 10
		}

	}
	return ret
}