# OPC-client-for-PLC-SIEMENS
OPCua Python client for PLC SIEMENS S7-1500  

## Description
A Python-based OPC UA client implementation for communicating with Siemens S7-1500 PLCs.

## Structure
The `OPCclient` folder contains the following components:

- `UaClient.py` - Basic utility for reading PLC variables via OPC UA protocol
- `methods.py` - Utility for executing PLC methods
- `metloopsub.py` - Continuous data acquisition script using method calls in a loop

## Data Visualization
The `data` folder includes:
- Example acquired data files
- `plotter.py` - A visualization tool for plotting acquired data

## Requirements
- Python 3.x
- opcua library
- numpy
- matplotlib


## How to Use

### 1. Basic Setup
1. Install the required Python packages:
   ```bash
   pip install opcua numpy matplotlib
   ```

2. Configure your PLC's OPC UA server address in the client scripts. The default is:
   ```
   opc.tcp://192.168.129.20:4840
   ```

### 2. Reading PLC Variables
To read variables from your PLC, use `UaClient.py`:

```python
from OPCclient.UaClient import Client

# Create client instance
client = Client("opc.tcp://YOUR_PLC_IP:4840")
client.connect()

# Access PLC variables
objects = client.get_objects_node()
PLC = objects.get_child(["3:PLC_1"])
```

### 3. Data Acquisition
You can acquire data using two main methods:

#### a. Single Method Calls
Use `methods.py` for single method executions:
- Execute PLC methods with parameters.
- Data is saved to `data/file.txt`.

#### b. Continuous Acquisition
Use `metloopsub.py` for continuous data acquisition:
- Implements subscription-based monitoring.
- Automatically collects data in a loop.
- Configurable sample size (default: 500 samples).

### 4. Data Visualization
To plot the acquired data:
1. Ensure your data is saved in `data/file.txt`.
2. Run the plotter script:
   ```bash
   python OPCclient/data/plotter.py
   ```
   This generates a time-series plot of the acquired data.

### 5. Example Usage

#### Example of Basic Data Acquisition
```python
from OPCclient.methods import Client

# Create client instance
client = Client("opc.tcp://192.168.129.20:4840")
client.connect()

# Execute method with parameters
test = methods.call_method(
    metodi,
    metodo,
    ua.Variant(1, ua.VariantType.Float),
    ua.Variant(0, ua.VariantType.Float)
)
```

### Notes
- Ensure your PLC's OPC UA server is running and accessible.
- Default port is `4840` for Siemens S7-1500.
- Data is stored in a tab-separated format in `file.txt`.
- The visualization tool supports basic time-series plotting.

## License
This project is licensed under GNU General Public License v3.0