# Ansible Usage

## **Chapter 1: Introduction to Ansible for Network Engineers**

---

### **1.1 What is Ansible?**

Ansible is a simple, powerful, and `agentless` IT automation tool. It is mostly used for configuration management, application deployment, and task automation. Unlike other tools, Ansible does not require an agent to be installed on the managed device. It uses `SSH` (or `API` for some platforms) to communicate.

For network engineers, this means you can automate routers, switches, and firewalls without needing to install anything on the devices.

---

### **1.2 Why Should a Network Engineer Use Ansible?**

Traditionally, network engineers log into each router or switch and apply configuration manually. In large-scale environments, this is:

- Time-consuming
- Error-prone
- Hard to repeat consistently

With Ansible, you can:

- Push configuration to **many devices at once**
- Maintain **configuration consistency**
- **Backup** device configs automatically
- Run **compliance checks**
- Integrate with **version control systems** like Git
- Schedule routine tasks easily

Example: If you want to configure NTP settings on 50 routers, instead of logging into each router, you write one playbook and run it once. Ansible takes care of the rest.

---

### **1.3 How Ansible Works (High-Level Overview)**

Ansible uses a **control node** (your computer or server where Ansible is installed) to manage **managed nodes** (in this case, network devices).

Key components:

- **Control node**: Where you run Ansible commands and playbooks.
- **Managed nodes**: Devices (routers, switches) accessed via SSH or API.
- **Inventory file**: A list of devices with their IP addresses and credentials.
- **Modules**: Predefined functions to interact with devices (e.g., ios_config for Cisco IOS).
- **Playbook**: A YAML file where tasks are defined step-by-step.

---

### **1.4 A Network-Centric Example**

Let’s say you want to change the hostname of 3 routers.

**Manual method:**

You SSH to each device and run:

```
conf t
hostname R1
```

**Ansible method:**

You define a `playbook` once and run it. Ansible connects to each router and applies the hostname automatically. All three process are `occurred  parallel`.

Result: same configuration, faster, and less error-prone.

---

### **1.5 Ansible for Network Operating Systems**

Ansible supports many network OS platforms:

- Cisco IOS / IOS-XE
- Cisco NX-OS
- Juniper JunOS
- Arista EOS
- Palo Alto, Fortinet, etc.

Each platform has its own module collection (e.g., cisco.ios, cisco.nxos). These modules allow Ansible to understand how to talk to the device.

Example modules:

- ios_config: send configuration commands to Cisco IOS devices.
- ios_facts: collect device facts like hostname, version, interfaces.
- nxos_facts: collect info from Nexus switches.

---

## **Chapter 2: Installing Ansible and Preparing a Lab Environment**

### **2.1 Installing Ansible on the Control Node**

Ansible works best on a Linux-based system (Ubuntu, Debian, CentOS, etc.). You can also install it on macOS using brew.

### **📌 For Ubuntu/Debian:**

```
sudo apt update
sudo apt install ansible -y
```

or in python

```bash
sudo apt install python3.12-venv # install virtual environment
python3 -m venv dcaui # create virtual environment
source dcaui/bin/activate # activate virtual environment

pip install ansible # install ansible
```

✎ python include newer version of ansible. I recommend python and pip.

To verify the installation:

```
ansible --version
```

You should see output with the Ansible version and Python path.

---

### **2.2 Creating a Basic Network Lab**

For practicing Ansible in a network environment, you’ll need some routers/switches. The most common ways to build this:

### **Option 1: EVE-NG or GNS3 (Recommended)**

You can emulate Cisco IOS devices (IOSv, IOS-XE) using:

- **EVE-NG**
- **GNS3**
- **Physical Device**

Upload Cisco images such as:

- csr1000v-universalk9
- IOSv
- NX-OS
- ACI simulator etc.

**Lab topology:**

![image.png](Ansible%20Usage%20235bf5a1d42080e0890cfd9f5c1a4c74/image.png)

---

### **2.3 Configuring Cisco Device for Ansible Access**

To use Ansible with Cisco IOS devices, routers, nexuses, switches must support SSH and be reachable from the Ansible host and ACI must be accessible over `api`

---

### **2.4 Testing SSH Access**

From your Ansible control node (Linux):

If you’re able to log in, SSH is working. If not:

- Check connectivity (ping)
- Check credentials
- Check VTY/SSH config

---

### **2.5 Preparing the Inventory File**

