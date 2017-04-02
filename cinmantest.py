""" Commands are not uniform across different distributions of linux. 
	Periphals details and Software details are pending.

	look for subprocess module and functions available in it.
	"/proc" directory contains files which has some useful information.
"""

import subprocess
import os
import time
import simplejson


class OSDetails:
	
	def __init__(self):
		self.kernel_name = ""
		self.node_hostname = ""
		self.kernel_release = ""
		self.machine_hardware = ""
		self.processor = ""
		self.hardware_platform = ""
		self.operating_system = ""

	def getDetails(self):
		try : 
			#Uses command : uname 
			#type : uname --help 
			filein = subprocess.call("uname -s >OSdetails", shell = True , stdout = subprocess.PIPE)
			file = open("OSdetails","r+")
			self.kernel_name = file.read()
 			file.close()
 			filein = subprocess.call("uname -n >OSdetails", shell = True , stdout = subprocess.PIPE)
			file = open("OSdetails","r+")
			self.node_hostname = file.read()
 			file.close()
 			filein = subprocess.call("uname -r >OSdetails", shell = True , stdout = subprocess.PIPE)
			file = open("OSdetails","r+")
			self.kernel_release = file.read()
 			file.close()
 			filein = subprocess.call("uname -m >OSdetails", shell = True , stdout = subprocess.PIPE)
			file = open("OSdetails","r+")
			self.machine_hardware = file.read()
 			file.close()
 			filein = subprocess.call("uname -p >OSdetails", shell = True , stdout = subprocess.PIPE)
			file = open("OSdetails","r+")
			self.processor = file.read()
 			file.close()
 			filein = subprocess.call("uname -i >OSdetails", shell = True , stdout = subprocess.PIPE)
			file = open("OSdetails","r+")
			self.hardware_platform = file.read()
 			file.close()
 			filein = subprocess.call("uname -o >OSdetails", shell = True , stdout = subprocess.PIPE)
			file = open("OSdetails","r+")
			self.operating_system = file.read()
 			file.close()
 			file = open("OSdetails","w")
 			file.write(self.kernel_name)
 			file.write(self.node_hostname)
 			file.write(self.kernel_release)
 			file.write(self.machine_hardware)
 			file.write(self.processor)
 			file.write(self.hardware_platform)
 			file.write(self.operating_system)
 			file.close()
		except :
			print("ERROR occured while gathering OS details")
		return

	def getDictionary(self):
		tmpdict = {"kernel name" : self.kernel_name , "node hostname" : self.node_hostname , "kernel release" : self.kernel_release , "machine hardware" : self.machine_hardware , "processor" : self.processor , "hardware platform" : self.hardware_platform, "operating system" : self.operating_system}
		return tmpdict

class RAMDetails:

	def __init__(self):
		self.mem_total = ""
		self.mem_available  = ""

	def getDetails(self):
		try :
			#cd /proc , you'll find bunch of files which contains some useful details.
			filein = subprocess.call("cat /proc/meminfo >RAMdetails" , shell = True	, stdout = subprocess.PIPE)
			file = open("RAMdetails","r")
			details = file.read()
			#Total RAM
			tmp = details.find("MemTotal")
			tmp = tmp + len("MemTotal") + 1
			while (details[tmp] == " ") :
				tmp = tmp + 1
			while (details[tmp] != '\n') :
				self.mem_total += details[tmp]
				tmp = tmp + 1
			#Available RAM
			tmp = details.find("MemAvailable")
			tmp = tmp + len("MemAvailable") + 1 
			while (details[tmp] == " ") :
				tmp = tmp + 1
			while (details[tmp] != '\n') :
				self.mem_available += details[tmp]
				tmp = tmp + 1
			file.close()
		except :
			print("ERROR occured while gathering RAM details")
		return

	def getDictionary(self):
		tmpdict = {"total memory" :self.mem_total , "available memory" : self.mem_available}
		return tmpdict 		

