from datetime import datetime

class Note:
    def __init__(self, title : str, body : str, date=datetime.now().isoformat(' ', 'seconds'), dateChanges=datetime.now().isoformat(' ', 'seconds')):
        self.title = title
        self.body = body
        self.date = date
        self.dateChanges = dateChanges

    def createNote():
        title = input('Заголовок: ')
        body = input('Текст: ')
        date = datetime.now().isoformat(' ', 'seconds')
        dateCh = date
        return Note(title, body, date, dateCh)

    def printNote(self):
        print(f'Заголовок: {self.title}')
        print(f'Текст: {self.body}')

    def printFullNote(self):
        Note.printNote(self)
        print(f'Дата создания: {self.date}')
        print(f'Дата изменения: {self.dateChanges}')

    def changeNote(self):
        self.printNote()
        print('Изменение заметки: ')
        print('Заголовок:', self.title)
        newtitle = input('Новый заголовок: ')
        print('Изменение текста: ')
        print('Текст:', self.body)
        newbody = input('Новый текст заметки: ')
        print('Сохранить изменения? (Д - сохранить)')
        answer = input()
        if(answer.lower() == 'д'):
            self.title = newtitle
            self.body = newbody
            self.dateChanges = datetime.now().isoformat(' ', 'seconds')