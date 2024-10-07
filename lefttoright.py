disk_list = ["dark", "light", "dark", "light", "dark", "light", "dark", "light"] # initializing disk list as an array of strings

def leftToright(disk_list): 

    n = len(disk_list) // 2 

    for i in range(n):
        for j in range(1,2*n):
            if disk_list[j] == 'light' and disk_list[j-1] == 'dark':
                disk_list[j], disk_list[j-1] = disk_list[j-1], disk_list[j]

    return disk_list


diskListsorted = leftToright(disk_list)

print(diskListsorted)