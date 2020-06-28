padding = 2


def dash_field(text, width):
    #padding = 2
    return text.ljust(len(text) + padding, ' ').ljust(width, '-')


def center_equals_field(text, width=92):
    #padding = 2

    if len(text) + 2 * padding >= width:
        return padding * ' ' + text + padding * ' '

    leftSize = (width // 2) + (len(text) // 2) + 1
    return right_equals_field(left_equals_field(text, leftSize), width)


def left_equals_field(text, width):
    return text.rjust(len(text) + padding, ' ').rjust(width, '=')


def right_equals_field(text, width):
    return text.ljust(len(text) + padding, ' ').ljust(width, '=')


if __name__ == "__main__":
    print('This is the tester for field Space')
    print(center_equals_field("Perfect! This is nice", 91))
