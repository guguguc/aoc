ALL_FIELDS = {"byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid", "cid"}
ALLOWED_MISS_FIELD = ["cid"]

def check_num(func):
    def wrap(value: str):
        return func(value) if value.isdigit() else False
    return wrap

@check_num
def check_byr(value: str):
    return len(value) == 4 and int(value) in range(1920, 2002+1)

@check_num
def check_iyr(value: str):
    return len(value) == 4 and int(value) in range(2010, 2020+1)

@check_num
def check_eyr(value: str):
    return len(value) == 4 and int(value) in range(2020, 2030+1)

@check_num
def check_pid(value: str):
    return len(value) == 9

def check_hgt(value: str):
    num, end = value[:-2], value[-2:]
    if not num.isdigit():
        return False
    num = int(num)
    if end == "cm":
        return num in range(150, 193+1)
    elif end == "in":
        return num in range(59, 76+1)
    else:
        return False

def check_hcl(value: str):
    if not value.startswith("#"): return False
    length = len(value)
    accept = set("0123456789abcdef")
    return length == 7 and set(value[1:]).issubset(accept)

def check_ecl(value: str):
    accept = {"amb", "blu", "brn", "gry", "grn", "hzl", "oth"}
    return value in accept

def check_cid(value: str):
    return True

CHECK_TABLE = {
        "byr": check_byr, "iyr": check_iyr,
        "eyr": check_eyr, "hgt": check_hgt,
        "hcl": check_hcl, "ecl": check_ecl,
        "pid": check_pid, "cid": check_cid, }

def check_fields(fields: list[str]) -> bool:
   diff = set(ALL_FIELDS).difference(set(fields))
   cond0 = not diff
   cond1 = not diff.difference(ALLOWED_MISS_FIELD)
   return cond0 or cond1

def check_item(key: str, val: str) -> bool:
    if key not in CHECK_TABLE.keys():
        return False
    return CHECK_TABLE[key](val)

def is_valid(item: dict):
    fields= item.keys()
    if not check_fields(fields):
        return False
    for field, value in item.items():
        if not check_item(field, value):
            return False
    return True
