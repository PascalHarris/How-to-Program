a = [None]*10 # Create an Array with 10 spaces in it.
for i in range (0,10): # Count from 0 to 9, putting the current value into i
    a[i] = chr(i+65) # Add i to 65 (which is A, remember), and store it in position i in the array.
for i in range (0,10): # Count from 0 to 9, putting the current value into i
    print (a[i]) # Print out the letter stored at position i in the array.
