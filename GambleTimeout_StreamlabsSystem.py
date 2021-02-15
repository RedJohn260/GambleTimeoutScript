#---------------------------
#   Import Libraries
#---------------------------
import os
import sys
import json
sys.path.append(os.path.join(os.path.dirname(__file__), "lib")) #point at lib folder for classes / references

import clr
clr.AddReference("IronPython.SQLite.dll")
clr.AddReference("IronPython.Modules.dll")

#   Import your Settings class
from GambleTimeoutSettings_Module import GambleTimeoutMySettings
#from random import *
#---------------------------
#   [Required] Script Information
#---------------------------
ScriptName = "Gamble Timeout"
Website = "https://www.twitch.tv/redjohn260"
Description = "If activated, it will randomly timeout user that use any of the gambling commands defined."
Creator = "RedJohn260"
Version = "1.0.0.0"

#---------------------------
#   Define Global Variables
#---------------------------
global GambleTimeoutSettingsFile
GambleTimeoutSettingsFile = os.path.join(os.path.dirname(__file__), "Settings\gambletimeout_settings.json")
global GambleTimeoutScriptSettings
GambleTimeoutScriptSettings = GambleTimeoutMySettings(GambleTimeoutSettingsFile)

#---------------------------
#   [Required] Initialize Data (Only called on load)
#---------------------------
def Init():

    #   Create Settings Directory
    directory = os.path.join(os.path.dirname(__file__), "Settings")
    if not os.path.exists(directory):
        os.makedirs(directory)
    return

#---------------------------
#   [Required] Execute Data / Process messages
#---------------------------
def Execute(data):

    #command1
    if GambleTimeoutScriptSettings.Command1 in data.Message.lower() and not Parent.IsOnUserCooldown(ScriptName,GambleTimeoutScriptSettings.Command1,data.User) and Parent.HasPermission(data.User,GambleTimeoutScriptSettings.Permission,GambleTimeoutScriptSettings.Info):
        x = Parent.GetRandom(0,100)
        Parent.BroadcastWsEvent("EVENT_MINE","{'show':false}")
        if x <= GambleTimeoutScriptSettings.TimeoutChance:
            SendMessage("/timeout " + data.User + " " + GambleTimeoutScriptSettings.TimeoutSeconds + GambleTimeoutScriptSettings.TimeUnit + " " + GambleTimeoutScriptSettings.Response)
        Parent.AddUserCooldown(ScriptName,GambleTimeoutScriptSettings.Command1,data.User,GambleTimeoutScriptSettings.Cooldown)

    #command2
    if GambleTimeoutScriptSettings.Command2 in data.Message.lower() and not Parent.IsOnUserCooldown(ScriptName,GambleTimeoutScriptSettings.Command2,data.User) and Parent.HasPermission(data.User,GambleTimeoutScriptSettings.Permission,GambleTimeoutScriptSettings.Info):
        x = Parent.GetRandom(0,100)
        Parent.BroadcastWsEvent("EVENT_MINE","{'show':false}")
        if x <= GambleTimeoutScriptSettings.TimeoutChance:
            SendMessage("/timeout " + data.User + " " + GambleTimeoutScriptSettings.TimeoutSeconds + GambleTimeoutScriptSettings.TimeUnit + " " + GambleTimeoutScriptSettings.Response)
        Parent.AddUserCooldown(ScriptName,GambleTimeoutScriptSettings.Command2,data.User,GambleTimeoutScriptSettings.Cooldown)

    #command3
    if GambleTimeoutScriptSettings.Command3 in data.Message.lower() and not Parent.IsOnUserCooldown(ScriptName,GambleTimeoutScriptSettings.Command3,data.User) and Parent.HasPermission(data.User,GambleTimeoutScriptSettings.Permission,GambleTimeoutScriptSettings.Info):
        x = Parent.GetRandom(0,100)
        Parent.BroadcastWsEvent("EVENT_MINE","{'show':false}")
        if x <= GambleTimeoutScriptSettings.TimeoutChance:
            SendMessage("/timeout " + data.User + " " + GambleTimeoutScriptSettings.TimeoutSeconds + GambleTimeoutScriptSettings.TimeUnit + " " + GambleTimeoutScriptSettings.Response)
        Parent.AddUserCooldown(ScriptName,GambleTimeoutScriptSettings.Command3,data.User,GambleTimeoutScriptSettings.Cooldown)

    #command4
    if GambleTimeoutScriptSettings.Command4 in data.Message.lower() and not Parent.IsOnUserCooldown(ScriptName,GambleTimeoutScriptSettings.Command4,data.User) and Parent.HasPermission(data.User,GambleTimeoutScriptSettings.Permission,GambleTimeoutScriptSettings.Info):
        x = Parent.GetRandom(0,100)
        Parent.BroadcastWsEvent("EVENT_MINE","{'show':false}")
        if x <= GambleTimeoutScriptSettings.TimeoutChance:
            SendMessage("/timeout " + data.User + " " + GambleTimeoutScriptSettings.TimeoutSeconds + GambleTimeoutScriptSettings.TimeUnit + " " + GambleTimeoutScriptSettings.Response)
        Parent.AddUserCooldown(ScriptName,GambleTimeoutScriptSettings.Command4,data.User,GambleTimeoutScriptSettings.Cooldown)

    return

#---------------------------
#   [Required] Tick method (Gets called during every iteration even when there is no incoming data)
#---------------------------
def Tick():
    return

def Log(message):
    Parent.Log("Gamble Timeout Script", message)
    return

def SendMessage(message):
    Parent.SendStreamMessage(message)
    return