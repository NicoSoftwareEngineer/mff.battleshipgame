def clear():
    """Clear the terminal screen by emitting ANSI control sequences.

    This function attempts several common clear sequences so it works on
    a variety of terminals. It does not return a value.
    """
    print("\033[H\033[2J", end="")
    print("\033[H\033[3J", end="")
    print("\033c", end="")