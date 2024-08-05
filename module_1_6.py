my_dict = {"Вася": 1985, "Петя": 1995}
print("Dict:", my_dict)
print("Existing value:", my_dict.get("Вася"))
print("Not existing value:", my_dict.get("Коля"))
my_dict["Kamila"] = 1990
my_dict["Artem"] = 2000
deleted_value = my_dict.pop("Петя")
print("Deleted value:", deleted_value)
print("Modified dictionari:",my_dict)
print()

my_set = {1, "Яблоко", 42.314, 1, "Яблоко", (5, 6, 1.6)}
print("Set:", my_set)
my_set.add(13)
my_set.add(("Яблоко", "Груша"))
my_set.remove(1)
print("Modified set:", my_set)