from dotenv import load_dotenv
import os

load_dotenv()
dir = os.getenv('DISCORD_DIR')

def sendHotkey(author_id, args):
    link = ""
    if len(args) != 1:
        link = "ERROR: You have given an invalid command. You have given either too much or too little information."
    else:
        hotkey = args[0]
        fileName = dir + "hotkey/" + str(author_id) + ".txt"
        line = searchFile((dir+"hotkey/everyone.txt"), hotkey)
        if line[0] == "ERR":
            line = searchFile(fileName, hotkey)
        
        if  line[0] != "ERR":
            link = line[2]
        else:
            link = "ERROR: You do not have this hotkey set up."
    return link

def addHotkey(author_id, args):
    returnVal = ""
    if len(args) < 2:
        returnVal = "ERROR: You have given insuffcient amount of data for this command to work. Consult !help sethotkey for more information."
    else:
        hotkey = args[0]
        fileName = dir + "hotkey/" + str(author_id) + ".txt"
        if not os.path.exists(fileName):
            file = open(fileName, "w")
            file.close()
        
        found = False
        if searchFile(fileName, hotkey) != ["ERR"]:
            found = True

        file = open(fileName, "a")
        if not found: 
            if len(args) == 2:
                writeLine = hotkey + "," + hotkey
            elif len(args) == 3:
                writeLine = hotkey + "," + args[2]

            writeLine +=  "," + args[1] + "\n"
            file.write(writeLine)
            returnVal = "Successfully added!"
        else:
            returnVal = "ERROR: Hotkey name/alias overlaps with an existing hotkey."
        file.close()
            
    return returnVal

def getData(line):
    posFirstComma = line.find(',', 0)
    hotkeyName = line[:posFirstComma]
    hotkeyAlias = line[posFirstComma+1:line.find(',', posFirstComma+1)]
    hotkeyLink = line[line.find(',', posFirstComma+1)+1:]
    
    return [hotkeyName, hotkeyAlias, hotkeyLink]

def searchFile(fileName, hotkey):
    ret = ["ERR"]
    if os.path.exists(fileName):
            with open(fileName) as file:
                for data in enumerate(file):
                    nameAlias = getData(data[1])
                    if hotkey == nameAlias[0] or hotkey == nameAlias[1]:
                        ret = nameAlias
                        break
    return ret

def listHotkey(author_id, args):
    returnText = ""

    if len(args) > 1:
        returnText = "ERROR: Invalid command given."
    
    else:
        commonFile = dir + "hotkey/everyone.txt"
        userFile = dir + "hotkey/" + str(author_id) + ".txt"
        
        if len(args) == 0 or args[0] == "-name" or args[0] == "-n":
            returnText = lhkName(commonFile, userFile)

        elif args[0] == "-all" or args[0] == "-a":
            returnText = lhkAll(commonFile, userFile)
        
        else:
            returnText = "ERROR: Invalid option given. Available options are \"-name (or -n)\" and \"-all (or -a)\""    
    return returnText

def lhkAll(commonFile, userFile):
    returnText = "```\nCommon hotkeys:\n"
    with open(commonFile) as cf:
        for data in enumerate(cf):
            nameAlias = getData(data[1])
            
            returnText += nameAlias[0]
            if nameAlias[0] != nameAlias[1]:
                returnText += " (Alias: " + nameAlias[1] + ")"
            else:
                returnText += " (No alias)"
            returnText += " -> " + nameAlias[2] + "\n"

    returnText += "\nYour hotkeys:\n"
    
    if os.path.exists(userFile):
        with open(userFile) as uf:
            for data in enumerate(uf):
                nameAlias = getData(data[1])
            
                returnText += nameAlias[0]
                if nameAlias[0] != nameAlias[1]:
                    returnText += " (Alias: " + nameAlias[1] + ")"
                else:
                    returnText += " (No alias)"
                returnText += " -> " + nameAlias[2] + "\n"
    else:
        returnText += "You have no hotkeys. Use !addhotkey to make some.\n"
    
    returnText += "```"
    return returnText

def lhkName(commonFile, userFile):
    returnText = "```\nCommon hotkeys:\n"
    with open(commonFile) as cf:
        for data in enumerate(cf):
            line = data[1]
            returnText += line[:(line.find(",")+1)]
    
    returnText = returnText[:-1]
    returnText += "\nYour hotkeys:\n"

    if os.path.exists(userFile):
        with open(userFile) as uf:
            for data in enumerate(uf):
                line = data[1]
                returnText += line[:(line.find(",")+1)]
    else:
        returnText += "None,"
    
    returnText = returnText[:-1]
    returnText += "\n```"
    return returnText

def delHotkey(author_id, args):
    returnVal = ""
    fileName = dir + "hotkey/" + str(author_id) + ".txt"
    if not os.path.exists(fileName):
        returnVal = "ERROR: You do not have any hotkeys to delete!"
    else:
        if len(args) == 1:
            hotkey = args[0]
            with open(fileName, "r+") as fread:
                lines = fread.readlines()
                fread.seek(0)
                for line in lines:
                    lineData = getData(line)
                    if(lineData[0] != hotkey):
                        fread.write(line)
                fread.truncate()
            returnVal = "Successfully deleted."
        else:
            returnVal = "ERROR: Invalid argument given."
    return returnVal