Create a folder to store your Ansible files:

```
mkdir ~/network-ansible
cd ~/network-ansible
touch inventory.ini
```

Add the following to inventory.ini:

```
[nexuses]
nxos_01 ansible_host=192.168.64.101
nxos_02 ansible_host=192.168.64.100
nxos_always_on ansible_host=sbx-nxos-mgmt.cisco.com ansible_user=admin ansible_password=Admin_1234!

[nexuses:vars]
ansible_connection=network_cli
ansible_user=admin
ansible_network_os=nxos
ansible_password=112233on!
host_key_checking=false
# ansible_become=yes
# ansible_become_method=enable
# ansible_become_password=enablepass
```

you can check ssh connection over ansible with: `ansible nexuses -I inventory.ini -m cisco.nxos.nxos_command a- “commands=’show hostname’” -o` cli level check ssh connection, then send command, display output  or you can use more small command.

```bash
ansible routers -i inventory.yml -m ios_facts
```

when you run command, you might encounter an error that is about fingerprint. There are options here:

- you can do ssh connection on console before execution to store fingerprint
- you can bypass `host_key_checking` with `false` parameter in ansible.cfg file  like below

```bash

[defaults]
host_key_checking=false
```

---

**PS:**  or you can use .yml file instead of .ini

```yaml
all:
	children:
		nexuses:
			hosts:
				nexus_01:
					ansible_host: 192.168.64.100
					ansible_user: admin
					ansible_password: 112233on!
					ansible_connection: network_cli
					ansible_network_os: nxos
				nexus_02:
					ansible_host: 192.168.64.101
					ansible_user: admin
					ansible_password: 112233on!
					ansible_connection: network_cli
					ansible_network_os: nxos
				nexus_always_on:
				  ansible_host: sbx-nxos-mgmt.cisco.com
          ansible_user: admin
          ansible_password: Admin_1234!
          ansible_connection: network_cli
					ansible_network_os: nxos
```

or merge common parameters

```yaml
all:
	children:
		nexuses:
			hosts:
				nexus_01:
					ansible_host: 192.168.64.100
				nexus_02:
					ansible_host: 192.168.64.101
			vars:
				ansible_user: admin
				ansible_password: 112233on!
				ansible_connection: network_cli
				ansible_network_os: nxos
```

---

Expected output: facts about the device (hostname, version, interfaces).

---

## **Chapter 3: Inventory File and Device Grouping**

### **3.1 Grouping Devices by Function or Location**

---

Inventory groups can represent:

- **Device role:** routers, switches, firewalls
- **Location:** datacenter1, branch_office2
- **OS type:** ios_devices, nxos_devices

### **Example:**

```yaml
all:
  children:
    dc_nexuses:
      hosts:
        nexus_01:
          ansible_host: 192.168.64.100
        nexus_02:
          ansible_host: 192.168.64.101

    branch_routers:
      hosts:
        br1:
          ansible_host: 10.1.1.1
        br2:
          ansible_host: 10.1.1.2

    all_devices:
      children:
        dc_nexuses:
        branch_routers:
      vars:
        ansible_user: admin
        ansible_password: cisco123
        ansible_network_os: ios
        ansible_connection: network_cli
```

Now, you can run a playbook just on core_routers, branch_routers, or all using all_routers.

---

### **3.2 Best Practices**

- Use **hostnames** (aliases) instead of raw IPs in playbooks.
- Store **group-specific variables** using [group:vars] to avoid duplication.
- For large environments, split the inventory into multiple files or directories (using inventory/ folder).
- Use **ansible-vault** to encrypt passwords.

---

### **3.3 Testing Grouping**

To test which devices are in a group:

```
ansible all -i inventory.ini --list-hosts
ansible branch_routers -i inventory.ini --list-hosts
```

To run a command (e.g., collect facts) on a specific group:

```
ansible core_routers -i inventory.ini -m ios_facts
```

---

## **Chapter 4: Modules and Ad-Hoc Commands**

### **4.1 What is a Module?**

A **module** is a reusable unit of work in Ansible.

Modules are used inside playbooks or directly from the command line (ad-hoc).

Each module does **one job**: send a command, change config, get facts, etc.

### **Example modules used in networking:**

| **Module Name** | **Description** |
| --- | --- |
| nxos_config | Apply configuration commands |
| nxos_facts | Get data from Cisco NX-OS switches |
| ping | Ping module for Linux hosts (not routers) |

