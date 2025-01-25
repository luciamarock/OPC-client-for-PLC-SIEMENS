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
#from opcua import ua

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
        memoria=PLC.get_child("3:DataBlocksGlobal")
        variabili=memoria.get_child("3:variables")
        counter=variabili.get_child("3:ctr")
        condition=counter.get_value()
        var = memoria.get_child("3:waveforms")
        variabile = var.get_child("3:value1")
        #struttura = var.get_child("3:y1")
        
        #amp=first.get_child("3:[time]")
        #opps=amp.get_value()
        
        amplitude = variabile.get_child("3:amplitude")
        tempo_val = variabile.get_child("3:time")
        z_1=1000
        while condition<1000:
            struttura = var.get_child("3:y1")
            '''
            for i in range (3000):
                elements = struttura.get_child("3:[{}]".format(i))
                '''
            # get a specific node knowing its node id   
            condition=counter.get_value()
            if condition!=z_1:
                valore = amplitude.get_value()
                tempo=tempo_val.get_value()
                print(tempo, valore, condition)
                with open('file.txt', 'a') as file:
                    file.write("{}".format(tempo) + "\t" + "{}".format(valore) + "\n")
    
            
            z_1=condition
            time.sleep(0.01)
        #value = var.get_data_value() # get value of node as a DataValue object
        #print(value)
        #var.get_value() # get value of node as a python builtin
        #var.set_value(ua.Variant([23], ua.VariantType.Int64)) #set node value using explicit data type
        #var.set_value(3.9) # set node value using implicit data type

        
        # subscribing to a variable node
        '''
        handler = SubHandler()
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
        time.sleep(1.1)
        #embed()

    finally:
        client.disconnect()
