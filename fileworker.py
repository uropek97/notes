import json
import os
from datetime import  datetime
from note import Note

dirName = 'Notes'
firstPartName = 'note'
lastPartNape = '.json' 




def write(notes: list):
    if(not os.path.exists(dirName)):
        os.mkdir(dirName)
    i = 1
    for note in notes:
        newFile = dirName + '/' + firstPartName + str(i) + lastPartNape
        i+=1
        with open(newFile, 'w') as f:
            json.dump(note, f, default=to_json)

def read():
    if(os.path.exists(dirName)):
        os.chdir(dirName)    
        for file in os.listdir():
            with open(file, 'r') as f:
                note = json.load(f)
                Note.addNote(Note(note))
    
#создать функцию для десериализации.  json.load(f, object_hook= ???)
#подумать, стоит ли записывать и читать всё из одного файла.
#если что реализовтаь обра варианта. 


def to_json(note):
    if isinstance(note, Note):
        return {'__class__': 'Note',
                '__title__': note.title,
                '__body__': note.body,
                '__data__': date_to_json(note.data),
                '__dateChanges__': date_to_json(note.dataChanges)}
    raise TypeError(repr(note) + ' is not JSON serializable')

def date_to_json(date):
    if isinstance(date, datetime):
        return date.isoformat()
    raise TypeError(repr(date) + ' is not JSON serializable')

