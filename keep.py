import gkeepapi
import keyring


# Valid Note Colors
noteColors = {
    'white' : gkeepapi.node.ColorValue.White,
    'red' : gkeepapi.node.ColorValue.Red,
    'orange' : gkeepapi.node.ColorValue.Orange,
    'yellow' : gkeepapi.node.ColorValue.Yellow,
    'green' : gkeepapi.node.ColorValue.Green,
    'teal' : gkeepapi.node.ColorValue.Teal,
    'blue' : gkeepapi.node.ColorValue.Blue,
    'purple' : gkeepapi.node.ColorValue.Purple,
    'pink' : gkeepapi.node.ColorValue.Pink,
    'brown' : gkeepapi.node.ColorValue.Brown,
    'gray' : gkeepapi.node.ColorValue.Gray
}

keep = gkeepapi.Keep()
username, master_token = '', ''
token = keyring.get_password('google-keep-token', username)
keep.resume(username, master_token)

# Error reporting
# try:
#     # Code that raises the exception
# except gkeepapi.exception.ParseException as e:
#     print(e.raw)



def postNote(title, text, labels=[], pin=False, color=None):
    try:    
        note = keep.createNote(title, text)
        if len(labels) != 0:
            for label in labels:
                note.labels.add(label)
        if pin == True:
            note.pinned = True
            
        # if color not None:
        #     try:
        #         note.color = noteColors[color]
        #     except KeyError:
        # ## note: exception caught during cli arg parse ## 
        #         print('Invalid Color. \nFollowing is the list of valid colors:\n')
        #         for color in noteColors:
        #             print(color)
        
        keep.sync()
    except gkeepapi.exception.ParseException as e:
        print(e.raw)

def listLabels():
    try:
        print('labels:')
        for label in keep.labels():
            print(label)
    except gkeepapi.exception.ParseException as e:
        print(e.raw)

def findNote(queryStr='', labels=[], pinned=False):
    try:
        if len(labels):
            labels = [keep.findLabel(label) for label in labels]
            matches = keep.find(query=queryStr, labels=[keep.findLabel(labels)])
        if pinned == True:
            matches = keep.find(query=queryStr, labels=[keep.findLabel(labels)], pinned=True)
        print('Found', len(matches), 'matching notes:')
        return matches
    except gkeepapi.exception.ParseException as e:
        print(e.raw)
