# Python Refresher

## 1. Data Types and Their Methods

### 1.1 Strings (`str`)

Strings are used to represent text — such as interface names or hostnames.

### ✅ Use cases:

- Interface names: `"GigabitEthernet0/1"`
- Hostnames: `"leaf1"`
- IP addresses: `"10.0.0.1"`

### 🔧 Common operations:

```python
interface = "GigabitEthernet1/0/1"

print(interface.upper())               # GIGABITETHERNET1/0/1
print(interface.startswith("Gig"))     # True
print(interface.replace("GigabitEthernet", "Gi"))  # Gi1/0/1

```

### 💡 Real-world example:

```python
hostname = "leaf1"
command = f"ping {hostname}"
print(command)  # Output: ping leaf1

```

---

### 1.2 Integers and Floats (`int`, `float`)

Used to represent numerical values like port numbers, latency, and utilization.

### ✅ Use cases:

- Port numbers: `22`, `443`
- Latency and jitter: `3.8`, `0.5`
- CPU load: `45.3`

### 🔧 Common operations:

```python
latency = 4.6
if latency > 2.0:
    print("⚠️ High latency detected")

ssh_port = 22
print(f"Connecting to device via port {ssh_port}")

```

---

### 1.3 Booleans (`bool`)

Booleans represent truth values: `True` or `False`.

### ✅ Use cases:

- Link status (up/down)
- Ping result (success/failure)

### 🔧 Example:

```python
is_up = True

if is_up:
    print("Link is UP")
else:
    print("Link is DOWN")

```

---

### 1.4 Lists (`list`)

Lists are ordered collections of items, commonly used for device groups or interfaces.

### ✅ Use cases:

- List of devices: `["leaf1", "leaf2", "spine1"]`
- List of interfaces: `["Gig0/0", "Gig0/1"]`

### 🔧 Common operations:

```python
devices = ["leaf1", "leaf2", "spine1"]
devices.append("spine2")

for dev in devices:
    print(f"SSH into {dev}")

```

---

### 1.5 Dictionaries (`dict`)

Dictionaries store key-value pairs, commonly used to represent device attributes.

### ✅ Use cases:

- Device info: `{"hostname": "leaf1", "ip": "10.0.0.1"}`
- Interface details
- JSON API responses

### 🔧 Example:

```python
device = {
    "hostname": "leaf1",
    "mgmt_ip": "192.168.100.10",
    "os": "nxos"
}

print(device["hostname"])               # leaf1
print(device.get("serial", "unknown")) # fallback to "unknown"

```

### 🔁 List of dictionaries:

```python
inventory = [
    {"hostname": "leaf1", "ip": "10.1.1.1"},
    {"hostname": "leaf2", "ip": "10.1.1.2"},
]

for dev in inventory:
    print(f"Pinging {dev['hostname']} at {dev['ip']}")

```

---

### 1.6 NoneType (`None`)

`None` is used to indicate the absence of a value.

### 🔧 Example:

```python
status = None

if status is None:
    print("Device status unknown")

```

---

### 📋 Summary Table

| Type | Example | Use Case |
| --- | --- | --- |
| `str` | `"GigabitEthernet0/1"` | Interface name, CLI command |
| `int` | `22` | Port number |
| `float` | `3.75` | Latency, CPU load |
| `bool` | `True` | Link status |
| `list` | `["R1", "R2"]` | Device inventory |
| `dict` | `{"hostname": "R1", "ip": "10.0.0.1"}` | Device metadata |
| `None` | `None` | Empty value / waiting for data |

## 2. Conditional Statements

Conditional statements allow your code to make decisions. In network automation, you use them to apply different logic depending on the device's OS, platform, state, or inventory attributes.

### 2.1 if / elif / else

These keywords allow branching logic.

### Example: Platform check

