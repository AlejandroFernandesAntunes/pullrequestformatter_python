import os

#VARS
trelloCardNumber = ''
title = ''
description = ''
reviewers = []
notes = []
tasks = []
trelloLink = ''
risk = ''
risks = ['Low', 'Medium', 'High']

# This is the instructions dictionary.
# instruction_key: [alias1, alias2]
# you can add all the alias you like on the arrays for specific tasks.
_instrustionsWhitelist = {  'see how it is going': ['sr', 'see results'],
                            'add trello card number': ['trello card number', 'tcn'],
                            'add trello link': ['add trello link', 'atl'],
                            'write description':['write description', 'wd'],
                            'write a task':['write a task', 'wat'],
                            'delete a task': ['delete a task', 'dat'],
                            'write title': ['write title', 'title', 't'],
                            'add reviewer': ['add reviewer', 'ar'],
                            'delete reviewer': ['delete reviewer', 'dr'],
                            'add note': ['add note', 'an'],
                            'delete note': ['delete note', 'dn'],
                            'add risk': ['add risk', 'set risk', 'risk'],
                            'delete risk': ['delete risk', 'reset risk', 'rr'],
                            'help': ['help', 'h', '?'] }


#FUNCTIIONS
def addReviewer( reviewer ):
    reviewers.append(reviewer)
    clearScreen()

def deleteReviewer ( reviewerNumber ):
    reviewers.pop(reviewerNumber - 1)
    clearScreen()
    return True

def addNote( note ):
    notes.append(note)
    clearScreen()

def deleteNote ( noteNumber ):
    notes.pop(noteNumber - 1)
    clearScreen()
    return True

def writeTask( taskBody ):
    tasks.append('- [x] '+ taskBody)
    clearScreen()

def deleteTask ( taskNumber ):
    tasks.pop(taskNumber - 1)
    clearScreen()
    return True

def clearScreen():
    os.system('clear')

def printHelp():
    clearScreen()
    print('This work with instructions, they are aliases for them you can use the full name of the instruction as well.')
    print('Feel free to open the code and add aliases on your own, this are the standard ones.')
    print('--------------------------------------------------------')
    print('sr - see results this will show you how PR content.')
    print('tcn - specify trello card number. Calling it again will reset the value to the new one.')
    print('atl - add trello link. Calling it again will reset the value to the new one.')
    print('wd - write description. Calling it again will reset the value to the new one.')
    print('t - write PR title.')
    print('wat - write a task.')
    print('dat - delete a task.')
    print('ar - add reviewer.')
    print('dr - remove reviewer.')
    print('an - add note.')
    print('dn - delete note.')
    print('an - add note.')
    print('risk - add risk.')
    print('rr - reset risk.')
    print('exit - imagine what this will do...')
    print('--------------------------------------------------------')


def printResult():
    print('##' + title)
    print('#### Trello board reference:')
    print("* [Trello Card #"+str(trelloCardNumber)+"]("+str(trelloLink)+")")
    print(' --- ')
    print ('#### Description:')
    print ('*' + description)
    print(' --- ')
    print ('#### Reviewers:')
    for reviewer in reviewers: print '*' + reviewer
    print(' --- ')
    print ('#### Notes:')
    for note in notes: print '*' + note
    print(' --- ')
    print ('#### Tasks:')
    for task in tasks: print task
    print(' --- ')
    print ('#### Risk:')
    print (risk)
    print(' --- ')
    print ('#### Preview:')
    print ('* N/A')

while True:
    print('# hi, if you feel lost here type help or ?.')
    print('# type exit to end.')
    _userInput = raw_input('instruction? ')
    if _userInput == 'exit':
        printResult()
        break
    else:
        for key, currentValue in _instrustionsWhitelist.items():
            if _userInput in currentValue:

                if key == 'help':
                    clear = False
                    while not clear:
                        printHelp()
                        clearInput = raw_input('shall we continue? (y/n): ')
                        if clearInput == 'y':
                            clear = True
                    if clear: clearScreen()

                if key == 'see how it is going':
                    clear = False
                    while not clear:
                        printResult()
                        clearInput = raw_input('shall we continue? (y/n): ')
                        if clearInput == 'y':
                            clear = True
                    if clear: clearScreen()

                if key == 'write description':
                    _userInput = raw_input('please, describe the PR: ')
                    description = str(_userInput)
                if key == 'write a task':
                    _userInput = raw_input('please, describe the task: ')
                    writeTask(_userInput)

                if key == 'delete a task':
                    print tasks
                    correctOption = False
                    while not correctOption:
                        try:
                            _userInput = raw_input('which one you want to delete (number of task)?: ')
                            correctOption = deleteTask(int(_userInput))
                        except ValueError:
                            print 'please provide the number of the task, they are right there'
                        except IndexError:
                            print 'there are only ' + str(len(tasks)) + ' and you want to remove number ' + str(_userInput) + '! be serious...'

                if key == 'add trello card number':
                    _userInput = raw_input('which is the card number? ')
                    trelloCardNumber = str(_userInput)
                    clearScreen()

                if key == 'add trello link':
                    _userInput = raw_input('trello link (can use clipboard here)? ')
                    trelloLink = str(_userInput)
                    clearScreen()

                if key == 'write title':
                    _userInput = raw_input('title for the PR: ')
                    title = _userInput
                    clearScreen()

                if key == 'add reviewer':
                    _userInput = raw_input('please, write slack alias for reviewer: ')
                    addReviewer(_userInput)

                if key == 'delete reviewer':
                    print reviewers
                    correctOption = False
                    while not correctOption:
                        try:
                            _userInput = raw_input('which one you want to delete (number of reviewer)?: ')
                            correctOption = deleteReviewer(int(_userInput))
                        except ValueError:
                            print 'please provide the number of the reviewer, they are right there'
                        except IndexError:
                            print 'there are only ' + str(len(tasks)) + ' and you want to remove number ' + str(_userInput) + '! be serious...'

                if key == 'add note':
                    _userInput = raw_input('please, write the note: ')
                    addNote(_userInput)

                if key == 'delete note':
                    print notes
                    correctOption = False
                    while not correctOption:
                        try:
                            _userInput = raw_input('which one you want to delete (number of note)?: ')
                            correctOption = deleteNote(int(_userInput))
                        except ValueError:
                            print 'please provide the number of the note, they are right there'
                        except IndexError:
                            print 'there are only ' + str(len(tasks)) + ' and you want to remove number ' + str(_userInput) + '! be serious...'

                if key == 'add risk':
                    print(risks)
                    correctOption = False
                    while not correctOption:
                        try:
                            _userInput = raw_input('please, specify risk (1 2 or 3)?: ')
                            risk = risks[int(_userInput)]
                            correctOption = True
                        except ValueError:
                            print 'please provide the number of the note, they are right there'
                        except IndexError:
                            print 'there are only ' + str(len(risks)) + ' and you want to remove number ' + str(_userInput) + '! be serious...'

                if key == 'delete risk':
                    resetRisk()
