from typing import List


def cellsInRange(s: str) -> List[str]:
    letters = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
    output = []
    start, finish = s.split(":")
    for i in range(ord(start[0]), ord(finish[0]) + 1):
        for num in range(int(start[1]), int(finish[1]) + 1):
            output.append(f"{chr(i)}{num}")
    return output
s = "A1:F1"
print(cellsInRange(s))
    