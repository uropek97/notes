from note import Note

class listNotes:
    def __init__(self, notes=list()):
        self.notes = notes

    def addNote(self, note: Note):
        self.notes.append(note)

    def printNote(self, id: int):
        self.notes[id].printNote()

    def printFullNote(self, id: int):
        print(id + 1)
        self.notes[id].printFullNote()

    def printNotes(self):
        for id in range(len(self.notes)):
            self.printNote(id)

    def printFullNotes(self):
        for id in range(len(self.notes)):
            self.printFullNote(id)

    def changeNoteByID(self, id : int):
        note = self.notes[id - 1]
        note.changeNote()

    def changeNoteByTitle(self, title: str):
        for note in self.notes:
            if note.title == title:
                note.changeNote()
                return
        print('Нет такой заметки')

    def removeNoteByID(self, id: int):
        corId = id - 1
        if(corId <= len(self.notes)):
            self.notes.pop(corId)

    def removeNoteByTitle(self, title: str):
        for note in self.notes:
            if note.title == title:
                self.notes.remove(note)
                return
        print('Нет такой заметки')
    
