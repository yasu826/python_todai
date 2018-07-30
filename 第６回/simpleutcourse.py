class SimpleCourse:
    def __init__(self):
        self.students = []
    def add_member(self, id):
        self.students.append(id)
        
class SimpleUTCourse(SimpleCourse):
    def __init__(self, title_j, name_j, year, terms, slot):
        super().__init__()
        self.title_j = title_j
        self.year = year
        self.terms = terms
        self.slot = slot
