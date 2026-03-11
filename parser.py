def parse_request(line):

    parts = line.strip().split()

    if len(parts) != 2:
        raise ValueError("Invalid input format")

    user = parts[0]

    try:
        timestamp = int(parts[1])
    except:
        raise ValueError("Timestamp must be an integer")

    return user, timestamp