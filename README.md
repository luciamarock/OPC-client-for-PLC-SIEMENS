# OPC-client-for-PLC-SIEMENS
OPCua Python client for PLC SIEMENS S7-1500  


OPCclient.tgz archive contains the software. 
Extract everything running the following command on linux:

$> tar -xzvf OPCclient.tgz

in the extracted folder you will find:

UaClient.py → first simple utility accessing PLC variables value via OPC protocol 

methods.py → simple utility for calling PLC methods 

metloopsub.py → method call in a loop for continuous data acquisition 

you will find a “data” folder where an example of acquired data and a visualization tool are provided. 
