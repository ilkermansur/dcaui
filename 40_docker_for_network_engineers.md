# Docker for Network Engineers - Complete Instructor's Guide

## Table of Contents

- [Chapter 1: Introduction - Why Network Engineers Should Learn Docker](#chapter-1-introduction---why-network-engineers-should-learn-docker)
- [Chapter 2: Docker Fundamentals - Images, Containers, Volumes](#chapter-2-docker-fundamentals---images-containers-volumes)
- [Chapter 3: Docker Networking Concepts](#chapter-3-docker-networking-concepts)
- [Chapter 4: Hands-On - Setting Up Docker in a Lab Environment](#chapter-4-hands-on---setting-up-docker-in-a-lab-environment)
- [Chapter 5: Networking Modes - Bridge, Host, None, and Custom Networks](#chapter-5-networking-modes---bridge-host-none-and-custom-networks)
- [Chapter 6: Practical Examples - Network Simulations & Topologies](#chapter-6-practical-examples---network-simulations--topologies)
- [Chapter 7: Integrating Docker with Network Tools](#chapter-7-integrating-docker-with-network-tools)
- [Chapter 8: Advanced Networking - Overlay, Macvlan, and Multi-Host](#chapter-8-advanced-networking---overlay-macvlan-and-multi-host)
- [Chapter 9: Security Considerations for Containerized Networks](#chapter-9-security-considerations-for-containerized-networks)
- [Chapter 10: Troubleshooting Docker Networks](#chapter-10-troubleshooting-docker-networks)
- [Chapter 11: Real World Use Cases for Network Engineers](#chapter-11-real-world-use-cases-for-network-engineers)
- [Chapter 12: Summary & Further Resources](#chapter-12-summary--further-resources)

---

## **Chapter 1: Introduction - Why Network Engineers Should Learn Docker**

---

### **1.1 Evolution of Network Infrastructure**

The networking landscape has dramatically evolved over the past decade. Traditional network management approaches that worked well in static environments are becoming increasingly inadequate for modern, dynamic infrastructures.

**Traditional Networking Challenges:**
- Manual configuration processes prone to human error
- Inconsistent environments between development, testing, and production
- Difficulty in scaling network services quickly
- Limited ability to reproduce network scenarios
- Time-consuming troubleshooting and testing processes

**The Container Revolution:**
Docker has revolutionized how applications are developed, deployed, and managed. For network engineers, containers offer a powerful way to:
- Create consistent, reproducible network environments
- Simulate complex network topologies
- Deploy network tools and services rapidly
- Implement Infrastructure as Code (IaC) principles
- Enable DevOps practices in network operations

---

### **1.2 Benefits of Containerization for Network Engineers**

**🔧 Consistency Across Environments**
```bash
# Same network service runs identically across different hosts
docker run -d --name network-monitor \
  -p 8080:8080 \
  monitoring-app:latest
```

**📦 Isolation and Resource Management**
- Each containerized network service runs in its own isolated environment
- Prevents conflicts between different tools and their dependencies
- Precise resource allocation and limitation

**⚡ Rapid Deployment and Scaling**
```bash
# Deploy multiple instances of a network service instantly
docker-compose up --scale web-server=5
```

**🔄 Version Control and Rollbacks**
- Network configurations and tools can be versioned
- Easy rollback to previous working configurations
- Consistent deployment across different environments

**💰 Cost Efficiency**
- Better resource utilization compared to VMs
- Reduced infrastructure overhead
- Faster startup times enable more efficient testing

---

### **1.3 Common Use Cases and Scenarios**

**Network Testing and Validation**
```bash
# Quickly spin up a test environment
docker run -it --rm --network host \
  network-tester:latest \
  ping -c 4 192.168.1.1
```

**Tool Deployment**
- Deploy monitoring solutions (Zabbix, PRTG, LibreNMS)
- Run network analysis tools (Wireshark, tcpdump)
- Create custom network utilities

**Lab Environments**
```bash
# Create isolated lab networks
docker network create --driver bridge \
  --subnet 10.0.1.0/24 \
  lab-network
```

**Automation and CI/CD**
- Automated network configuration testing
- Infrastructure validation pipelines
- Continuous integration for network changes

---

### **1.4 Prerequisites and Learning Objectives**

**Prerequisites:**
- Basic understanding of networking concepts (TCP/IP, routing, switching)
- Command-line interface experience (Linux/Unix)
- Familiarity with network protocols and services
- Basic understanding of virtualization concepts

**Learning Objectives:**
By the end of this course, you will be able to:
1. Understand Docker's core concepts and networking architecture
2. Deploy and manage containerized network services
3. Create complex network topologies using Docker
4. Implement network monitoring and troubleshooting solutions
5. Integrate Docker into existing network operations workflows
6. Apply security best practices for containerized networks
7. Troubleshoot common Docker networking issues
8. Design and implement real-world network automation solutions

**📚 Course Structure:**
This instructor-led course combines theoretical knowledge with hands-on practical exercises. Each chapter builds upon previous concepts and includes:
- Detailed explanations with network-focused examples
- Command-line exercises and configurations
- Real-world scenarios and use cases
- Troubleshooting tips and common pitfalls
- Hands-on lab exercises

---

### **💡 Why Docker Matters for Network Engineers**

**Traditional Approach:**
```bash
# Installing tools on host system (potential conflicts)
sudo apt-get install wireshark tcpdump nmap
# Configuration management becomes complex
# Different versions across different hosts
```

**Docker Approach:**
```bash
# Consistent, isolated tool deployment
docker run -it --rm --net=host \
  nicolaka/netshoot \
  nmap -sn 192.168.1.0/24
```

**Key Advantages for Network Engineers:**
1. **Reproducibility**: Same network environment every time
2. **Isolation**: No conflicts between tools or configurations
3. **Portability**: Run anywhere Docker is supported
4. **Scalability**: Easy to scale network services
5. **Automation**: Perfect for CI/CD pipelines and automation

---

### **🛠️ Chapter 1 Hands-On Exercise**

**Exercise 1.1: Understanding the Docker Advantage**

**Scenario:** You need to quickly test network connectivity from multiple source points with different tool versions.

**Traditional Method (Time-consuming):**
1. Install tools on multiple systems
2. Ensure consistent configurations
3. Manage different versions and dependencies
4. Deal with potential conflicts

**Docker Method (Efficient):**
```bash
# Test from different "hosts" instantly
docker run --rm nicolaka/netshoot ping -c 3 google.com
docker run --rm nicolaka/netshoot traceroute google.com
docker run --rm nicolaka/netshoot nslookup google.com
```

**Exercise Tasks:**
1. Research three network tools you regularly use
2. Find their Docker container equivalents
3. Compare deployment time: traditional vs. containerized
4. Document the benefits you observe

**Expected Outcome:**
Students will understand the practical advantages of containerized network tools and begin to see how Docker can streamline their daily network operations.

---

## **Chapter 2: Docker Fundamentals - Images, Containers, Volumes**

---

### **2.1 Core Docker Concepts for Network Engineers**

Understanding Docker's fundamental concepts is crucial for network engineers who want to leverage containerization effectively. Let's explore these concepts through a networking lens.

**🏗️ Docker Architecture Overview**

```
Docker Client (docker CLI) ←→ Docker Daemon (dockerd) ←→ Container Runtime
                                      ↓
                              Images, Containers, Networks, Volumes
```

**Docker Components:**
- **Docker Client**: Command-line interface you interact with
- **Docker Daemon**: Background service managing containers
- **Container Runtime**: Executes and manages container lifecycle
- **Registry**: Storage for Docker images (Docker Hub, private registries)

---

### **2.2 Images vs Containers - The Network Perspective**

**🖼️ Docker Images**
Think of a Docker image as a **network appliance template** - it contains everything needed to run a specific network service or tool.

```bash
# List available images
docker images

# Search for network-related images
docker search nginx
docker search wireshark
docker search monitoring
```

**Example: Network Monitoring Image**
```dockerfile
# Example Dockerfile for a network monitoring tool
FROM ubuntu:20.04
RUN apt-get update && apt-get install -y \
    net-tools \
    tcpdump \
    nmap \
    iperf3 \
    curl
COPY monitoring-script.sh /usr/local/bin/
EXPOSE 8080
CMD ["/usr/local/bin/monitoring-script.sh"]
```

**📦 Docker Containers**
A container is a **running instance** of an image - like powering on that network appliance.

```bash
# Create and run a container from an image
docker run -d --name web-server nginx:latest

# View running containers
docker ps

# View all containers (running and stopped)
docker ps -a
```

**Key Differences:**
| Images | Containers |
|--------|------------|
| Static templates | Running instances |
| Read-only | Read-write layer on top |
| Can be shared | Instance-specific |
| Stored in registry | Exist on local host |

---

### **2.3 Container Lifecycle Management**

**🔄 Container States:**
```
Created → Running → Paused → Stopped → Removed
```

**Essential Container Commands:**
```bash
# Start a container
docker start container-name

# Stop a container gracefully
docker stop container-name

# Force stop a container
docker kill container-name

# Restart a container
docker restart container-name

# Remove a container
docker rm container-name

# Remove all stopped containers
docker container prune
```

**Network Service Example:**
```bash
# Run an nginx web server
docker run -d \
  --name web-server \
  -p 8080:80 \
  nginx:latest

# Check if the service is accessible
curl http://localhost:8080

# View container logs
docker logs web-server

# Execute commands inside the running container
docker exec -it web-server bash
```

---

### **2.4 Volume Management and Data Persistence**

For network engineers, data persistence is crucial for configuration files, logs, and monitoring data.

**📁 Volume Types:**

**1. Named Volumes (Recommended for production)**
```bash
# Create a named volume
docker volume create network-configs

# Use the volume in a container
docker run -d \
  --name router-config \
  -v network-configs:/etc/configs \
  ubuntu:latest

# List volumes
docker volume ls

# Inspect volume details
docker volume inspect network-configs
```

**2. Bind Mounts (Great for development)**
```bash
# Mount host directory into container
docker run -d \
  --name network-monitor \
  -v /host/configs:/container/configs \
  -v /host/logs:/var/log \
  monitoring-tool:latest
```

**3. tmpfs Mounts (Temporary data)**
```bash
# Mount temporary filesystem
docker run -d \
  --name temp-cache \
  --tmpfs /tmp:rw,noexec,nosuid,size=100m \
  caching-service:latest
```

**📊 Network Configuration Management Example:**
```bash
# Create persistent storage for network configurations
docker volume create router-configs
docker volume create switch-configs

# Run configuration management container
docker run -d \
  --name config-manager \
  -v router-configs:/configs/routers \
  -v switch-configs:/configs/switches \
  -p 8080:8080 \
  network-config-manager:latest
```

---

### **2.5 Image Management Best Practices**

**🏷️ Image Tagging Strategy:**
```bash
# Tag images with version numbers
docker tag nginx:latest myregistry.com/nginx:v1.0
docker tag nginx:latest myregistry.com/nginx:production

# Always specify tags in production
docker run myregistry.com/nginx:v1.0  # Good
docker run nginx                      # Bad (uses latest)
```

**🧹 Image Cleanup:**
```bash
# Remove unused images
docker image prune

# Remove all unused images (not just dangling)
docker image prune -a

# Remove specific image
docker rmi image-name:tag
```

**📦 Registry Operations:**
```bash
# Push image to registry
docker push myregistry.com/network-tool:v1.0

# Pull image from registry
docker pull myregistry.com/network-tool:v1.0

# Login to private registry
docker login myregistry.com
```

---

### **2.6 Networking-Specific Image Examples**

**Popular Network Engineering Images:**
```bash
# Network troubleshooting Swiss Army knife
docker pull nicolaka/netshoot

# Wireshark (requires X11 forwarding)
docker pull ffeldhaus/wireshark

# iperf3 for bandwidth testing
docker pull networkstatic/iperf3

# NGINX for web services
docker pull nginx:alpine

# OpenVPN server
docker pull kylemanna/openvpn
```

**Testing Network Tools:**
```bash
# Network troubleshooting
docker run -it --rm --net=host nicolaka/netshoot

# Inside the container, you can use:
# ping, traceroute, nslookup, dig, nmap, tcpdump, etc.
```

---

### **💡 Best Practices for Network Engineers**

**1. Always Use Specific Tags**
```bash
# Instead of this:
docker run nginx

# Use this:
docker run nginx:1.21-alpine
```

**2. Minimize Image Size**
```bash
# Use Alpine-based images when possible
docker pull nginx:alpine        # ~22MB
docker pull nginx:latest        # ~133MB
```

**3. Use Multi-stage Builds**
```dockerfile
# Build stage
FROM node:16 AS builder
COPY package*.json ./
RUN npm install
COPY . .
RUN npm run build

# Production stage
FROM nginx:alpine
COPY --from=builder /app/dist /usr/share/nginx/html
```

**4. Manage Secrets Securely**
```bash
# Use Docker secrets instead of environment variables
echo "admin_password" | docker secret create db_password -
```

---

### **🛠️ Chapter 2 Hands-On Exercise**

**Exercise 2.1: Container Lifecycle Management**

**Scenario:** Deploy a network monitoring solution with persistent configuration storage.

**Task 1: Image and Container Management**
```bash
# 1. Pull required images
docker pull nginx:alpine
docker pull nicolaka/netshoot

# 2. Create a named volume for configurations
docker volume create monitoring-configs

# 3. Run nginx with persistent configuration
docker run -d \
  --name web-monitor \
  -p 8080:80 \
  -v monitoring-configs:/etc/nginx/conf.d \
  nginx:alpine

# 4. Test the service
curl http://localhost:8080
```

**Task 2: Configuration Management**
```bash
# 1. Create a custom nginx configuration
docker exec -it web-monitor sh -c "echo 'server {
    listen 80;
    location /status {
        return 200 \"Network Monitor Active\";
        add_header Content-Type text/plain;
    }
}' > /etc/nginx/conf.d/monitoring.conf"

# 2. Reload nginx configuration
docker exec web-monitor nginx -s reload

# 3. Test the new endpoint
curl http://localhost:8080/status
```

**Task 3: Network Troubleshooting**
```bash
# 1. Run network troubleshooting container
docker run -it --rm --name netshoot \
  --net container:web-monitor \
  nicolaka/netshoot

# Inside the netshoot container:
# - Check listening ports: netstat -tlnp
# - Test internal connectivity: curl localhost:80
# - Check DNS resolution: nslookup google.com
```

**Exercise 2.2: Volume Management Scenarios**

**Scenario:** Set up persistent logging for network devices.

```bash
# 1. Create volumes for different log types
docker volume create router-logs
docker volume create switch-logs
docker volume create firewall-logs

# 2. Create a log aggregation container
docker run -d \
  --name log-aggregator \
  -v router-logs:/logs/routers \
  -v switch-logs:/logs/switches \
  -v firewall-logs:/logs/firewalls \
  -v /host/backup:/backup \
  busybox:latest \
  tail -f /dev/null

# 3. Simulate log generation
docker exec log-aggregator sh -c "echo 'Router-01: Interface GigE0/1 UP' >> /logs/routers/router-01.log"
docker exec log-aggregator sh -c "echo 'Switch-01: VLAN 100 created' >> /logs/switches/switch-01.log"

# 4. Verify persistent storage
docker exec log-aggregator find /logs -name "*.log" -exec head -1 {} \;
```

**Expected Outcomes:**
1. Understanding of Docker's fundamental concepts
2. Practical experience with container lifecycle management
3. Knowledge of volume management for persistent data
4. Ability to deploy and manage network services in containers

**Common Pitfalls to Avoid:**
- Using `latest` tag in production environments
- Not backing up volume data
- Running containers with excessive privileges
- Ignoring resource limits and constraints

---

## **Chapter 3: Docker Networking Concepts**

---

### **3.1 Docker Networking Architecture**

Understanding Docker's networking architecture is fundamental for network engineers who want to effectively design and troubleshoot containerized network solutions.

**🏗️ Docker Networking Stack Overview**

```
┌─────────────────────────────────────────────────────────────┐
│                    Applications                              │
├─────────────────────────────────────────────────────────────┤
│                 Container Layer                              │
├─────────────────────────────────────────────────────────────┤
│            Docker Network Drivers                           │
├─────────────────────────────────────────────────────────────┤
│               Linux Networking                              │
│        (iptables, namespaces, bridges)                     │
├─────────────────────────────────────────────────────────────┤
│              Physical Network                               │
└─────────────────────────────────────────────────────────────┘
```

**Core Networking Components:**
- **Network Drivers**: Implement different networking behaviors
- **Network Namespaces**: Provide isolation between containers
- **Virtual Ethernet Pairs (veth)**: Connect containers to networks
- **Linux Bridge**: Default switching mechanism
- **iptables**: Firewall and NAT rules

---

### **3.2 Network Namespaces and Isolation**

Network namespaces are the foundation of Docker's networking isolation. Each container gets its own network namespace with:

**🔒 Isolated Network Stack:**
- Network interfaces
- Routing tables
- Firewall rules (iptables)
- Network statistics

**Examining Network Namespaces:**
```bash
# List network namespaces on the host
sudo ip netns list

# For each running container, Docker creates a namespace
docker run -d --name test-container nginx:alpine

# Find the container's process ID
docker inspect test-container | grep '"Pid":'

# Or use this one-liner
PID=$(docker inspect -f '{{.State.Pid}}' test-container)

# Access the container's network namespace
sudo nsenter -t $PID -n ip addr show
sudo nsenter -t $PID -n ip route show
```

**Network Namespace Example:**
```bash
# Create a custom network namespace
sudo ip netns add network-lab

# List available namespaces
sudo ip netns list

# Execute commands in the namespace
sudo ip netns exec network-lab ip addr show

# Clean up
sudo ip netns delete network-lab
```

---

### **3.3 Container-to-Container Communication**

Docker provides several mechanisms for containers to communicate with each other.

**🔗 Communication Methods:**

**1. Same Network Communication**
```bash
# Create a custom network
docker network create app-network

# Run containers on the same network
docker run -d --name web-server --network app-network nginx:alpine
docker run -d --name app-server --network app-network python:alpine tail -f /dev/null

# Test connectivity using container names (automatic DNS resolution)
docker exec app-server ping web-server
docker exec app-server wget -qO- http://web-server/
```

**2. Service Discovery via DNS**
```bash
# Docker provides automatic DNS resolution for container names
docker exec app-server nslookup web-server

# Output shows internal IP resolution
# Name:   web-server
# Address: 172.18.0.2
```

**3. Port Publishing for External Access**
```bash
# Publish container port to host
docker run -d --name public-web -p 8080:80 nginx:alpine

# Access from host or external networks
curl http://localhost:8080
curl http://$(hostname -I | awk '{print $1}'):8080
```

**Network Communication Example:**
```bash
# Create a multi-tier application network
docker network create --driver bridge production-net

# Database tier
docker run -d \
  --name database \
  --network production-net \
  -e MYSQL_ROOT_PASSWORD=secret \
  mysql:8.0

# Application tier
docker run -d \
  --name app-backend \
  --network production-net \
  python:alpine \
  sh -c "while true; do echo 'App running'; sleep 30; done"

# Web tier (publicly accessible)
docker run -d \
  --name web-frontend \
  --network production-net \
  -p 80:80 \
  nginx:alpine

# Test inter-container communication
docker exec app-backend ping database
docker exec web-frontend ping app-backend
```

---

### **3.4 Host Networking Fundamentals**

Understanding how Docker integrates with the host's networking stack is crucial for network engineers.

**🖥️ Host Network Integration:**

**Bridge Mode (Default):**
```bash
# Inspect the default bridge network
docker network inspect bridge

# Show bridge interface on host
ip addr show docker0
brctl show docker0  # If bridge-utils installed

# View iptables rules created by Docker
sudo iptables -t nat -L -n
sudo iptables -L DOCKER -n
```

**Host Mode:**
```bash
# Container uses host's network stack directly
docker run -d --name host-nginx --network host nginx:alpine

# Container binds directly to host's port 80
ss -tlnp | grep :80
```

**None Mode:**
```bash
# Container with no network access
docker run -it --name isolated --network none alpine:latest

# Inside container - no network interfaces except loopback
ip addr show
```

**📊 Network Interface Analysis:**
```bash
# Compare network interfaces
echo "=== Host Network Interfaces ==="
ip addr show

echo "=== Container Network Interfaces ==="
docker exec nginx-container ip addr show

echo "=== Bridge Details ==="
docker network inspect bridge | jq '.[0].IPAM.Config'
```

---

### **3.5 Virtual Ethernet Pairs (veth)**

Docker uses virtual ethernet pairs to connect containers to networks.

**🔌 veth Pair Concepts:**
- One end inside container (usually named `eth0`)
- Other end connected to Docker bridge on host
- Provides layer 2 connectivity

**Examining veth Pairs:**
```bash
# Run a container and find its veth pair
docker run -d --name veth-demo nginx:alpine

# Get container's network interface index
docker exec veth-demo cat /sys/class/net/eth0/iflink

# Find corresponding host interface
ip addr show | grep -A1 "^[interface_index]:"

# Alternative method using container PID
PID=$(docker inspect -f '{{.State.Pid}}' veth-demo)
sudo nsenter -t $PID -n ip link show eth0
```

**veth Pair Traffic Analysis:**
```bash
# Monitor traffic on the host side of veth pair
VETH_HOST=$(docker exec veth-demo cat /sys/class/net/eth0/iflink)
VETH_NAME=$(ip link show | grep "^$VETH_HOST:" | cut -d: -f2 | awk '{print $1}')

# Capture traffic on the veth interface
sudo tcpdump -i $VETH_NAME -n icmp

# Generate traffic from another container
docker run --rm alpine:latest ping -c 3 $(docker inspect -f '{{range .NetworkSettings.Networks}}{{.IPAddress}}{{end}}' veth-demo)
```

---

### **3.6 Network Driver Deep Dive**

Docker supports multiple network drivers, each serving different use cases.

**🚗 Available Network Drivers:**

**Bridge Driver (Default):**
```bash
# Create custom bridge network
docker network create \
  --driver bridge \
  --subnet 172.20.0.0/16 \
  --ip-range 172.20.240.0/20 \
  --gateway 172.20.0.1 \
  custom-bridge

# Inspect the created network
docker network inspect custom-bridge
```

**Host Driver:**
```bash
# Direct host network access
docker run --rm --network host nicolaka/netshoot netstat -tlnp
```

**None Driver:**
```bash
# Completely isolated container
docker run --rm --network none nicolaka/netshoot ip addr show
```

**Custom Network Configuration:**
```bash
# Create network with specific DNS settings
docker network create \
  --driver bridge \
  --subnet 10.10.0.0/24 \
  --gateway 10.10.0.1 \
  --dns 8.8.8.8 \
  --dns 1.1.1.1 \
  lab-network

# Use the custom network
docker run --rm --network lab-network nicolaka/netshoot nslookup google.com
```

---

### **💡 Advanced Networking Concepts**

**Traffic Flow Analysis:**
```bash
# Create containers for traffic flow demonstration
docker network create flow-demo
docker run -d --name client --network flow-demo alpine:latest tail -f /dev/null
docker run -d --name server --network flow-demo nginx:alpine

# Trace packet flow
echo "=== Container to Container ==="
docker exec client traceroute server

echo "=== Container to External ==="
docker exec client traceroute 8.8.8.8

echo "=== Host Bridge Configuration ==="
docker network inspect flow-demo | jq '.[0].IPAM'
```

**iptables Rules Analysis:**
```bash
# Examine Docker's iptables rules
echo "=== NAT Table ==="
sudo iptables -t nat -L -n --line-numbers

echo "=== Filter Table - DOCKER Chain ==="
sudo iptables -L DOCKER -n --line-numbers

echo "=== Port Forwarding Rules ==="
sudo iptables -t nat -L DOCKER -n --line-numbers
```

---

### **🛠️ Chapter 3 Hands-On Exercise**

**Exercise 3.1: Network Namespace Exploration**

**Scenario:** Understand how Docker creates network isolation for containers.

**Task 1: Namespace Investigation**
```bash
# 1. Create a test container
docker run -d --name namespace-test nginx:alpine

# 2. Find the container's PID
PID=$(docker inspect -f '{{.State.Pid}}' namespace-test)
echo "Container PID: $PID"

# 3. Compare network interfaces
echo "=== Host Interfaces ==="
ip addr show | grep -E '^[0-9]+:|inet '

echo "=== Container Interfaces ==="
sudo nsenter -t $PID -n ip addr show

# 4. Compare routing tables
echo "=== Host Routing ==="
ip route show

echo "=== Container Routing ==="
sudo nsenter -t $PID -n ip route show
```

**Task 2: veth Pair Analysis**
```bash
# 1. Find veth pair information
IFLINK=$(docker exec namespace-test cat /sys/class/net/eth0/iflink)
echo "Container interface link: $IFLINK"

# 2. Find host side of veth pair
HOST_VETH=$(ip link show | grep "^$IFLINK:" | cut -d: -f2 | awk '{print $1}')
echo "Host veth interface: $HOST_VETH"

# 3. Monitor traffic on veth pair
sudo tcpdump -i $HOST_VETH -c 5 &

# 4. Generate traffic
docker exec namespace-test ping -c 3 8.8.8.8
```

**Exercise 3.2: Multi-Container Network Setup**

**Scenario:** Create a three-tier application with proper network segmentation.

```bash
# 1. Create networks for different tiers
docker network create frontend-net --subnet 172.21.0.0/24
docker network create backend-net --subnet 172.22.0.0/24
docker network create database-net --subnet 172.23.0.0/24

# 2. Deploy database tier
docker run -d \
  --name postgres-db \
  --network database-net \
  -e POSTGRES_PASSWORD=secret \
  postgres:13-alpine

# 3. Deploy application tier (connected to both backend and database networks)
docker run -d \
  --name app-server \
  --network backend-net \
  python:3.9-alpine \
  sh -c "while true; do echo 'App running'; sleep 30; done"

# Connect app-server to database network
docker network connect database-net app-server

# 4. Deploy web tier
docker run -d \
  --name web-server \
  --network frontend-net \
  -p 8080:80 \
  nginx:alpine

# Connect web-server to backend network
docker network connect backend-net web-server

# 5. Test connectivity between tiers
echo "=== Testing Database Connectivity ==="
docker exec app-server ping postgres-db

echo "=== Testing App Connectivity ==="
docker exec web-server ping app-server

echo "=== Network Isolation Test (should fail) ==="
docker exec web-server ping postgres-db || echo "Direct database access blocked ✓"
```

**Exercise 3.3: Network Traffic Analysis**

**Scenario:** Monitor and analyze container network traffic.

```bash
# 1. Set up monitoring
docker run -d --name traffic-gen nginx:alpine
docker run --rm --net container:traffic-gen nicolaka/netshoot &

# 2. Generate different types of traffic
# HTTP requests
docker exec traffic-gen wget -qO- http://httpbin.org/get

# DNS queries
docker exec traffic-gen nslookup github.com

# ICMP traffic
docker exec traffic-gen ping -c 3 google.com

# 3. Analyze network statistics
echo "=== Container Network Statistics ==="
docker exec traffic-gen cat /proc/net/dev

echo "=== Host Network Statistics ==="
cat /proc/net/dev | grep docker0
```

**Expected Outcomes:**
1. Deep understanding of Docker's networking architecture
2. Practical experience with network namespaces and isolation
3. Knowledge of container-to-container communication mechanisms
4. Ability to analyze and troubleshoot Docker network connectivity
5. Understanding of how Docker integrates with host networking

**Troubleshooting Tips:**
- Use `docker network ls` to list all networks
- Use `docker network inspect <network>` for detailed network information
- Use `docker exec <container> ip addr show` to check container interfaces
- Use `docker logs <container>` to check for network-related errors
- Remember that container names provide automatic DNS resolution within the same network

---
