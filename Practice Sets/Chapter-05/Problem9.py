# Can you change the values inside a list which is contained in set S?
# s = {8, 7, 12, "Harry", [1,2]}

s = {8, 7, 12, "Harry", [1,2]}

s[0][4] = 16  # Not Allowed In Python

# Ans: We can't change because;
    # -> We can not include list inside a set
    # -> We can not porformed the indexing operations
    # -> Not Hashable


