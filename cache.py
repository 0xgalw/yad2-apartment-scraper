

def load_cache_from_file():
    try:
        with open('cache.txt', 'r') as f:
            return set(f.read().splitlines())
    except FileNotFoundError:
        return set()


# Function that appends the local_cache to cache.txt
def save_cache_to_file():
    with open('cache.txt', 'w') as f:
        f.write('\n'.join(local_cache))

local_cache = load_cache_from_file()

