import json
import os
from note import Note

def write(note: Note, filename: str):
    with open(filename, 'w') as f:
        json.dump(note, f, default=to_json, indent=2)

def read(filename: str):
    with open(filename, 'r') as f:
        return json.load(f, object_hook=from_json)

def to_json(obj):
    if isinstance(obj, Note):
        return obj.__dict__
    
def from_json(obj):
    return Note(obj["title"], obj["body"], obj["date"], obj["dateChanges"])

def getNotes(dirName : str = 'Notes/'):
    return os.listdir(dirName)