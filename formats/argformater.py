maxListLength = 5
maxTupleLength = 5
maxDictLength = 5
maxStringLength = 12
maxRecDepth = 2


def collapse_or_recurse(value, leftD, sep, rightD, maxLength, depth):
    if len(value) > maxLength or depth > maxRecDepth:
        return leftD + "len(" + str(len(value)) + ")" + rightD
    else:
        return leftD + sep.join([value_parse(x, depth + 1)
                                 for x in value]) + rightD


def value_parse(value, depth=0):
    if isinstance(value, int):
        return str(value)
    if isinstance(value, float):
        return str(value)
    if isinstance(value, bool):
        return str(value)
    if value is None:
        return 'None'
    if isinstance(value, str):
        if len(value) > maxStringLength:
            return "'len(" + str(len(value)) + ")'"
        else:
            return value
    if isinstance(value, list):
        return collapse_or_recurse(value, "[", ", ", "]", maxListLength, depth)
    if isinstance(value, tuple):
        return collapse_or_recurse(value, "(", ", ", ")", maxListLength, depth)
    if isinstance(value, dict):
        return collapse_or_recurse(value, "{", ":.., ", "}", maxListLength,
                                   depth)

    return ' '


def formatArgs(arg_name, args):
    res = ''
    for name, value in zip(arg_name, args):
        res += name + '='
        res += value_parse(value, 0)
    return ", ".join([
        name + "=" + value_parse(value) for name, value in zip(arg_name, args)
    ])


#if __name__ == "__main__":
#    print(value_parse(45))
#    print(value_parse("Hello"))
#    print(value_parse("This is my long name"))
#    print(value_parse([2, 3, 4, 'stop']))
#    print(value_parse([2, 3, 4, 'stop this string its too long']))
#    print(value_parse([1, 2, 3, True, 5, 6]))
#    print(value_parse([1, None, [True, 'b', 'c']]))
#    print(
#        value_parse([
#            1, 2, ['a', 'b', 'c'],
#            [(2, 8), [(5, 2, 3), 12, 'this is another big string']]
#        ]))
#
#    f = {'foo': 80, (2, 4, 5): 'Nothing', 'a longer string key': 2, 'a': 12}
#    print(value_parse(f))
#
#    print(value_parse([1, 2, ['a', 'b', 'c', [2, f]]]))