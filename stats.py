def number_of_words(words):
    count = len(words.split())
    print(f"Found {count} total words")
    return count


def char_count(characters):
    counts = {}

    for char in characters:
        lower_char = char.lower()
        if lower_char not in counts:
            counts[lower_char] = 0
        counts[lower_char] += 1
    return counts


def dict_sorted(dict_data):
    data = []
    for i in dict_data.items():
        new = {"char": i[0], "num": i[1]}
        data.append(new)

    sorted_data = sorted(data, key=lambda x: x["num"], reverse=True)
    return sorted_data
