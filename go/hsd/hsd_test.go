package hsd

import (
	"reflect"
	"testing"
)

// func TestStringDistance(t *testing.T) {
// 	got := StringDistance("fio", "foh")
// 	want := 2
// 	if got != want {
// 		// その時点でテストを中断（t.Fatal）, t.Errorはエラー後もテストを続行。
// 		// 期待値と結果の両方を出力
// 		t.Fatalf("expected: %v, got%v", want, got)
// 		// t.Errorf("expected: %v, got%v", want, got)
// 	}
// }

// Table Driven Tests（テストケースをテーブルとしてまとめたもの）
func TestStringDistance(t *testing.T) {
	tests := []struct {
		name string
		lhs  string
		rhs  string
		want int
	}{
		// テストケースをまとめる(name:テスト名、lhs&foo:関数の引数, want:期待値)
		{name: "lhs is longer than rhs", lhs: "foot", rhs: "foo", want: -1},
		{name: "rhs is shorter than rhs", lhs: "foo", rhs: "foot", want: -1},
		{name: "diff 0", lhs: "foot", rhs: "foot", want: 0},
		{name: "diff 1", lhs: "foot", rhs: "foat", want: 1},
		{name: "diffs 2", lhs: "foots", rhs: "foatt", want: 2},
		{name: "diffs 3", lhs: "footts", rhs: "faotat", want: 3},
		{name: "diff 1", lhs: "こぞい", rhs: "こよい", want: 1},
	}
	for _, tc := range tests {
		got := StringDistance(tc.lhs, tc.rhs)
		if !reflect.DeepEqual(tc.want, got) {
			t.Fatalf("%s:expected: %v, git: %v", tc.name, tc.want, got)
		}
	}
}