---

### **4.2 What is an Ad-Hoc Command?**

Ad-hoc commands let you **run a single task** on one or more devices without writing a playbook.

It’s very useful for:

- Testing connection
- Gathering info (facts)
- Sending quick CLI commands
- Making one-time configuration changes

### **General Syntax:**

```
ansible <group> -i inventory.ini -m <module> -a "<arguments>"
```

---

### **4.3 Ad-Hoc Examples for Network Devices**

### **✅ Test connection to routers (should use a network module):**

```
ansible nexuses -i inventory.ini -m nxos_facts
```

### **✅ Run a show command (e.g., show version):**

```
ansible nexus_02 -i inventory.yml -m nxos_command -a "commands='show version'"
```

for multi line commands

```bash
ansible nxos_hosts -m cisco.nxos.nxos_command -a '{"commands": ["show version", "show ip route"]}'
```

---

### **4.4 Output Explanation**

Ansible will return a JSON-style output with information like:

- changed: true: means something was modified on the device.
- changed: false: means nothing was changed (already in desired state).
- stdout: command output (for show commands).
- failed: true: an error occurred.

### **Sample output of**

### **ios_command:**

```
"stdout": [
  "Interface IP-Address OK? Method Status Protocol\nGig0/0 192.168.1.1 YES manual up up"
]
```

---

### **4.5 Dry Run (Check Mode)**

Some modules support --check mode (like ios_config). This means:

> “Show me what would change, but don’t actually apply anything.”
> 

```
ansible routers -i inventory.ini -m ios_config -a "lines=['hostname TestRouter']" --check
```

This helps prevent accidental changes.

```bash

ansible nxos_02 -i inventory.yml -m cisco.nxos.nxos_config -a 'lines="ip address 1.1.1.2/32" parents="interface loopback2"'
ansible nxos_02 -i inventory.yml -m cisco.nxos.nxos_config -a '{"lines": ["ip address 1.1.1.2/32"], "parents": ["interface loopback2"]}'
ansible nxos_02 -i inventory.yml -m cisco.nxos.nxos_config -a 'lines="interface loopback2,ip address 1.1.1.2/32"'
```

---

### **4.6 Useful Built-in CLI Options**

| **Option** | **What it does** |
| --- | --- |
| -i inventory.ini | Specifies the inventory file |
| -m | Specifies the module to use |
| -a | Provides arguments for the module |
| -v, -vvv | Verbose output for troubleshooting |
| --limit | Run on a specific host/group |
| --check | Dry-run mode |

---

## **Chapter 5: Writing Your First Playbook**

### **5.1 What is a Playbook?**

A **playbook** is a YAML file where you define the tasks that Ansible should execute on one or more devices.

Playbooks describe the **desired state** of devices. Ansible ensures that configuration matches what you define — if it’s already correct, it won’t change anything.

---

### **5.2 Basic Structure of a Playbook**

A simple playbook includes:

- **name** – a human-readable title
- **hosts** – the group or devices to apply the playbook to
- **gather_facts** – used for Linux hosts, typically set to no for network devices
- **connection** – specifies the type of connection (network_cli for Cisco IOS)
- **tasks** – a list of steps to run on the target devices

---

### **5.3 Example 1: Set Loopback interface on Cisco Nexus**

**File:** set_loopback_on_nxos.yml

```yaml
- name: Set loopback
  hosts: nexus_02
  gather_facts: no

  tasks:
    - name: Set loopback interface
      ios_config:
        lines:
          - interface loopback01
          - ip address 1.1.1.1/32
          - description "user 01 config by Ansible"
```

### **Explanation:**

- hosts: routers – runs on the group or single, in this lab scenario called `nxos_02`  in your inventory file.
- ios_config – module used to send configuration lines to Cisco IOS devices.

---

### **5.4 Running the Playbook**

Use the following command to execute the playbook:

```
ansible-playbook -i inventory.yml 00_set_loopback_on_nxos.yml
```

Expected output:

```
changed:[nxos_02]
```

This means the configuration done successfully and changed on device.

---

### **5.5 Example 2: Display Output on Console**

**File:**set_loopback_on_nxos_with_result.yml

```yaml
- name: Set loopback
  hosts: nxos_02
  gather_facts: no
  connection: network_cli

  tasks:
    - name: Set loopback interface
      nxos_config:
        lines:
          - interface loopback 1
          - ip address 1.1.1.1/32
          - description "user 01 config by Ansible"
      register: result

    - name: Display result
      debug:
        var: result
```

