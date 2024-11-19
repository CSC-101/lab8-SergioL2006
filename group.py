def groups_of_3(group:list[int]) -> list[list[int]]:
    x = 0 #beginner index to add
    j = 2 #iterates between indexes every 3, beginning from 2 as first 3 in list is 0, 1, 2
    allgroups = [] #where all groups are stored

    while j <= len(group)+1: #ensures that it iterates through, even containing 1 element
        templist = [] #used to create each group
        while x <= j and x <= len(group)-1: #has to have both checks to iterate through towards j and ensure the index does not go out of range
            templist.append(group[x]) #appends the members of the first group
            x += 1 #moves on to new member until it reaches j the end of the group
        allgroups.append(templist) #appends the newly made group
        j += 3 #has it iterate through the next members if they are there

    return allgroups #returns new groups