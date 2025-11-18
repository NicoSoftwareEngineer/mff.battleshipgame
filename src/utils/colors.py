class ANSI():
    """Helpers for composing simple ANSI escape sequences for styling text.

    Methods are lightweight and return strings that wrap the provided
    content or codes. They are used by the board printing logic to color
    output.
    """
    def background(code):
        """Return an ANSI sequence for a background color code."""
        return "\33[{code}m".format(code=code)

    def style_text(code):
        """Return an ANSI sequence for a text style code."""
        return "\33[{code}m".format(code=code)

    def color_text(text, code):
        """Wrap `text` with an ANSI color code and reset to default.

        Args:
            text: the text to color.
            code: numeric ANSI color code.

        Returns:
            Colored string suitable for printing to an ANSI-capable terminal.
        """
        output = "\33[{code}m".format(code=code)
        output += str(text)
        output += "\33[{code}m".format(code=37)
        return output
    
