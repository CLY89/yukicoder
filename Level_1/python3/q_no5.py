length = int(input())
box_sum = int(input())
box_list = sorted(list(map(int, input().split())))

count = 0
for box in box_list:
    length -= box
    if length < 0:
        break
    count += 1

print(count)
