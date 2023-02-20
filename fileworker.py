import json
import os
from note import Note

dirName = 'Notes'

def write(notes: list):
    if(not os.path.exists(dirName)):
        os.mkdir(dirName)
    i = 1
    firstPartName = 'note'
    lastPartNape = '.json' 
    for note in notes:
        newFile = dirName + '/' + firstPartName + str(i) + lastPartNape
        i+=1
        with open(newFile, 'w') as f:
            json.dump(note, f, default=to_json, indent=2)

def read():
    if(os.path.exists(dirName)):
        os.chdir(dirName)    
        for file in os.listdir():
            with open(file, 'r') as f:
                a = json.load(f, object_hook=from_json)
                Note.addNote(a)

def to_json(obj):
    if isinstance(obj, Note):
        return obj.__dict__
    
def from_json(obj):
    return Note(obj["title"], obj["body"], obj["date"], obj["dateChanges"])
