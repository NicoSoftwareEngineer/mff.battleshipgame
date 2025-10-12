class ANSI():
    def background(code):
        return "\33[{code}m".format(code=code)

    def style_text(code):
        return "\33[{code}m".format(code=code)

    def color_text(text, code):
        output = "\33[{code}m".format(code=code)
        output += str(text)
        output += "\33[{code}m".format(code=37)
        return output
    
    