import string

# Base62 characters
CHARS = string.digits + string.ascii_uppercase + string.ascii_lowercase
BASE = len(CHARS)

url_db = {}
id_counter = 1


def encode_base62(num):
    if num == 0:
        return CHARS[0]

    arr = []
    while num > 0:
        arr.append(CHARS[num % BASE])
        num //= BASE

    return ''.join(reversed(arr))


def decode_base62(short):
    num = 0
    for c in short:
        num = num * BASE + CHARS.index(c)
    return num


def shorten_url(long_url):
    global id_counter

    url_db[id_counter] = long_url
    short = encode_base62(id_counter)

    id_counter += 1
    return short


def get_original_url(short):
    id_val = decode_base62(short)
    return url_db.get(id_val)


# Example
short = shorten_url("https://google.com/search/python-system-design?q=base62+url+shortener")
print("Short URL:", short)

original = get_original_url(short)
print("Original URL:", original)