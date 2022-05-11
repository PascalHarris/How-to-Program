5 dim fizzbuzz as string
10 for i = 1 to 100 step 1
20 fizzbuzz = ""
30 if i mod 3 = 0 then fizzbuzz = "fizz"
40 if i mod 5 = 0 then fizzbuzz = fizzbuzz+"buzz"
50 if i mod 3 <> 0 and i mod 5 <> 0 then fizzbuzz = i 60 print fizzbuzz
70 next i
