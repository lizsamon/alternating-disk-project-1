disk_list = ['dark', 'light', 'dark', 'light', 'dark', 'light', 'dark', 'light'] # initializing unsorted disk list as an array of strings

def leftToright(disk_list): # defining the left-to-right function and passing in the disk_list input

    n = len(disk_list) // 2 # setting n as half the length of the disk_list since there are 2n disks in total

    for i in range(n): # outer loop which iterates n times through the disk_list

        for j in range(1,2*n): # inner loop which iterates from index 1 to 2n-1 

            if disk_list[j] == 'light' and disk_list[j-1] == 'dark': # if a disk is 'light' and that disk's left adjacent disk is 'dark', swap 
                
                disk_list[j], disk_list[j-1] = disk_list[j-1], disk_list[j] # swaps the right disk with its adjacent left disk

    return disk_list # returns the sorted disk_list


diskListsorted = leftToright(disk_list) # assigning leftToright function to a variable

print(diskListsorted) # prints sorted disk_list: ['light', 'light', 'light', 'light', 'dark', 'dark', 'dark', 'dark']