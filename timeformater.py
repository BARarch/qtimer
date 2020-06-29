millisecondLimit = 2
secondLimit = 60
minuteSecondLimit = 3600


def format_time(tc):
    if tc < millisecondLimit:
        return "{} ms".format(int((tc) * 1000))
    if tc < secondLimit:
        return "{:.3f} s".format(tc)
    tc = int(tc)
    if tc < minuteSecondLimit:
        return "{}m {}s".format(tc // 60, tc % 60)

    return "{}:{}:{}".format(tc // 3600, (tc % 3600) // 60, tc % 60)


if __name__ == "__main__":
    import time
    s = input("Press Enter to Start Clock")
    ts = time.time()
    e = input("Press Enter to Stop Clock")
    te = time.time()

    print(format_time(te - ts))