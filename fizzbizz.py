input_num = int(raw_input("Count to number between 1 and 100: "))
for x in range(input_num):
    if (x + 1) % 3 == 0 and (x + 1) % 5 == 0:
        print ("fizzbuzz")
    elif (x + 1) % 3 == 0:
        print ("fizz")
    elif (x + 1) % 5 == 0:
        print ("buzz")
    else:
        print (x+1)
