
def leftToright(disk_list): # defining the left-to-right function and passing in the disk_list input

    n = len(disk_list) # setting n as the length of the disk_list

    for i in range(n): # outer loop which runs n times through the disk_list

        for j in range(0, n - 1): # inner loop which iterates from index 0 to n - 1 

            if disk_list[j] == 'dark' and disk_list[j+1] == 'light': # checks if a disk is 'dark' and that disk's right adjacent disk is 'light'
                
                disk_list[j], disk_list[j+1] = disk_list[j+1], disk_list[j] # when conditions met, swaps the disk with its adjacent right disk

    return disk_list # returns the sorted disk_list

userInput = input("Enter a disk list (ex. 'dark light dark'):  ") # taking in user input
disk_list = userInput.split() # splits string into an array of strings

diskListsorted = leftToright(disk_list) # assigning leftToright function to a variable

print(diskListsorted) # prints sorted disk_list, ex: ['light', 'light', 'light', 'light', 'dark', 'dark', 'dark', 'dark']