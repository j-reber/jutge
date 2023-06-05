import time

from easyinput import read_line


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
    palindrome_suffix = s[-length:] if length > 0 else ''

    return palindrome_suffix


def is_palindrome(s):
    """
    Check if a string is a palindrome.
    """
    return s == s[::-1]


def longest_palindrome_suffix_simp(s):
    """
    Find the longest suffix that is a palindrome using a naive approach.
    """
    longest_suffix = ""
    n = len(s)

    for i in range(n):
        suffix = s[i:]
        if is_palindrome(suffix) and len(suffix) > len(longest_suffix):
            longest_suffix = suffix

    return longest_suffix


def main():
    s = []
    while True:
        strg = input()
        if strg == "":
            break
        s.append(strg)
    for strg in s:
        # start = time.time()
        pal = longest_palindrome_suffix(strg)
        # end_soph = time.time()
        print(len(pal))
        # print(end_soph-start)
        # pal_simp = longest_palindrome_suffix_simp(strg)
        # end_simp = time.time()
        # print(len(pal_simp))
        # print(end_simp-end_soph)



if __name__ == '__main__':
    main()
