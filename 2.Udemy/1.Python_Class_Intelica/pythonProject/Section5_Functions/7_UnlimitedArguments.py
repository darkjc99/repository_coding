def standard_arg(arg):
    print(arg)


def pos_only_arg(arg, arg2, /):  # Have to be passed by their respective position
    print(arg, arg2)


def kwd_only_arg(*, arg, arg2):  # Refer them by the kwargs
    print(arg, arg2)


def combined_example(pos_only, pos_only2, /, standard, standard2, *, kwd_only):
    print(pos_only, standard, kwd_only)


if __name__ == "__main__":
    # pos_only_arg(1, 2)
    # kwd_only_arg(arg=1, arg2=2)
    combined_example(1, 2, 3, standard2=4, kwd_only=5)
