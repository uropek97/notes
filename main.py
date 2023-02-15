from note import Note

body = 'body'
title = 'title' 

Note.createNote(title, body)

body2 = 'body2'
title2 = 'title2' 

Note.createNote(title2, body2)
Note.printNotes()
Note.changeNote(1)
Note.printNotes()


