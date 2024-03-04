import discord
import datetime as dt
import re
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
    
def getUptime(diffUptime):
    output = ""

    diffTime = diffUptime
    months = int(diffTime/2628000)

    diffTime = diffTime % 2628000
    days = int(diffTime / 86400)

    diffTime = diffTime % 86400
    hours = int(diffTime / 3600)

    diffTime = diffTime % 3600
    minutes = int(diffTime / 60)
    
    diffTime = int(diffTime % 60)

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
    if(diffTime >= 0):
        output += str(diffTime) + "s "
    return output

def betterLink(message):
    #https://at.tumblr.com/starconfusedtellation/698396984102518784/jrj0630030o5
    firstSlashIndex = message.find("https://at.tumblr.com/") + 22
    index = message.find("/",firstSlashIndex)
    index2 = message.find("/",index+1) + 1
    ret = "https://" + message[firstSlashIndex:index] + ".tumblr.com/" + message[index+1:index2]
    return ret

def convertFunction(args):
    impUnits = ["lb", "mi", "gal", "f", "ft", "in", "mpg"]
    convUnits = [0.4535924, 1.609344, 4.54609, 0, 0.3048, 2.54, 0.425143707]
    metUnits = ["kg", "km", "l", "c", "m", "cm", "kml"]

    if len(args) == 2 or len(args) == 3:
        try:
            val = float(args[0])
        except:
            return "ERROR: Invalid inputs given."
        else:
            unit = args[1].lower()       
            result = 0
            retUnit = ""
            if unit in impUnits:
                index = impUnits.index(unit)

                if unit == "f":
                    result = (5/9) * (val-32)
                else:
                    result = val * convUnits[index]
                
                retUnit =  metUnits[index]
            elif unit in metUnits:
                index = metUnits.index(unit)

                if unit == "c":
                    result = (9*val/5) + 32
                else:
                    result = val / convUnits[index]

                retUnit = impUnits[index]
            else:
                return "ERROR: Invalid units given. Valid options are: " + str(impUnits) + ", " + str(metUnits)
            return str(val) + " " + unit + " converts to " + str(round(result,4)) + " " + retUnit + "."
    else:
        return "ERROR: Invalid number of arguments given."

# Got rid of all of this code because turns out you need to have an offset for each timezone you are in, which I will do another day.
"""def getUTCTime(dateTimeTuple):
    if len(dateTimeTuple) == 3 or len(dateTimeTuple) == 4:
        if(len(dateTimeTuple) == 4):
            re.search(r"[A|P][M]", dateTimeTuple[2])
            re.search(r"[0-9]{2,2}", "")
            
            return "ERROR: Invalid time given."
        dates = dateTimeTuple[0].split("-")

        timeStr = dateTimeTuple[1]
        timeSepIndex = timeStr.index(":")
        times = [timeStr[:timeSepIndex], timeStr[(timeSepIndex+1):(timeSepIndex+3)]]

        argsCmd = dates + times

        for i in range(len(argsCmd)):
            try:
                argsCmd[i] = int(argsCmd[i])
            except:
                return "ERROR: Invalid time given."

        if (argsCmd[3] > 12 and len(dateTimeTuple) == 3):
            return "ERROR: Invalid time given."
        
        if (argsCmd[3] < 12 and "PM" in dateTimeTuple[2]):
            argsCmd[3] += 12

        return ("<t:" + str((dt.datetime(argsCmd[2],argsCmd[1],argsCmd[0],argsCmd[3],argsCmd[4]).replace(tzinfo=dt.timezone.utc)).timestamp())[:-2] + ">")
    else:
        return "ERROR: Incorrect number of arguments given. You must give your input as [dd]-[mm]-[yyyy] [hh]:[mm] [AM or PM (optional)] [EST/PST/EDT]"
        """

