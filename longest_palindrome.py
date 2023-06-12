import time
from yogi import tokens


def kmp(strg):
    p = [0 for _ in strg]
    j = -1
    for i in range(len(strg)):
        while j >= 0 and strg[j] != strg[i]:
            if j:
                j = p[j - 1]
            else:
                j = -1
        j += 1
        p[i] = j
    return p


def longest_palindrome_suffix(s):
    # Reverse the input string
    reversed_s = s[::-1]

    # Concatenate the reversed string and a special character '$'
    modified_s = reversed_s + '$' + s

    # Compute the longest proper suffix array
    lps = kmp(modified_s)

    # Find the length of the longest palindrome suffix
    length = lps[-1]

    # Extract the longest palindrome suffix from the original string
    # palindrome_suffix = s[-length:] if length > 0 else ''

    # return palindrome_suffix
    return length

# def is_palindrome(s):
#     """
#     Check if a string is a palindrome.
#     """
#     return s == s[::-1]


# def longest_palindrome_suffix_simp(s):
#     """
#     Find the longest suffix that is a palindrome using a naive approach.
#     """
#     longest_suffix = ""
#     n = len(s)
#
#     for i in range(n):
#         suffix = s[i:]
#         if is_palindrome(suffix) and len(suffix) > len(longest_suffix):
#             longest_suffix = suffix
#
#     return longest_suffix


def main():
    s = []
    # s.append('i')
    # s.append('anna')
    # s.append('abcbapep')
    # s.append('zzzzzzzz')
    # s.append('buenopuesmoltbepuesadios')
    # s.append('abba')
    # s.append('abc' * 2)
    for i, x in enumerate(tokens(str)):
        s.append(x)
    for i in range(len(s)):
        rots = longest_palindrome_suffix(s[i])
        # rots_simp = longest_palindrome_suffix_simp(s[i])
        # print(len(rots_simp))
        print(rots)


if __name__ == '__main__':
    main()
