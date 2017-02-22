import oca
import config
from oca.exceptions import OpenNebulaException

# Create the client instance using the parameters defined in the config
client = oca.Client(config.userName + ':' + config.password, config.protocol + '://' + config.ipAddress + ':' + config.port + config.endPoint)

try : 
	# Lets create a test VM with 128MB of ram and 1 CPU
	vm_id=oca.VirtualMachine.allocate(client, '<VM><MEMORY>128</MEMORY><CPU>1</CPU></VM>')
	print("Created with id = %d" % vm_id)
	
	# Lets print the VMs available in the pool
	print("Printing the available VMs in the pool.")
	vm_pool = oca.VirtualMachinePool(client)
	for vm in vm_pool:
		print("%s (memory: %s MB)" % ( vm.name, vm.template.memory))
	
except OpenNebulaException:
	print("OpenNebulaException occurred.")
