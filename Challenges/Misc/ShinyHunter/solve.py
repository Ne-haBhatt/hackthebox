import random

def lcg(seed, a=1664525, c=1013904223, m=2**32):
    return (a * seed + c) % m

def generate_ids(seed):
    random.seed(seed)
    tid = random.randint(0, 65535)
    sid = random.randint(0, 65535)
    return tid, sid

def generate_poketmon(seed, tid, sid, name):
    random.seed(seed)
    stats = {
        "HP": random.randint(20, 31),
        "Attack": random.randint(20, 31),
        "Defense": random.randint(20, 31),
        "Speed": random.randint(20, 31),
        "Special Attack": random.randint(20, 31),
        "Special Defense": random.randint(20, 31)
    }
    natures = ["Adamant", "Bashful", "Bold", "Brave", "Calm", "Careful", "Docile", "Gentle", "Hardy", "Hasty", "Impish", "Jolly", "Lax", "Lonely", "Mild", "Modest", "Naive", "Naughty", "Quiet", "Quirky", "Rash", "Relaxed", "Sassy", "Serious", "Timid"]
    nature = random.choice(natures)
    pid = random.randint(0, 2**32 - 1)
    shiny_value = ((tid ^ sid) ^ (pid & 0xFFFF) ^ (pid >> 16))
    is_shiny = shiny_value < 8

    return {
        "name": name,
        "stats": stats,
        "nature": nature,
        "is_shiny": is_shiny
    }

def find_shiny_time_offset(device_mac):
    mac_int = int(device_mac.replace(":", ""), 16)
    base_time_passed = 18  # The known time passed
    starter_names = ["Bulbasaurus", "Charedmander", "Squirturtle"]

    for offset in range(10000):  # Increase range to search more offsets
        formatted_time = base_time_passed + offset
        initial_seed = int(formatted_time + mac_int)
        seed = lcg(initial_seed)
        tid, sid = generate_ids(seed)

        for i in range(3):
            poketmon = generate_poketmon(seed + i, tid, sid, starter_names[i])
            if poketmon['is_shiny']:
                print(f"Offset: {offset} seconds")
                print(f"Total time to wait: {base_time_passed + offset} seconds")
                return offset, poketmon['name'], poketmon['stats'], poketmon['nature']

    return None  # If no shiny is found within the range

if __name__ == "__main__":
    device_mac = input("Enter the device MAC address: ")

    result = find_shiny_time_offset(device_mac)
    if result:
        offset, name, stats, nature = result
        print(f"Shiny Poketmon: {name}")
        print(f"Stats: {stats}")
        print(f"Nature: {nature}")
    else:
        print("No shiny found within the given range.")
