// Using exponent * log(base) instead of math/big package was hilariously different in time
// 6.650204ms (vs 1st attempt 14minutes)
package main

import ("fmt"
        "strings"
        "math"
        "io/ioutil"
        "strconv"
        "time")


func main() {
  start := time.Now()
  data2, _ := ioutil.ReadFile("base_exp.txt")
  data := strings.Split(string(data2), "\n")
  max := float64(0)
  answer := 0
  for index, line := range(data) {
    if index % 100 == 0 {fmt.Println(index, line,time.Since(start))}
    base, _ := strconv.Atoi(strings.Split(line, ",")[0])
    exponent, _ := strconv.Atoi(strings.Split(line, ",")[1])
    contender := float64(exponent) * math.Log10(float64(base)) // this one line change saves 14 minutes
    if contender > max {
      max = contender
      answer = index + 1
    }
  }
  fmt.Println(answer, time.Since(start))
}
