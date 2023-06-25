import discord
from dotenv import load_dotenv
import os

load_dotenv()
dir = os.getenv('DISCORD_DIR')
swears = ["cock", "cum", "pussy", "penis", "balls", "cumming", "dong"]

def isProfane(message, mid):
    if (mid != "930181587218358373" and mid != "806970604610912289"):
        for i in swears:
        #this is in NO way an elegant way of going about at it but.
            case1 = i + " "
            case2 = " " + i
            case3 = case2 + " "
            msg = message.content.lower()
        #the 913637349018177587 case is to check for the CUM! emoji in the Lads server        
            ret = (case1 in msg) or (case2 in msg) or (case3 in msg) or (msg == i) or ("ussy" in msg) or ("913637349018177587" in msg)
            if ret == True:
                return ret
                

def appreciation(message):
    msg = message.content.lower()
    ret = False
    if("885327368594530376" in msg):
        ret = ("good" in msg) or ("love" in msg) or ("ily" in msg) or ("ilu" in msg)
    if ret == True:
        return ret

def sad(message):
    msg = message.content.lower()
    ret = False
    if("885327368594530376" in msg):
        ret = ("bad" in msg) or ("fuck" in msg)
    if ret == True:
        return ret

def fruitReturn(fruitName):
    if fruitName == "grape":
        return "  \ \n ()()\n()()()\n ()()\n  ()"
    if fruitName == "apple":
        return " ,(.\n(   )\n `\"\'"
    if fruitName == "banana":
        return " ,\n \`.__.\n  `._,\'"
    if fruitName == "pineapple":
        return " \|/\n AXA\n/XXX\ \n\XXX/\n `^'"
    
def getUptime(diffTime):
    output = ""

    months = int(diffTime/2628000)

    daysDiffTime = diffTime % 2628000
    days = int(daysDiffTime / 86400)

    hoursDiffTime = daysDiffTime % 86400
    hours = int(hoursDiffTime / 3600)

    minDiffTime = hoursDiffTime % 3600
    minutes = int(minDiffTime / 60)
    
    secondDiffTime = int(minDiffTime % 60)

    if(months > 0):
        output += str(months) + "m "
    if(days >= 0):
        if(months > 0 and days == 0):
            output += "0d "
        else:
            output += str(days) + "d "
    if(hours >= 0):
        output += str(hours) + "h "
    if(minutes >= 0):
        output += str(minutes) + "m "
    if(secondDiffTime >= 0):
        output += str(secondDiffTime) + "s "
    return output

def betterLink(message):
    #https://at.tumblr.com/starconfusedtellation/698396984102518784/jrj0630030o5
    firstSlashIndex = message.find("https://at.tumblr.com/") + 22
    index = message.find("/",firstSlashIndex)
    index2 = message.find("/",index+1) + 1
    ret = "https://" + message[firstSlashIndex:index] + ".tumblr.com/" + message[index+1:index2]
    return ret

def sendHotkey(author_id, hotkey):
    link = ""
    
    if len(hotkey) != 1:
        link = "ERROR: You have given an invalid command. You have given either too much or too little information."
    else:
        fileName = dir + "hotkey/" + str(author_id) + ".txt"
        
        line = searchFile((dir+"hotkey/everyone.txt"), hotkey[0])
        if line[0] == "ERR":
            line = searchFile(fileName, hotkey[0])
        
        if  line[0] != "ERR":
            link = line[2]
        else:
            link = "ERROR: You do not have this hotkey set up."
    return link

def addHotkey(author_id, hotkey):
    returnVal = ""
    if len(hotkey) < 2:
        returnVal = "ERROR: You have given insuffcient amount of data for this command to work. Consult !help sethotkey for more information."
    else:
        fileName = dir + "hotkey/" + str(author_id) + ".txt"
        if not os.path.exists(fileName):
            file = open(fileName, "w")
            file.close()
        
        found = False
        if searchFile(fileName, hotkey[0]) != "ERR":
            found = True

        file = open(fileName, "a")
        if not found: 
            if len(hotkey) == 2:
                writeLine = hotkey[0] + "," + hotkey[0]
            elif len(hotkey) == 3:
                writeLine = hotkey[0] + "," + hotkey[2]

            writeLine +=  "," + hotkey[1] + "\n"
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

def delHotkey(author_id, hotkey):
    tempFileName = dir + "hotkey/" + str(author_id)
    fileName = tempFileName + ".txt"
    returnVal = ""
    if not os.path.exists(fileName):
        returnVal = "ERROR: You do not have any hotkeys to delete!"
    else:
        file = open(tempFileName, "w")
        with open(fileName) as cf:
            for data in enumerate(cf):
                line = getData(data[1])
                if line[0] != hotkey:
                    file.write(line[0] + "," + line[1] + "," + line[2])
        file.close()
        os.remove(fileName)
        os.rename(tempFileName,fileName)
        returnVal = "Successfully deleted."
    return returnVal
