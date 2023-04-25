# Ken Leam G. Gamboa
# BSCPE 1-5
# This program will determine which text file where an integer 
# will be headed into by identifying if it is an even or odd number.

#read numbers text file, open even.txt, open odd.txt
with open("numbers.txt", "r") as num_file, open("even.txt", "a") as even_file, open("odd.txt") as odd_file:
    #for each line in numbers text file
    for line in num_file:
        #convert numbers into integers
        integer_value = int(line)
        #check the integers
        even_num = integer_value % 2
        #if even, append to even.txt
        if even_num == 0:
           even_file.write(str(integer_value) + "\n")
        #if odd, append to odd.txt
        else: 
            odd_file = integer_value