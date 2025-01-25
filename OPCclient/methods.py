import sys
sys.path.insert(0, "..")
import logging
import time
#from opcua.tools import uaclient

try:
    from IPython import embed
except ImportError:
    import code

    def embed():
        vars = globals()
        vars.update(locals())
        shell = code.InteractiveConsole(vars)
        shell.interact()


from opcua import Client
from opcua.common import methods
#from opcua.common import node
from opcua import ua

class SubHandler(object):

    """
    Subscription Handler. To receive events from server for a subscription
    data_change and event methods are called directly from receiving thread.
    Do not do expensive, slow or network operation there. Create another 
    thread if you need to do such a thing
    """

    def datachange_notification(self, node, val, data):
        print("Python: New data change event", node, val)

    def event_notification(self, event):
        print("Python: New event", event)

if __name__ == "__main__":
    #uaclient()
    logging.basicConfig(level=logging.WARN)
    #logger = logging.getLogger("KeepAlive")
    #logger.setLevel(logging.DEBUG)
    

    client = Client("opc.tcp://192.168.129.20:4840")
    #servers=client.connect_and_find_servers()
    
    
    # client = Client("opc.tcp://admin@localhost:4840/freeopcua/server/") #connect using a user
    #endpoint=client.get_endpoints()
    
    try:
        
        client.connect()
        
        objects = client.get_objects_node()
        #print("Objects node is: ", objects)
        PLC=objects.get_child(["3:PLC_1"])
        #print("chldren are:  ", children)
        # Node objects have methods to read and write node attributes as well as browse or populate address space
        #print("Children of root are: ", root.get_children())
        memoria=PLC.get_child("3:DataBlocksInstance")
        metodi=memoria.get_child("3:methods_DB")        
        metodo=metodi.get_child("3:Method")
        args = metodo.get_child("3:InputArguments")
        argomenti=args.get_value()
        with open('file.txt', 'w') as file:
                    file.write("{}".format(argomenti))
        vartype=metodi.get_child("3:Static")
        paramin=vartype.get_child("3:UAMethod_InParameters")
        mystruct1=paramin.get_child("3:myStruct1")
        structvalue=mystruct1.get_value()
        metodopass=metodo.get_browse_name()
        
        #print("metodopass is ",metodopass)
        #print("metodo is ", metodo)
        dbglobal=PLC.get_child("3:DataBlocksGlobal")
        variables=dbglobal.get_child("3:variables")
        readyagain=variables.get_child("3:loop")
        #print(abil)
        nn=int(sys.argv[1])
        #nn=3000
        lost=0
        for i in range(nn):
            #print('COMINCIO')        
            test=methods.call_method(metodi,metodo,ua.Variant(1,ua.VariantType.Float),ua.Variant(i,ua.VariantType.Float))
            print('call number {}'.format(i+1))
            abil=readyagain.get_value()
            k=0
            while abil==0 and  k<4:
                time.sleep(0.005)
                abil=readyagain.get_value()                
                k=k+1
                if k>3:
                    lost=lost+1
        '''
        variabile = var.get_child("3:value1")
        #struttura = var.get_child("3:y1")
        '''
        #amp=first.get_child("3:[time]")
        #opps=amp.get_value()
        '''
        amplitude = variabile.get_child("3:amplitude")
        tempo_val = variabile.get_child("3:time")
        z_1=1000
       '''
        #value = var.get_data_value() # get value of node as a DataValue object
        #print(value)
        #var.get_value() # get value of node as a python builtin
        #var.set_value(ua.Variant([23], ua.VariantType.Int64)) #set node value using explicit data type
        #var.set_value(3.9) # set node value using implicit data type

        
        # subscribing to a variable node
        
        handler = SubHandler()
        '''
        sub = client.create_subscription(200, handler)
        #handle = sub.subscribe_data_change(amplitude)
        
        time.sleep(0.1)
        '''
        # we can also subscribe to events from server
        #sub.subscribe_events()
        # sub.unsubscribe(handle)
        # sub.delete()

        # calling a method on server
        #res = obj.call_method("2:multiply", 3, "klk")
        #print("method result is: ", res)
        print('lost trigger samples {}'.format(lost))
        time.sleep(0.1)
        #embed()
        
    finally:
        client.disconnect()
