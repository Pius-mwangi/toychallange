def min_patches(S):
    num_patches = 0
    segment = 0
    
    while segment < len(S):
        if S[segment] == "X":
            num_patches += 1
            segment += 3
        else:
            segment += 1

    return num_patches

print(min_patches(".X..X"))  # Should print 2
print(min_patches("X.XXXXX.X."))  # Should print 3
print(min_patches("XX.XXX.."))  # Should print 2
print(min_patches("XXXX"))  # Should print 2
print(min_patches('.X...XX'))  # Should print 2
