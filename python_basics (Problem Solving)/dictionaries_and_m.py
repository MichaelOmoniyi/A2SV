# Enter your code here. Read input from STDIN. Print output to STDOUT
import sys

n = int(input())
entries = [input().split() for _ in range(n)]
queries = [line.strip() for line in sys.stdin]

phonebook = {}

for entry in entries:
    phonebook[entry[0]] = entry[1]
    
for query in queries:
    if query in phonebook:
        print(f"{query}={phonebook[query]}")
    else:
        print("Not found")