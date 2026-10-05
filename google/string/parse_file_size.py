import re

def parse_size(size: str) -> int:
    size = size.strip()
    
    match = re.fullmatch(r"([0-9]+(?:\.[0-9]+)?)\s*([a-zA-Z]+)?", size)
    if not match:
        raise ValueError(f"Invalid format: {size}")

    number = float(match.group(1))
    unit  = match.group(2) or "B"
    unit = unit.lower()

    units = {
        "b": 1,
        "kb": 1000,
        "mb": 1000 ** 2,
        "gb": 1000 ** 3,
        "tb": 1000 ** 4,    

        "kib": 1024,
        "mib": 1024 ** 2,
        "gib": 1024 ** 3,
        "tib": 1024 ** 4,
    }

    if unit not in units:
       raise ValueError(f"Invalid Unit: {unit}")
   
    return int(number * units[unit]) 

def main():
    test_cases = ["500 kb", "1000 kib", "712MIB", "1 GB", "20 Tib"]
    
    for case in test_cases:
        size = parse_size(case)

        print(f"{case} is {size} bytes")


if __name__ == "__main__":
    main()

