#3. Merge dictionaries a and b. The resultant dict must contain all items of
#both dicts. If key is common then the value of key in resultant dict
#must be the sum of value in a and b.
a = {"x": 1, "y": 2, "z": 3}
b = {"a": 4, "b": 5, "y": 6}
def dictMerge(a: dict, b: dict) -> dict:
    # create new dict so a and b can be merged
    new_dict = {}
    for k, v in a.items():
        new_dict[k] = v
    
    for k, v in b.items():
        if k in new_dict:
            new_dict[k] = new_dict[k] + v
        else:
            new_dict[k] = v

    return new_dict
print(dictMerge(a, b))