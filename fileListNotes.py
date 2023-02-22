import filehelper
from listNotes import listNotes

dirName = 'Notes'
firstPart = 'note'
endPart = '.json'

def writeNote(listNotes : listNotes, id: int, filename: str):
    filehelper.write(listNotes.notes[id], filename)

def writeNotes(listNotes : listNotes):
    filehelper.createDir(dirName)
    filehelper.clearDir(dirName)
    for index in range(len(listNotes.notes)):
        writeNote(listNotes, index, f'{dirName}/{firstPart}{index+1}{endPart}')

def readNotes(listNotes : listNotes = listNotes()):
    for file in filehelper.getNotes(dirName):
        listNotes.addNote(filehelper.read(f'{dirName}/{file}'))
    return listNotes