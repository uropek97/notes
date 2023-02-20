from note import Note

class listNotes:
    def __init__(self, notes=list()):
        self.notes = notes

    def addNote(self, note: Note):
        self.notes.append(note)

    def printNote(self, id: int):
        self.notes[id].printNote()

    def printFullNote(self, id: int):
        self.notes[id].printFullNote()




