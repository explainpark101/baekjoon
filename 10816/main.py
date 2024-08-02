_ = input()
nums = input().split(" ")
numDict = {}
for num in nums:
    numDict[num] = numDict.get(num, 0) + 1
_ = input()
print(" ".join(map(str, (numDict.get(_, 0) for _ in input().split(" ")))))