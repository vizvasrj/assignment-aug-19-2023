#2. count the occurrences of a particular element in the list and output
# highest occurring element
days = ["sun","mon","tue","wed","thu","fri","sun","mon","mon"]
def findMaxOccuringString(days):
    count = {}
    max_occ = 0
    max_occ_element = None
    for x in days:
        if x in count:
            count[x] += 1
        else:
            count[x] = 1
        if count[x] > max_occ:
            max_occ = count[x]
            max_occ_element = x

        
    return max_occ_element

print(findMaxOccuringString(days))