### **Explanation:**

- Register config output to `result`
- Display `result` to console

---

### **5.6 Common Parameters in**

### **nxos_config**

| **Parameter** | **Description** |
| --- | --- |
| lines | The config lines to send |
| parents | The parent config context (e.g., interface Eth1/1) |
| before | Commands to run before applying the main lines |
| after | Commands to run after the main lines |
| match | Check mode to ensure config is only updated if needed |
| replace | Control how lines are replaced (line, block, etc) |

---

### **5.7 Best Practices for Writing Playbooks**

- Make sure indentation is consistent.
- Use variables to make playbooks reusable across different devices.
- Test changes first with --check mode to avoid unexpected behavior.
- Organize playbooks by function or role (e.g., hostname, interfaces, NTP).

---

## **Chapter 6: Templating and Jinja2 Basics**

### **6.1 What is Templating?**

Templating allows you to **generate configurations dynamically** using variables.

Instead of hardcoding interface names, IPs, or hostnames, you define templates that insert values from your inventory or variable files.

Ansible uses the **Jinja2** templating engine for this purpose.

---

### **6.2 Why Network Engineers Need Jinja2**

In real-world networks:

- Devices have **similar configurations** with small differences (e.g., Loopback IP, hostname, AS number).
- You want to **automate** config generation based on device-specific data.

Jinja2 makes this possible.

---

### **6.3 Example Scenario**

You want to configure Loopback interfaces on 3 routers, each with a different IP address.

Instead of writing 3 separate playbooks, you can write **one template** that reads values from variables.

---

### **6.4 Step-by-Step: Creating a Jinja2 Template**

### **1. Create a Jinja2 template file**

**File:** router_config.j2

```
hostname {{ hostname }}

interface {{ interface_name }}
  ip address {{ ip_address }} {{ subnet_mask }}
  no shutdown

{% if description is defined %}
description {{ description }}
{% endif %}

router ospf {{ ospf_process_id }}
  network {{ ospf_network }} {{ ospf_wildcard }} area {{ ospf_area }}
```

```yaml
- name: Configure Cisco Router with Jinja2 template
  hosts: routers
  gather_facts: no

  vars:
    hostname: R1
    interface_name: GigabitEthernet0/0
    ip_address: 192.168.1.1
    subnet_mask: 255.255.255.0
    description: Uplink to ISP
    ospf_process_id: 1
    ospf_network: 192.168.1.0
    ospf_wildcard: 0.0.0.255
    ospf_area: 0

  tasks:
    - name: Render Jinja2 template to a config file
      template:
        src: router_config.j2
        dest: router_config.txt

    - name: Push configuration to router
      ios_config:
        src: router_config.txt
```

---

### **6.5 Explanation**

- The template module takes your Jinja2 file and fills in variables.
- dest: defines where the rendered output will be saved.
- ios_config then reads from that file and applies the configuration to the device.

---

### **6.6 Common Jinja2 Syntax**

| **Syntax Example** | **Meaning** |
| --- | --- |
| {{ var_name }} | Insert a variable |
| {% if condition %} | Start a conditional block |
| {% for item in list %} | Start a loop |
| {{ inventory_hostname }} | Built-in variable for device name |

---

### **6.7 Jinja2 Conditional Example**

```
{% if ospf_enabled %}
router ospf 1
 network {{ loopback_ip }} 0.0.0.0 area 0
{% endif %}
```

```yaml
...
router_0x:
	ansible_host: 192.168.1.1
	ospf_enabled: true
	loopback_ip: 1.1.1.1
...
```

### 6.8 Write output on file

You want to store `result` of ansible execution.

```yaml

- name: Set loopback
  hosts: nxos_02
  gather_facts: no
  connection: network_cli

  tasks:
    - name: Set loopback interface
      nxos_config:
        lines:
          - interface loopback 1
          - ip address 1.1.1.1/32
          - description "user 01 config by Ansible"
      register: result

    - name: Write result on file
      copy:
        content: "{{ result['updates'] | to_nice_json}}"
        dest:  /config/workspace/result.txt
```

---

## **Chapter 7: Roles and Modular Playbook Design**

### **7.1 What is a Role?**

A **role** is a self-contained directory structure that organizes:

