""" Commands are not uniform across different distributions of linux. 
	Periphals details and Software details are pending.

	look for subprocess module and functions available in it.
	"/proc" directory contains files which has some useful information.
"""

import subprocess
import os
import time


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

class CPUDetails :

	def __init__(self):
		self.vendor_id = ""
		self.model_name = ""
		self.cpu_speed = ""
		self.cache_size = ""
		self.processors = ""
		self.cores_per_process = ""

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
				self.cores_per_process += details[tmp]
				tmp = tmp + 1
			file.close()
		except :
			print("ERROR occured while getting CPU details")
		return

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

class NetworkDetails:

	def __init__(self) :
		self.ip_addr = ""
		self.mac_addr = ""

	def getDetails(self):
		filein = subprocess.call("ifconfig eth0 >networkdetails",shell = True , stdout = subprocess.PIPE)
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


OS = OSDetails()
ram = RAMDetails()
cpu = CPUDetails()
net = NetworkDetails()
hdd = DiskDetails()
hdd.getDetails()
print hdd.avail


"""try :
	cd = os.getcwd()
	tmp = cd + "/CINMan"
	print(tmp)
	if not os.path.exists(tmp) :
		subprocess.call("mkdir CINMan",shell = True)
	
	os.chdir(tmp)
	os.getDetails()
	ram.getDetails()
	cpu.getDetails()
	net.getDetails()
	hdd.getDetails()
except :
	print("ERROR")"""
