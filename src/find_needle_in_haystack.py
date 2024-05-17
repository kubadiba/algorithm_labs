def prefix_function(needle):
    if not needle:
        return "no needle"

    needle_length = len(needle)
    prefix = [0] * needle_length
    j = 0
    i = 1
    while i < needle_length:
        if needle[j] == needle[i]:
            prefix[i] = j + 1
            i += 1
            j += 1
        else:
            if j == 0:
                prefix[i] = 0
                i += 1
            else:
                j = prefix[j - 1]
    return prefix


def knuth_morris_pratt(needle, haystack):
    result = []
    haystack_length = len(haystack)
    needle_length = len(needle)
    prefix = prefix_function(needle)
    i = 0
    j = 0
    while i < haystack_length:
        if haystack[i] == needle[j]:
            i += 1
            j += 1
            if j == needle_length:
                result.append(i - needle_length)
                j = prefix[j - 1] if j > 0 else 0
        else:
            if j > 0:
                j = prefix[j - 1]
            else:
                i += 1

    return result

