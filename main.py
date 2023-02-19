from note import Note

body = 'body'
title = 'title' 
Note.createNote(title, body)

body2 = 'body2'
title2 = 'title2' 
Note.createNote(title2, body2)

body3 = 'body3'
title3 = 'title3' 
Note.createNote(title3, body3)

Note.printNotes()
Note.changeNote(1)
print('До: ')
Note.printNotes()

Note.removeNote(0)
print('После: ')
Note.printNotes()