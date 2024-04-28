# 2 lists having some commom items in them
list1 = [1, 6, 7, 4, 5, 2, 3, 8, 9]
list2 = [2, 3, 4, 5, 6, 7, 8, 9, 10]

# merging the two lists
list3 = list1 + list2
print(f"List3: {list3}\n")
# removing the duplicates
list4 = list(set(list3))
print(f"List4: {list4}\n")
# sorting the list
list4.sort()
print(f"Sorted List: {list4}\n")

print("--------------------------------------------------")

# Now give 2 lists with common string items
list1 = ["a", "b", "c", "d", "e"]
list2 = ["c", "d", "e", "f", "g"]
# merging the two lists
list3 = list1 + list2
print(f"List3: {list3}\n")
# removing the duplicates
list4 = list(set(list3))
print(f"List4: {list4}\n")
# sorting the list
list5 = sorted(list4)
print(f"List5: {list5}\n")

