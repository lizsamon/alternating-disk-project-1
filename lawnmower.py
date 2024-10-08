def lawnmower(disk_list): # defining the lawnmower function and passing in the disk_list input

    n = len(disk_list) // 2 # setting n as half the length of the disk_list since there are 2n disks in total

    for i in range(n): # outer loop which runs n/2 times through the disk_list 

        for j in range(0, len(disk_list) - 1): # left to right inner loop which iterates from the first index to the last index

            if disk_list[j] == 'dark' and disk_list[j+1] == 'light': # checks if the disk is dark and its right adjacent disk is light

                disk_list[j], disk_list[j+1] = disk_list[j+1], disk_list[j] # when condition met, swaps the disk with it's right adjacent disk

        for j in range(len(disk_list) - 1, 0, -1): # right to left inner loop which iterates from the last index to the first index
             
             if disk_list[j] == 'light' and disk_list[j-1] == 'dark': # checks if the disk is light and its left adjacent disk is dark
                 
                 disk_list[j], disk_list[j-1] = disk_list[j-1], disk_list[j] #when condition is met, swaps the disk with it's left adjacent disk
                        

    return disk_list # returns the sorted disk_list

userInput = input("Enter a disk list (ex. 'dark light dark'):  ") # taking in user input
disk_list = userInput.split() # splits string into an array of strings

diskListsorted = lawnmower(disk_list) # assigning lawnmower function to a variable

print(diskListsorted) # prints the sorted disk_list, ex: ['light', 'light', 'light', 'light', 'dark', 'dark', 'dark', 'dark']