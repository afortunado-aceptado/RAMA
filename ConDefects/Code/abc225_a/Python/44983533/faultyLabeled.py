S = list(set(input()))
les = len(S)
if les == 3:
    print(6)
if les == 2: # Buggy line
    print(3)
else:
    print(1)