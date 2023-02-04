from datetime import datetime

class Note:
    id = 0

    def __init__(self, title : str, body : str):
        self.title = title
        self.body = body
        self.id = Note.id
        self.data = datetime.now()
        self.dataChanges = self.data
        Note.id += 1