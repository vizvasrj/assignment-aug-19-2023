#5. Implement a group_by_owners function that:
# ● Accepts a dictionary containing the file owner name for each file name.
# ● Returns a dictionary containing a list of file names for each owner name,
# in any order.
# For example, for dictionary
# {"Input.txt": "Randy", "Code.py": "Stan", "Output.txt": "Randy"}
# the group_by_owners function should return
# {"Randy": ["Input.txt", "Output.txt"], "Stan": ["Code.py"]}.

def group_by_owners(files: dict) -> dict:
    new_dict = {}
    for i, x in files.items():
        if x in new_dict:
            new_dict[x].append(i)
        else:
            new_dict[x] = [i]
    return new_dict

files = {
    "Input.txt": "Randy",
    "Code.py": "Stan",
    "Output.txt": "Randy"
}

print(group_by_owners(files))