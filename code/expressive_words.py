# 809. Expressive Words


def expressive_words(s, words):
    s_keys, s_values = get_maps(s)
    counts = 0
    for j in words:
        j_keys, j_values = get_maps(j)
        print(s_keys, j_keys)
        if s_keys == j_keys:
            target = 0
            for k in range(len(j_keys)):
                if s_values[k] == j_values[k]:
                    target += 1
                if s_values[k] > j_values[k] and s_values[k] >= 3:
                    target += 1
            if target == len(j_keys):
                counts += 1
    return counts



def get_maps(strings):
    if len(strings):
        keys, values = [strings[0]], [1]
        for i in range(1, len(strings)):
            if strings[i] == keys[-1]:
                values[-1] += 1
            else:
                keys.append(strings[i])
                values.append(1)
        return keys, values
    return [], []
