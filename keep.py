import gkeepapi
import keyring



# Valid Note Colors
noteColor = {
    'White' : gkeepapi.node.ColorValue.White,
    'Red' : gkeepapi.node.ColorValue.Red,
    'Orange' : gkeepapi.node.ColorValue.Orange,
    'Yellow' : gkeepapi.node.ColorValue.Yellow,
    'Green' : gkeepapi.node.ColorValue.Green,
    'Teal' : gkeepapi.node.ColorValue.Teal,
    'Blue' : gkeepapi.node.ColorValue.Blue,
    'Purple' : gkeepapi.node.ColorValue.Purple,
    'Pink' : gkeepapi.node.ColorValue.Pink,
    'Brown' : gkeepapi.node.ColorValue.Brown,
    'Gray' : gkeepapi.node.ColorValue.Gray
}


keep = gkeepapi.Keep()
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
        if pin: note.pinned = True
        if color not None:
            try:
                note.color = noteColor[color]
            except:
                print('Invalid Color. \nFollowing is the list of valid colors:\n')
                for color in noteColor:
                    print(color)
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
    if len(labels):
        labels = [keep.findLabel(lablel) for label in labels]
    try:
        matches = keep.find(query=queryStr, labels=[keep.findLabel(labels)])
        if pinned:
            matches = keep.find(query=queryStr, labels=[keep.findLabel(labels)]], pinned=True)
        print('Found', len(matches), 'matching notes:')
        return matches
    except gkeepapi.exception.ParseException as e:
        print(e.raw)
