import re

def is_valid_email(email):
    if not email:
        return False
    pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'
    if re.match(pattern, email):
        if email.startswith(("info@", "admin@", "contact@")):
            return False
        return True
    return False


def remove_duplicates(data):
    seen = set()
    result = []

    for item in data:
        if item["email"] not in seen:
            seen.add(item["email"])
            result.append(item)

    return result