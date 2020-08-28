// I cannot for the life of me figure out a quick solution to this problem
// a hhhhhwahping 39.916178952s
// decently easy though except for whatever solution is not 40 seconds long
package main
import ("fmt"
        "time"
        "strconv"
        "math"
)

func build(num int) (string, bool) {
  dividend := 0
  decimal := ""
  if num > 99 {
    dividend = 1000
    decimal += "00"
  } else if num > 9 {
    dividend = 100
    decimal += "0"
  } else {
    dividend = 10
  }
  divisor := num
  quotient := 0
  remainder := 0 
  for i := 0; i < 5000; i++ { // <------- This is the length of the decimal you want. it affects the time to run exponentially the higher it goes
    quotient = int(math.Floor(float64(dividend/divisor)))
    remainder = dividend % divisor
    dividend = remainder * 10
    if remainder == 0 {
      return "", true
    }
    decimal += strconv.Itoa(quotient)
  }
  return decimal, false
}

// the thinking for this is take every possible key and concatenate it with itself and it should match the decimal
// ie if key is 3212 then 321232123212 will match the decimal whereas 321321321 will not
func findpattern(decimal string) int {
  hashtable := map[string]bool{}
  shortest := 10000 // <------- if the pattern is 1234 this func will catch 12341234 as pattern and you want shortest one
  for i := 7; i < len(decimal); i++ { // <---- starting at 7 cuz we know from question that 6 is already the top dog
    hashtable[decimal[:i]] = true
  }
  for key, _ := range hashtable { // for the longest time i had no clue it iteratets "randomly" through the table instead of in insertion order
    match := ""
    for i := 0; i < 3; i++ {
      match += key
    }
    if len(match) > len(decimal) { // prevents runtime errors; if your string is too small the keys will be much bigger than it
      continue
    }
    if match == decimal[:len(match)] {
      if len(key) < shortest {
        shortest = len(key)
      }
    }
  }
  return shortest 
}

func main() {
  start := time.Now()
  maxlength := 0
  maxdecimal := 0
  for i := 1: i <= 1000; i++ {
    if i % 2 == 0 || i % 5 == 0 { // https://en.wikipedia.org/wiki/Repeating_decimal#Cyclic_numbers. only need coprime with 10 #s
      continue
    }
    decimal, terminated := build(i)
    if !terminated {
      length > maxlength {
        maxlength = length
        maxdecimal = i
      }
    }
  }
  fmt.Println(maxdecimal)
  fmt.Println(time.Since(start))
}
