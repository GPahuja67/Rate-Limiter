def parse_request(line):

    user = line.strip()

    if not user:
        raise ValueError("User name cannot be empty")

    return user