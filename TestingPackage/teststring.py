def getSubstring(self, start, end):
    sub = ""
    try:
        for a in range(start, end):
            sub = sub + self.str[a]
    except IndexError:
        return ("index out of bounds")
    return  sub


def getCharList(self):