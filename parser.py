def parse_request(line):

    parts = line.strip().split()

    if len(parts) != 2:
        raise ValueError("Input must follow the format: <user> <timestamp>")

    user = parts[0]

    try:
        timestamp = int(parts[1])
    except:
        raise ValueError("Timestamp must be a valid integer value")

    return user, timestamp