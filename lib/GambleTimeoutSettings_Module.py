import os
import codecs
import json

class GambleTimeoutMySettings(object):
	def __init__(self, settingsfile=None):
		try:
			with codecs.open(settingsfile, encoding="utf-8-sig", mode="r") as f:
				self.__dict__ = json.load(f, encoding="utf-8")
		except:
			self.Command1 = "!coin"
			self.Command2 = "!slots"
			self.Command3 = ""
			self.Command3 = ""
			self.Cooldown = 0
			self.Permission = "everyone"
			self.TimeoutChance = 25
			self.TimeoutSeconds = "30"
			self.TimeUnit = "s"
			self.Response = "Get Rekt!!!"

	def Reload(self, jsondata):
		self.__dict__ = json.loads(jsondata, encoding="utf-8")
		return

	def Save(self, settingsfile):
		try:
			with codecs.open(settingsfile, encoding="utf-8-sig", mode="w+") as f:
				json.dump(self.__dict__, f, encoding="utf-8")
			with codecs.open(settingsfile.replace("json", "js"), encoding="utf-8-sig", mode="w+") as f:
				f.write("var settings = {0};".format(json.dumps(self.__dict__, encoding='utf-8')))
		except:
			Parent.Log(ScriptName, "Failed to save settings to file.")
		return