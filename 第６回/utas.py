
class UTCourse:
    def __init__(self, a):
        for k,v in a.items():
            if k == "year":
                setattr(self, k, int(v))
            else:
                setattr(self, k, v)
