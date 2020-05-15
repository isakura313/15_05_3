def adder(*nums):
    sum = 0

    for n in nums:
        sum += n
    print("sum: ", sum)


adder(3, 5)
adder(3, 5, 5)
adder(3, 5, 5, 6)
adder(3, 5, 5, 6, 8)
