import discord

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

def convertFunction(args):
    impUnits = ["lb", "mi", "gal", "f", "ft"]
    convUnits = [0.4535924, 1.609344, 4.54609, 0, 0.3048]
    metUnits = ["kg", "km", "l", "c", "m"]

    if len(args) == 2:
        try:
            float(args[0])
        except:
            return "ERROR: Invalid inputs given."
        else:
            val = float(args[0])                
            unit = args[1].lower()       
            result = 0
            retUnit = ""

            if unit == "c":
                result = (9*val/5) + 32
                retUnit = "F"
            elif unit == "f":
                result = (5/9) * (val-32)
                retUnit = "C"
            else:
                try:
                    index = impUnits.index(unit)
                except:
                    try:
                        index = metUnits.index(unit)
                    except:
                        return "ERROR: Invalid units given. Valid options are: " + str(impUnits) + ", " + str(metUnits)
                    else:
                        result = val / convUnits[index]
                        retUnit = impUnits[index]
                else:
                    result = val * convUnits[index]
                    retUnit =  metUnits[index]
            return str(val) + " " + unit + " converts to " + str(round(result,4)) + " " + retUnit + "."
    else:
        return "ERROR: Invalid number of arguments given."