```python
device = {
    "hostname": "leaf1",
    "os": "nxos"
}

if device["os"] == "nxos":
    print("Apply NX-OS configuration template.")
elif device["os"] == "iosxe":
    print("Apply IOS-XE configuration template.")
else:
    print("Unsupported OS")

```

---

### 2.2 Combining conditions

Use `and`, `or`, `not` to build more complex logic.

### Example: Check interface state and OS

```python
device = {
    "hostname": "spine1",
    "os": "nxos",
    "int_status": "down"
}

if device["os"] == "nxos" and device["int_status"] == "down":
    print("Shut/no shut the interface to bounce it")

```

---

### 2.3 Truthy and Falsy values

Python evaluates these as **False**:

- `0`
- `""` (empty string)
- `[]` (empty list)
- `{}` (empty dict)
- `None`
- `False`

Everything else is considered **True**.

### Example:

```python
interface_list = []

if interface_list:
    print("Interfaces found")
else:
    print("No interfaces available")

```

---

### 2.4 Ternary operator

Short syntax for simple if-else:

```python
status = "up"
color = "green" if status == "up" else "red"
print(color)  # green

```

---

### Real-world Examples

### 1. Choose command based on interface type:

```python
intf = "GigabitEthernet1/0/1"

if "Gigabit" in intf:
    cmd = "speed 1000"
elif "FastEthernet" in intf:
    cmd = "speed 100"
else:
    cmd = "speed auto"

```

### 2. Determine if ping was successful:

```python
ping_output = "!!!!"

if "!" in ping_output:
    print("Ping successful")
else:
    print("Ping failed")

```

## 3. Functions

Functions allow you to encapsulate logic and reuse code efficiently. In network automation, you often write functions for tasks like building configuration lines, parsing output, or handling API calls.

---

### 3.1 Defining a Function

```python
def greet_device(hostname):
    print(f"Connecting to {hostname}")

```

### Usage:

```python
greet_device("leaf1")
# Output: Connecting to leaf1

```

---

### 3.2 Functions with Arguments and Return Values

```python
def build_vlan_config(vlan_id, vlan_name):
    config = f"vlan {vlan_id}\\n name {vlan_name}"
    return config

```

### Usage:

```python
print(build_vlan_config(10, "Users"))
# Output:
# vlan 10
#  name Users

```

---

### 3.3 Default Parameter Values

```python
def connect(host, port=22):
    print(f"Connecting to {host} on port {port}")

```

### Usage:

```python
connect("192.168.1.1")       # port defaults to 22
connect("192.168.1.1", 443)  # override default port

```

---

### 3.4 Function Composition (Calling a Function Inside Another)

```python
def get_interface_status(interface):
    # Placeholder for logic
    return "up"

def print_interface_status(interface):
    status = get_interface_status(interface)
    print(f"Interface {interface} is {status}")

```

---

### 3.5 Real-world Use Case: Generate Interface Config

```python
def generate_interface_config(name, vlan):
    return f"interface {name}\\n switchport access vlan {vlan}"

config = generate_interface_config("Gig1/0/1", 20)
print(config)

```

---

### 3.6 Best Practices

- Function names should describe what the function does.
- Use `return` instead of `print` when the result will be used later.
- Keep functions small and focused.

---

## 3.7. *args and **kwargs

Python provides special syntax to pass a variable number of arguments to a function.

---

### `args`: Variable Positional Arguments

Used when you want to accept multiple positional arguments as a **tuple**.

### Example:

```python
def show_interfaces(*interfaces):
    for intf in interfaces:
        print(f"Checking status of {intf}")

```

### Usage:

```python
show_interfaces("Gig0/0", "Gig0/1", "Gig0/2")

```

---

### `*kwargs`: Variable Keyword Arguments

Used when you want to accept multiple named arguments as a **dictionary**.

### Example:

```python
def configure_device(**kwargs):
    for key, value in kwargs.items():
        print(f"{key} = {value}")

```

