import timeit

def load_file(filepath, encoding='utf-8'):
    try:
        with open(filepath, 'r', encoding=encoding) as file:
            return file.read()
    except UnicodeDecodeError:
        with open(filepath, 'r', encoding='latin-1') as file:
            return file.read()

article1 = load_file('text-1.txt')
article2 = load_file('text-2.txt')

def compute_lps(pattern):
    lps = [0] * len(pattern)
    length = 0
    i = 1
    while i < len(pattern):
        if pattern[i] == pattern[length]:
            length += 1
            lps[i] = length
            i += 1
        else:
            if length != 0:
                length = lps[length - 1]
            else:
                lps[i] = 0
                i += 1
    return lps

def kmp_search(main_string, pattern):
    M = len(pattern)
    N = len(main_string)
    lps = compute_lps(pattern)
    i = j = 0
    while i < N:
        if pattern[j] == main_string[i]:
            i += 1
            j += 1
        elif j != 0:
            j = lps[j - 1]
        else:
            i += 1
        if j == M:
            return i - j
    return -1

def build_shift_table(pattern):
    table = {}
    length = len(pattern)
    for index, char in enumerate(pattern[:-1]):
        table[char] = length - index - 1
    table.setdefault(pattern[-1], length)
    return table

def boyer_moore_search(text, pattern):
    shift_table = build_shift_table(pattern)
    i = 0
    while i <= len(text) - len(pattern):
        j = len(pattern) - 1
        while j >= 0 and text[i + j] == pattern[j]:
            j -= 1
        if j < 0:
            return i
        i += shift_table.get(text[i + len(pattern) - 1], len(pattern))
    return -1

def polynomial_hash(s, base=256, modulus=101):
    n = len(s)
    hash_value = 0
    for i, char in enumerate(s):
        power_of_base = pow(base, n - i - 1) % modulus
        hash_value = (hash_value + ord(char) * power_of_base) % modulus
    return hash_value

def rabin_karp_search(main_string, substring):
    substring_length = len(substring)
    main_string_length = len(main_string)
    base = 256
    modulus = 101
    substring_hash = polynomial_hash(substring, base, modulus)
    current_slice_hash = polynomial_hash(main_string[:substring_length], base, modulus)
    h_multiplier = pow(base, substring_length - 1) % modulus
    for i in range(main_string_length - substring_length + 1):
        if substring_hash == current_slice_hash:
            if main_string[i:i + substring_length] == substring:
                return i
        if i < main_string_length - substring_length:
            current_slice_hash = (current_slice_hash - ord(main_string[i]) * h_multiplier) % modulus
            current_slice_hash = (current_slice_hash * base + ord(main_string[i + substring_length])) % modulus
            if current_slice_hash < 0:
                current_slice_hash += modulus
    return -1

# Define the substrings to search for
existing_substring = "пошук"
non_existing_substring = "nonexistent"

# Measure time for article1 with existing substring
bm_time_article1_exist = timeit.timeit(lambda: boyer_moore_search(article1, existing_substring), number=10)
kmp_time_article1_exist = timeit.timeit(lambda: kmp_search(article1, existing_substring), number=10)
rk_time_article1_exist = timeit.timeit(lambda: rabin_karp_search(article1, existing_substring), number=10)

# Measure time for article1 with non-existing substring
bm_time_article1_nonexist = timeit.timeit(lambda: boyer_moore_search(article1, non_existing_substring), number=10)
kmp_time_article1_nonexist = timeit.timeit(lambda: kmp_search(article1, non_existing_substring), number=10)
rk_time_article1_nonexist = timeit.timeit(lambda: rabin_karp_search(article1, non_existing_substring), number=10)

# Measure time for article2 with existing substring
bm_time_article2_exist = timeit.timeit(lambda: boyer_moore_search(article2, existing_substring), number=10)
kmp_time_article2_exist = timeit.timeit(lambda: kmp_search(article2, existing_substring), number=10)
rk_time_article2_exist = timeit.timeit(lambda: rabin_karp_search(article2, existing_substring), number=10)

# Measure time for article2 with non-existing substring
bm_time_article2_nonexist = timeit.timeit(lambda: boyer_moore_search(article2, non_existing_substring), number=10)
kmp_time_article2_nonexist = timeit.timeit(lambda: kmp_search(article2, non_existing_substring), number=10)
rk_time_article2_nonexist = timeit.timeit(lambda: rabin_karp_search(article2, non_existing_substring), number=10)

# Print results
print(f"Article 1 - Existing Substring: BM: {bm_time_article1_exist:.6f}, KMP: {kmp_time_article1_exist:.6f}, RK: {rk_time_article1_exist:.6f}")
print(f"Article 1 - Non-Existing Substring: BM: {bm_time_article1_nonexist:.6f}, KMP: {kmp_time_article1_nonexist:.6f}, RK: {rk_time_article1_nonexist:.6f}")
print(f"Article 2 - Existing Substring: BM: {bm_time_article2_exist:.6f}, KMP: {kmp_time_article2_exist:.6f}, RK: {rk_time_article2_exist:.6f}")
print(f"Article 2 - Non-Existing Substring: BM: {bm_time_article2_nonexist:.6f}, KMP: {kmp_time_article2_nonexist:.6f}, RK: {rk_time_article2_nonexist:.6f}")