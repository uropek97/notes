import json
import os
from datetime import  datetime
from note import Note
from collections import namedtuple

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
    title = obj["title"]
    body = obj["body"]
    date = obj["date"]
    dateChanges = obj["dateChanges"]
    return Note(title, body, date, dateChanges)
