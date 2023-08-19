#4. Return the Item with highest value count
items = [{"Delhi": 3}, {"Mumbai": 9}, {"Goa": 7}, {"Gujrat": 4}]

def itemWithHighestValue(items):
    max_val = 0
    max_val_item = None
    for x in items:
        for k, v in x.items():
            if v > max_val:
                max_val = v
                max_val_item = k
    return max_val_item

print(itemWithHighestValue(items))