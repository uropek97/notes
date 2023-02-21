import filehelper
from listNotes import listNotes

def writeNote(listNotes : listNotes, id: int, filename: str):
    filehelper.write(listNotes.notes[id], filename)

def writeNotes(listNotes : listNotes):
    firstPart = 'Notes/note'
    endPart = '.json'
    for index in range(len(listNotes.notes)):
        writeNote(index, f'{firstPart}{index+1}{endPart}')

def readNotes(listNotes : listNotes = listNotes()):
    dirName = 'Notes/'
    for file in filehelper.getNotes(dirName):
        listNotes.addNote(filehelper.read(f'{dirName}{file}'))
    return listNotes