class CPUDetails :

	def __init__(self):
		self.vendor_id = ""
		self.model_name = ""
		self.cpu_speed = ""
		self.cache_size = ""
		self.processors = ""
		self.cores_per_processor = ""

	def getDetails(self):
		try : 
			filein = subprocess.call("cat /proc/cpuinfo >CPUdetails", shell = True , stdout = subprocess.PIPE)
			file = open("CPUdetails","r")
			details = file.read()
			#vendor_id 
			tmp = details.find("vendor_id\t")
			tmp = tmp + len("vendor_id\t") + 1
			while (details[tmp] == " "):
				tmp = tmp + 1
			while (details[tmp] != '\n'):
				self.vendor_id += details[tmp]
				tmp = tmp + 1
			#model name
			tmp = details.find("model name\t")
			tmp = tmp + len("model name\t") + 1
			while (details[tmp] == " "):
				tmp = tmp + 1
			while (details[tmp] != '\n'):
				self.model_name += details[tmp]
				tmp = tmp + 1
			#CPU speed 
			tmp = details.find("cpu MHz\t")
			tmp = tmp + len("cpu MHz\t") + 2
			while (details[tmp] == " "):
				tmp = tmp + 1
			while (details[tmp] != '\n'):
				self.cpu_speed += details[tmp]
				tmp = tmp + 1
			#cache size
			tmp = details.find("cache size\t")
			tmp = tmp + len("cache size\t") + 1
			while (details[tmp] == " "):
				tmp = tmp + 1
			while (details[tmp] != '\n'):
				self.cache_size += details[tmp]
				tmp = tmp + 1
			#processors
			tmp = details.find("siblings\t")
			tmp = tmp + len("siblings\t") + 1
			while (details[tmp] == " "):
				tmp = tmp + 1
			while (details[tmp] != '\n'):
				self.processors += details[tmp]
				tmp = tmp + 1
			#cpu cores per processors
			tmp = details.find("cpu cores\t")
			tmp = tmp + len("cpu cores\t") + 1
			while (details[tmp] == " "):
				tmp = tmp + 1
			while (details[tmp] != '\n'):
				self.cores_per_processor += details[tmp]
				tmp = tmp + 1
			file.close()
		except :
			print("ERROR occured while getting CPU details")
		return

	def getDictionary(self) :
		tmpdict = {"vendor id" : self.vendor_id , "model name" : self.model_name , "cpu speed" : self.cpu_speed , "cache size" : self.cache_size , "processors" : self.processors , "cores per processor" : self.cores_per_processor}
		return tmpdict

class DiskDetails:

	def __init__(self):
		self.size = ""
		self.used = ""
		self.avail = ""

	def getDetails(self):
		try :
			filein = subprocess.call("df -h --total >diskdetails", shell = True , stdout = subprocess.PIPE)
			file = open("diskdetails","r")
			details = file.read()
			tmp = details.find("total")
			tmp = tmp + len("total") 
			while (details[tmp] == " "):
				tmp = tmp + 1
			while (details[tmp] != " "):
				self.size += details[tmp]
				tmp = tmp + 1
			while (details[tmp] == " "):
				tmp = tmp + 1
			while (details[tmp] != " "):
				self.used += details[tmp]
				tmp = tmp + 1
			while (details[tmp] == " "):
				tmp = tmp + 1
			while (details[tmp] != " "):
				self.avail += details[tmp]
				tmp = tmp + 1
			file.close()
		except :
			print("Error occured while gathering disk details")
		return 

	def getDictionary(self):
		tmpdict = {"size" : self.size , "used" : self.used , "available" : self.avail}
		return tmpdict
class SotwareDetails:
	def __init__(self):
		self.allsoft=[]
	def getDetails(self):
		command="apt list --installed"
		filein = subprocess.call("apt list --installed > Details", shell = True , stdout = subprocess.PIPE)
		#file = open("OSdetails","r+")
		m=[]
		with open("details") as f:
		    for line in f:
			m.append(str(line))
		for x in m:
			self.allsoft.append(x[:x.find("/")])
	
	
class NetworkDetails:

	def __init__(self) :
		self.ip_addr = ""
		self.mac_addr = ""

	def getDetails(self):
		try :
			filein = subprocess.call("/sbin/ifconfig eth0 >networkdetails",shell = True , stdout = subprocess.PIPE)
			file = open("networkdetails","r")
			details = file.read()
			tmp = details.find("inet addr")
			tmp = tmp + len("inet addr") + 1
			while(details[tmp] != " ") :
				self.ip_addr += details[tmp]
				tmp = tmp + 1
			tmp = details.find("HWaddr")
			tmp = tmp + len("HWaddr") + 1
			while(details[tmp] != " ") :
				self.mac_addr += details[tmp]
				tmp = tmp + 1
		except :
			print("Error occured while gathering Network details")
		return 

	def getDictionary(self):
		tmpdict = {"ip addr" : self.ip_addr, "mac addr" : self.mac_addr}
		return tmpdict 


class userDetails:

	def __init__(self):
		self.user_list = []

	def getDetails(self):
		try :
			filein = subprocess.call("who -q >userdetails",shell = True , stdout = subprocess.PIPE)
			file = open("userdetails","r")
			details = file.read()
			parsed_details = details.split(" ")
			for i in range(0,len(parsed_details)-1) :
				self.user_list.append(parsed_details[i])
		except :
			print("Error occured while gathering user details")
		return 

	def getDictionary(self):
		tmpdict = {"user list" : self.user_list}
		return tmpdict

OS = OSDetails()
ram = RAMDetails()
cpu = CPUDetails()
net = NetworkDetails()
hdd = DiskDetails()
user = userDetails()

OS.getDetails()
ram.getDetails()
cpu.getDetails()
net.getDetails()
hdd.getDetails()
user.getDetails()

client_data = []

#collecting data in dictionary form and then appending all of them to create a list of dictionary
client_data.append(OS.getDictionary())
client_data.append(ram.getDictionary())
client_data.append(cpu.getDictionary())
client_data.append(net.getDictionary())
client_data.append(hdd.getDictionary())
client_data.append(user.getDictionary())

#serializing the client data using simple json

client_data = simplejson.dumps(client_data)