- Tasks
- Templates
- Variables
- Files
- Handlers

Each role performs **one function** (e.g., configure NTP, set hostname, deploy BGP).

Roles make your playbooks **modular**, **maintainable**, and **reusable**.

---

### **7.2 When to Use Roles**

Use roles when:

- Your playbooks are becoming long or repetitive.
- You want to reuse the same config logic across different projects.
- You’re working in a team and need consistent structure.

---

### **7.3 Role Directory Structure**

```
roles/
├── hostname_config/
│   ├── tasks/
│   │   └── main.yml
│   ├── templates/
│   └── vars/
│       └── main.yml
```

You can create this structure manually or with the CLI:

```
ansible-galaxy init hostname_config
```

---

### **7.4 Example: Create a Role to Configure Hostnames**

### **Step 1: Create the role**

```
ansible-galaxy init set_interface
```

### **Step 2: Add the task**

**roles/set_interface/tasks/main.yml**

```yaml
- name: set interface
  cisco.nxos.nxos_config:
    lines:
      - interface {{ interface_name }}
      - ip address {{ ip_address }}
      - description {{ description }}
```

### **Step 4: Define Variable**

```yaml
interface_name: loopback10
ip_address: 1.1.1.10/32
description: created by user10
```

---

### **Step 5: Use the role in a playbook**

**playbook.yml**

```yaml
- name: Set interface
  hosts: nxos_02
  gather_facts: no
  connection: network_cli

  roles:
    - set_interface
```

---

### **Chapter 8: Real-World Examples and Best Practices (NX-OS & ACI)**

---

### **8.1 Overview**

In large-scale enterprise and data center environments, tasks such as **config backup**, **interface configuration**, and **fabric policy management** are repeated across hundreds of switches. Ansible can simplify and standardize these tasks.

In this chapter, we will cover:

- Automating Cisco NX-OS configuration using Ansible modules.
- Interacting with Cisco ACI via the Ansible ACI collection (using the ACI API).
- Best practices for data modeling and role design.

---

### **8.2 NX-OS Automation: Backup Running Configuration**

**Playbook: backup_nxos_config.yml**

```yaml
- name: Backup NX-OS Running Config
  hosts: nxos_switches
  gather_facts: no
  connection: network_cli

  tasks:
    - name: Fetch running configuration
      nxos_config:
        backup: yes
```

The file will be saved in the default Ansible working directory under backup/ with filenames like leaf1.cfg.

---

### **8.3 NX-OS: Interface Configuration Example**

**Task: Configure interface Ethernet1/1 on all leaf switches**

**Playbook: nxos_interface_config.yml**

```yaml
- name: Configure interfaces on Nexus switches
  hosts: nxos_switches
  gather_facts: no
  connection: network_cli

  tasks:
    - name: Set interface description and enable
      nxos_config:
        lines:
          - description Uplink to Spine
          - no shutdown
        parents: interface Ethernet1/1
```

> parents: ensures the lines are placed under the correct interface context.
> 

---

### **8.4 ACI Automation: Create a Tenant and VRF**

Cisco ACI is managed through an API and requires **HTTPS/API-based modules**. Ansible communicates with the ACI fabric via REST API.

First, install the ACI collection:

```
ansible-galaxy collection install cisco.aci
```

**Inventory (inventory.yml)**

```yaml
    aci:
      hosts:
        aci_01:
```

---

### **Playbook: Create a Tenant and a VRF**

**File: aci_tenant_vrf.yml**

```yaml
- name: Create ACI Tenant and VRF
  hosts: aci_01
  gather_facts: no
  
  tasks:
    - name: Create Tenant
      cisco.aci.aci_tenant:
        host: 192.168.71.15
        username: admin
        password: Cisco123
        tenant: User10-Tenant
        description: Created by Ansible
        state: present
        validate_certs: false
      delegate_to: localhost

    - name: Create VRF
      cisco.aci.aci_vrf:
        host: 192.168.71.15
        username: admin
        password: Cisco123
        tenant: User10-Tenant
        vrf: User10-VRF
        description: Tenant VRF
        state: present
        validate_certs: false
      delegate_to: localhos
```

> These modules call the ACI APIC REST API behind the scenes.
> 

---

Continue with bridge domain 🙂

![image.png](Ansible%20Usage%20235bf5a1d42080e0890cfd9f5c1a4c74/58b43d97-4a93-4aa5-8daa-910856d36c9b.png)