### Usage:

```python
configure_device(hostname="leaf1", mgmt_ip="192.168.0.1", os="nxos")

```

---

### Combining `args` and `*kwargs`

```python
def deploy_script(script_name, *devices, **options):
    print(f"Deploying {script_name} to devices: {devices}")
    print("Options provided:")
    for key, value in options.items():
        print(f"  {key}: {value}")

```

### Usage:

```python
deploy_script(
    "backup_config.py",
    "leaf1", "leaf2",
    timeout=5, retries=3
)

```

---

### Real-World Example: Send Commands to Devices

```python
def send_commands(device, *commands):
    print(f"Connecting to {device}...")
    for cmd in commands:
        print(f"Sending command: {cmd}")

```

```python
send_commands("leaf1", "show version", "show ip interface brief")

```

---

### Key Points

- Use `args` when your function takes many unnamed values.
- Use `*kwargs` for flexible options or configuration parameters.
- In network scripts, they help you write **reusable** and **configurable** functions.

---

## 4. File Operations

File operations are essential when you want to:

- Save command outputs to files
- Read configuration templates
- Log automation results

---

### 4.1 Reading from a File

```python
with open("devices.txt", "r") as file:
    devices = file.readlines()

for line in devices:
    print(line.strip())

```

> "r" stands for read mode.
> 

---

### 4.2 Writing to a File

```python
output = "interface GigabitEthernet1/0/1\\n switchport access vlan 10"

with open("interface_config.txt", "w") as file:
    file.write(output)

```

> "w" stands for write mode. It overwrites the file if it exists.
> 

---

### 4.3 Appending to a File

```python
log = "leaf1 - backup completed\\n"

with open("backup_log.txt", "a") as file:
    file.write(log)

```

> "a" stands for append mode.
> 

---

### 4.4 Reading a Config Template

```python
with open("base_config.txt") as f:
    template = f.read()

config = template.replace("{{hostname}}", "leaf1")
print(config)

```

---

### 4.5 Real-World Example: Save Ping Results

```python
devices = ["leaf1", "leaf2"]

with open("ping_results.txt", "w") as log_file:
    for dev in devices:
        result = f"Pinged {dev}: Success\\n"
        log_file.write(result)

```

---

### Best Practices

- Always use `with open(...)` syntax — it handles file closing for you.
- Use `.strip()` to clean newline characters when reading.
- Be careful with `"w"` mode — it will delete old content.

---

## 5. Modules

Modules allow you to organize your code and reuse existing functionality. Python comes with many built-in modules and allows you to install external ones.

---

### 5.1 Importing Built-in Modules

### Example: Using `os` to interact with the operating system

```python
import os

print(os.getcwd())  # Current working directory

```

### Example: Using `time` to add delays

```python
import time

print("Waiting for device to reboot...")
time.sleep(5)  # wait for 5 seconds
print("Done")

```

---

### 5.2 Importing Specific Functions

```python
from math import sqrt

print(sqrt(16))  # Output: 4.0

```

---

### 5.3 Using Aliases

```python
import datetime as dt

now = dt.datetime.now()
print(now)

```

---

### 5.4 Installing External Modules

To install third-party modules, use `pip`:

```bash
pip install netmiko

```

Then in Python:

```python
from netmiko import ConnectHandler

```

---

### 5.5 Real-World Example: Netmiko SSH Connection

```python
from netmiko import ConnectHandler

device = {
    "device_type": "cisco_ios",
    "ip": "192.168.1.1",
    "username": "admin",
    "password": "cisco123"
}

net_connect = ConnectHandler(**device)
output = net_connect.send_command("show version")
print(output)
net_connect.disconnect()

```

---

### Best Practices

- Keep imports at the top of your script
- Use only what you need (`import module` vs `from module import something`)
- Use virtual environments to isolate project dependencies

---

## 6. Data Formats (CSV, JSON, XML)

