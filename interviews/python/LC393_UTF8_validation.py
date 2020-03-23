from typing import List

def validUtf8(data: List[int]) -> bool:
    count = 0

    for byte in data:
        if byte >= 128 and byte <= 191:
            if not count:
                return False
            count -= 1
        else:
            if count:
                return False
            if byte < 128:
                continue
            elif byte < 224:
                count = 1
            elif byte < 240:
                count = 2
            elif byte < 248:
                count = 3
            else:
                return False

    return count == 0

print(validUtf8([197, 130, 1]))
print(validUtf8([235, 140, 4]))
