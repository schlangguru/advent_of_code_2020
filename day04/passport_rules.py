import re

REQUIRED_FIELDS = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]
HEIGHT_PATTERN = re.compile(r"(\d+)(cm|in)")
HAIR_COLOR_PATTERN = re.compile(r"^#[0-9a-f]{6}$")
PID_PATTERN = re.compile(r"^\d{9}$")

def is_valid(document):
    """
    Applies all rules to the document.
    """
    if not has_required_fields(document):
        return False

    checks = [
        is_birthday_valid,
        is_issue_year_valid,
        is_expiration_date_valid,
        is_height_valid,
        is_hair_color_valid,
        is_eye_color_valid,
        is_pid_valid,
        is_cid_valid
    ]

    return all([check(document) for check in checks])

def has_required_fields(document):
    """
    Checks if the document has all required fields.
    """
    keys = document.keys()
    return all([key in keys for key in REQUIRED_FIELDS])

def is_birthday_valid(document):
    """
    Checks if the 'byr' field is valid.
    """
    return _is_between(int(document["byr"]), 1920, 2002)

def is_issue_year_valid(document):
    """
    Checks if the 'iyr' field is valid.
    """
    return _is_between(int(document["iyr"]), 2010, 2020)

def is_expiration_date_valid(document):
    """
    Checks if the 'eyr' field is valid.
    """
    return _is_between(int(document["eyr"]), 2020, 2030)

def is_height_valid(document):
    """
    Checks if the 'hgt' field is valid
    """
    match = HEIGHT_PATTERN.match(document["hgt"])
    if match:
        height = int(match.group(1))
        unit = match.group(2)
        if unit == "cm" and _is_between(height, 150, 193):
            return True
        if unit == "in" and _is_between(height, 59, 76):
            return True

    return False

def is_hair_color_valid(document):
    """
    Checks if the 'hcl' field is valid.
    """
    return bool(HAIR_COLOR_PATTERN.match(document["hcl"]))

def is_eye_color_valid(document):
    """
    Checks if the 'ecl' field is valid.
    """
    return document["ecl"] in ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]

def is_pid_valid(document):
    """
    Checks if the 'pid' field is valid.
    """
    return bool(PID_PATTERN.match(document["pid"]))

def is_cid_valid(document):
    """
    The 'cid' id always valid ;-)
    """
    return True

def _is_between(value, min, max):
    """
    Checks if value is between (inclusive) min and max.
    """
    return min <= value and value <= max