dict1 = {"apple": 60, "banana": 30}
dict2 = {"watermelon": 40, "mango": 100}
dict3 = {"grapes": 60, "pineapple": 40}

dict4 = {**dict1, **dict2, **dict3}

print("Merged Dictionary 4:", dict4)