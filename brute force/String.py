import sys
input = sys.stdin.readline

word1,word2 = input().split()

min_chai = 51

for i in range((len(word2)-len(word1))+1):
    chai = 0
    compair = word2[i:i+len(word1)]
    for j in range(len(compair)):
        if compair[j] != word1[j]:
            chai += 1
    min_chai = min(min_chai,chai)

print(min_chai)