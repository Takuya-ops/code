package hsd

func StringDistance(lhs, rhs string) int {
	return Distance([]rune(lhs), []rune(rhs))
}

func Distance(a, b []rune) int {
	dist := 0
	// 文字の長さが一致しない場合
	if len(a) != len(b) {
		return -1
	}
	// 互いの単語が同じであるか、１文字目から確認していく
	for i := range a {
		if a[i] != b[i] {
			dist++
		}
	}
	return dist
}
