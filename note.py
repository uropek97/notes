from datetime import datetime

class Note:
    listNotes = list()

    def __init__(self, title : str, body : str):
        self.title = title
        self.body = body
        self.data = datetime.now()
        self.dataChanges = self.data

    def createNote(title : str, body : str):
        Note.listNotes.append(Note(title, body))

    def printNote(self):
        print(f'ID: {Note.listNotes.index(self)}')
        print(f'Дата создания: {self.data}')
        print(f'Дата изменения: {self.dataChanges}')
        print(f'Заголовок: {self.title}')
        print(f'Текст: {self.body}')

    def printNotes():
        for note in Note.listNotes:
            Note.printNote(note)

    def changeNote(id : int):
        note = Note.listNotes[id]
        note.printNote()
        print('Изменение заметки: ')
        print('Заголовок:', note.title)
        newtitle = input('Новый заголовок: ')
        print('Изменение текста: ')
        print('Текст:', note.body)
        newbody = input('Новый текст заметки: ')
        print('Сохранить изменения? (Д - сохранить)')
        answer = input()
        if(answer.lower() == 'д'):
            note.title = newtitle
            note.body = newbody
            note.dataChanges = datetime.now()

    def removeNote(id : int):
        if(len(Note.listNotes) >= id):
            Note.listNotes.remove(Note.listNotes[id])
        else:
            print('Нет такой заметки.')