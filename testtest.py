filterfile = []
with open('kernel_debug.txt', 'r') as file:
    for row in file.readlines():
        if 'fw4_5' in row:
            filterfile.append(row)
with open('filtered.txt', 'w+') as file:
    file.writelines(filterfile)
    
    
    
# filterfile = []
# with open('kernel_debug.txt', 'r') as file:
    # counter = 0
    # for row in file.readlines():
        # filterfile.append(row)
        # counter += 1
        # if counter > 20000:
            # break
# with open('shorted.txt', 'w+') as file:
    # file.writelines(filterfile)