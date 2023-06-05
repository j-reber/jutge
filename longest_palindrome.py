from easyinput import read_line


def is_palindrome(s):
    return s == s[::-1]


def main():
    x = read_line()
    length = 0
    for i in range(len(x)+1):
        # print(i)
        # print(x[-i:])
        if is_palindrome(x[-i:]):
            length = i
    print(length)


if __name__ == '__main__':
    main()