Network automation often involves working with structured data formats. Python has built-in and external libraries to parse and generate them.

---

### 6.1 CSV (Comma-Separated Values)

CSV is commonly used to store inventory or tabular data.

### Example CSV content (`devices.csv`):

```
hostname,ip
leaf1,192.168.1.1
leaf2,192.168.1.2

```

### Reading CSV in Python:

```python
import csv

with open("devices.csv") as file:
    reader = csv.DictReader(file)
    for row in reader:
        print(row["hostname"], row["ip"])

```

---

### 6.2 JSON (JavaScript Object Notation)

JSON is widely used in REST APIs and configuration files.

### Example JSON:

```json
{
  "hostname": "leaf1",
  "ip": "192.168.1.1",
  "os": "nxos"
}

```

### Working with JSON in Python:

```python
import json

# Convert dict to JSON string
device = {"hostname": "leaf1", "ip": "192.168.1.1"}
json_str = json.dumps(device)

# Convert JSON string to dict
parsed = json.loads(json_str)
print(parsed["ip"])

```

### Reading JSON from a file:

```python
with open("device.json") as f:
    data = json.load(f)
    print(data["hostname"])

```

---

### 6.3 XML (eXtensible Markup Language)

XML is commonly used with NETCONF and older APIs.

### Example XML:

```xml
<device>
  <hostname>leaf1</hostname>
  <ip>192.168.1.1</ip>
</device>

```

### Parsing XML with `xml.etree.ElementTree`:

```python
import xml.etree.ElementTree as ET

xml_data = '''
<device>
  <hostname>leaf1</hostname>
  <ip>192.168.1.1</ip>
</device>
'''

root = ET.fromstring(xml_data)
hostname = root.find("hostname").text
ip = root.find("ip").text
print(hostname, ip)

```

---

### When to Use What?

| Format | Use Case | Library |
| --- | --- | --- |
| CSV | Inventory, tabular config | `csv` |
| JSON | REST API, structured data | `json` |
| XML | NETCONF, device metadata | `xml.etree` |

---

## 7. Classes

Classes allow you to define your own custom data types. They are useful for modeling devices, interfaces, configurations, or any reusable logic in network automation.

---

### 7.1 Defining a Class

```python
class NetworkDevice:
    def __init__(self, hostname, ip, os):
        self.hostname = hostname
        self.ip = ip
        self.os = os

    def connect(self):
        print(f"Connecting to {self.hostname} at {self.ip} via {self.os}")

```

### Usage:

```python
device1 = NetworkDevice("leaf1", "192.168.1.1", "nxos")
device1.connect()

```

---

### 7.2 Class Attributes and Methods

- **Attributes** store data (like `hostname`, `ip`)
- **Methods** perform actions (like `connect()`)

---

### 7.3 Adding More Behavior

```python
class NetworkDevice:
    def __init__(self, hostname, ip, os):
        self.hostname = hostname
        self.ip = ip
        self.os = os
        self.status = "disconnected"

    def connect(self):
        self.status = "connected"
        print(f"{self.hostname} connected")

    def disconnect(self):
        self.status = "disconnected"
        print(f"{self.hostname} disconnected")

    def show_status(self):
        print(f"{self.hostname} is {self.status}")

```

---

### 7.4 Inheritance

You can create a new class based on an existing one:

```python
class CiscoDevice(NetworkDevice):
    def enable_secret(self):
        print("Entering enable mode...")

```

### Usage:

```python
r1 = CiscoDevice("router1", "10.1.1.1", "ios")
r1.connect()
r1.enable_secret()

```

---

### When to Use Classes

- Managing device states (connected, disconnected)
- Building structured tools or frameworks
- Organizing related functions under one object

---

### Best Practices

- Use class names in **PascalCase** (e.g., `NetworkDevice`)
- Keep your classes focused and reusable
- Combine with modules to structure large automation tools

---
