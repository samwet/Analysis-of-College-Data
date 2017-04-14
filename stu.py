VALID_GENRES = ("Sincere", "Very Sincere", "?")

class stu:
    def __init__(self, roll_no, internal, external, genre):
        self.roll_no = roll_no
        self.internal = internal
        self.external = external
        if genre not in VALID_GENRES:
            raise ValueError("Invalid genre! ('" + genre + "')")
        else:
            self.genre = genre

    def __repr__(self):
        return "[Student] : roll no='{}'; internal marks={}; external marks={}, class='{}'".format(self.roll_no, self.internal, self.external, self.genre)
