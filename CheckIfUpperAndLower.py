def greatestLetter(s: str) -> str:
    greatest = None
    s = set(s)
    print(s)
    for c in s:
        if c.upper() in s and c.lower() in s:
            greatest = max(greatest, c.upper()) if greatest else c.upper()
    return '' if not greatest else greatest
    

s = "arRAzFif"
print(greatestLetter(s))