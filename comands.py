from listNotes import listNotes
import fileListNotes

listN = fileListNotes.readNotes()

listOneWordComands = ['help', 'exit', 'create', 'print']
listTwoWordComands = ['delete', 'del', 'remove', 'rm', 'change', 'chg', 'print']
comlist = ['create', 'change', 'delete', 'print', 'help', 'exit']

def run():
    comand = ''
    print('Приветсвую!')
    print('Это прилоежиние \"Заметки\" студента GB Игоря Чеботы')
    print('Существующие команды: ')
    for c in comlist:
        print(c, end='\t')
    while(comand != 'exit'):
        comand = input('Команда: ').lstrip().rstrip()
        try:
            choiceComm(comand)
        except Exception as e:
            print(e)
        fileListNotes.writeNotes(listN)

def choiceComm(comand):
    temp = parseStr(comand)
    if isinstance(temp, str):
        if temp in listOneWordComands:
            dictOneWordCommands[temp](listN)
    elif isinstance(temp, list):
        if temp[0] in listTwoWordComands:
            dictTwoWordCommands[temp[0]](temp[1])
    else:
        print('Неизвестаня команда')
        return

def parseStr(string: str):
    temp = string.split(' ')
    if len(temp) == 2:
        return temp
    elif len(temp) == 1:
        return string
    else:
        print('Неверное количество аргументов')
        return None

def howRM(data:str):
    if data.isdigit():
        listN.removeNoteByID(int(data))
    else:
        listN.removeNoteByTitle(data)

def howChg(data:str):
    if data.isdigit():
        listN.changeNoteByID(int(data))
    else:
        listN.changeNoteByTitle(data)

def howPrt(data:str):
    if data.isdigit():
        listN.printNote(int(data))
    else:
        if data.lower() == 'all':
            listN.printNotes()
        elif data.lower() == 'full':
            listN.printFullNotes()
        else:
            pass

dictOneWordCommands = {
    listOneWordComands[0]: print('help'),
    listOneWordComands[1]: print('exit'),
    listOneWordComands[2]: listNotes.createNote,
    listOneWordComands[3]: listNotes.printNotes
}

dictTwoWordCommands = {
    listTwoWordComands[0]: howRM,
    listTwoWordComands[1]: howRM,
    listTwoWordComands[2]: howRM,
    listTwoWordComands[3]: howRM,
    listTwoWordComands[4]: howChg,
    listTwoWordComands[5]: howChg,
    listTwoWordComands[6]: howPrt,
}