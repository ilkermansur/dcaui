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

## **Chapter 4: Hands-On - Setting Up Docker in a Lab Environment**

---

### **4.1 Installation Procedures for Different Platforms**

Setting up Docker properly is crucial for network engineers who need reliable, consistent environments across different systems.

**🐧 Linux Installation (Ubuntu/Debian)**

**Method 1: Official Docker Repository (Recommended)**
```bash
# Remove any existing Docker installations
sudo apt-get remove docker docker-engine docker.io containerd runc

# Update package index
sudo apt-get update

# Install packages to allow apt to use HTTPS
sudo apt-get install \
    ca-certificates \
    curl \
    gnupg \
    lsb-release

# Add Docker's official GPG key
sudo mkdir -p /etc/apt/keyrings
curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo gpg --dearmor -o /etc/apt/keyrings/docker.gpg

# Set up the repository
echo \
  "deb [arch=$(dpkg --print-architecture) signed-by=/etc/apt/keyrings/docker.gpg] https://download.docker.com/linux/ubuntu \
  $(lsb_release -cs) stable" | sudo tee /etc/apt/sources.list.d/docker.list > /dev/null

# Install Docker Engine
sudo apt-get update
sudo apt-get install docker-ce docker-ce-cli containerd.io docker-compose-plugin

# Verify installation
sudo docker run hello-world
```

**Method 2: Convenience Script (For development/testing)**
```bash
# Download and run Docker installation script
curl -fsSL https://get.docker.com -o get-docker.sh
sudo sh get-docker.sh

# Add user to docker group (logout/login required)
sudo usermod -aG docker $USER
```

**🍎 macOS Installation**

**Docker Desktop for Mac:**
```bash
# Download Docker Desktop from docker.com
# Or install via Homebrew
brew install --cask docker

# Verify installation
docker --version
docker-compose --version
```

**⊞ Windows Installation**

**Docker Desktop for Windows:**
```powershell
# Download Docker Desktop from docker.com
# Or install via Chocolatey
choco install docker-desktop

# Enable WSL 2 backend (recommended)
# Verify installation
docker --version
```

**🛠️ Post-Installation Configuration**
```bash
# Configure Docker to start on boot
sudo systemctl enable docker
sudo systemctl start docker

# Configure user permissions (Linux)
sudo usermod -aG docker $USER
newgrp docker

# Verify Docker is working
docker run hello-world
docker info
```

---

### **4.2 Lab Environment Setup and Configuration**

Creating a proper lab environment is essential for network engineers to practice and test Docker networking scenarios.

**🏗️ Lab Architecture Design**

```
┌─────────────────────────────────────────────────────────────┐
│                    Lab Environment                          │
├─────────────────────────────────────────────────────────────┤
│  Management Network (192.168.1.0/24)                      │
│  ┌─────────────┐  ┌─────────────┐  ┌─────────────┐        │
│  │ Docker Host │  │ Docker Host │  │ Docker Host │        │
│  │     #1      │  │     #2      │  │     #3      │        │
│  └─────────────┘  └─────────────┘  └─────────────┘        │
├─────────────────────────────────────────────────────────────┤
│  Container Networks                                         │
│  ┌─────────────────────────────────────────────────────────┐ │
│  │ Frontend (172.20.0.0/24)                               │ │
│  │ Backend  (172.21.0.0/24)                               │ │
│  │ Database (172.22.0.0/24)                               │ │
│  └─────────────────────────────────────────────────────────┘ │
└─────────────────────────────────────────────────────────────┘
```

**Lab Environment Setup Script:**
```bash
#!/bin/bash
# Docker Lab Environment Setup Script

echo "=== Docker Lab Environment Setup ==="

# Create lab directories
mkdir -p ~/docker-lab/{configs,logs,scripts,data}

# Create common networks for lab scenarios
echo "Creating lab networks..."
docker network create --driver bridge --subnet 172.20.0.0/24 lab-frontend
docker network create --driver bridge --subnet 172.21.0.0/24 lab-backend
docker network create --driver bridge --subnet 172.22.0.0/24 lab-database

# Create shared volumes for persistent data
echo "Creating lab volumes..."
docker volume create lab-configs
docker volume create lab-logs
docker volume create lab-data

# Deploy essential lab services
echo "Deploying lab services..."

# Network monitoring dashboard
docker run -d \
  --name lab-monitor \
  --network lab-frontend \
  -p 3000:3000 \
  -v lab-data:/var/lib/grafana \
  grafana/grafana:latest

# Network tools container
docker run -d \
  --name lab-tools \
  --network lab-backend \
  --privileged \
  -v lab-configs:/configs \
  nicolaka/netshoot \
  tail -f /dev/null

# Web server for testing
docker run -d \
  --name lab-web \
  --network lab-frontend \
  -p 8080:80 \
  nginx:alpine

echo "Lab environment setup complete!"
echo "Access points:"
echo "  - Lab Monitor: http://localhost:3000 (admin/admin)"
echo "  - Test Web Server: http://localhost:8080"
echo "  - Network Tools: docker exec -it lab-tools bash"
```

**📝 Lab Configuration Management:**
```bash
# Create configuration templates
cat > ~/docker-lab/configs/docker-compose.lab.yml << 'EOF'
version: '3.8'

services:
  web:
    image: nginx:alpine
    networks:
      - frontend
    ports:
      - "80:80"
    volumes:
      - ./configs/nginx.conf:/etc/nginx/nginx.conf:ro

  app:
    image: python:3.9-alpine
    networks:
      - frontend
      - backend
    command: tail -f /dev/null

  db:
    image: postgres:13-alpine
    networks:
      - backend
    environment:
      POSTGRES_PASSWORD: labpassword
    volumes:
      - lab-data:/var/lib/postgresql/data

networks:
  frontend:
    driver: bridge
    ipam:
      config:
        - subnet: 172.20.0.0/24
  backend:
    driver: bridge
    ipam:
      config:
        - subnet: 172.21.0.0/24

volumes:
  lab-data:
EOF
```

---

### **4.3 Initial Network Configuration and Testing**

Proper initial configuration ensures your Docker lab environment works correctly and provides a solid foundation for networking experiments.

**🔧 Docker Daemon Configuration**

**Configure Docker Daemon (`/etc/docker/daemon.json`):**
```json
{
  "default-address-pools": [
    {
      "base": "172.16.0.0/12",
      "size": 24
    }
  ],
  "dns": ["8.8.8.8", "1.1.1.1"],
  "log-driver": "json-file",
  "log-opts": {
    "max-size": "10m",
    "max-file": "3"
  },
  "storage-driver": "overlay2",
  "experimental": true
}
```

**Apply Configuration:**
```bash
# Restart Docker daemon to apply changes
sudo systemctl restart docker

# Verify configuration
docker info | grep -A5 "Default Address Pools"
```

**🧪 Network Connectivity Testing**

**Basic Connectivity Tests:**
```bash
# Test 1: Internet connectivity from containers
docker run --rm alpine:latest ping -c 3 8.8.8.8

# Test 2: DNS resolution
docker run --rm alpine:latest nslookup google.com

# Test 3: Container-to-container communication
docker network create test-net
docker run -d --name test1 --network test-net alpine:latest tail -f /dev/null
docker run -d --name test2 --network test-net alpine:latest tail -f /dev/null
docker exec test1 ping -c 3 test2

# Cleanup
docker rm -f test1 test2
docker network rm test-net
```

**Advanced Network Testing:**
```bash
# Create comprehensive test script
cat > ~/docker-lab/scripts/network-test.sh << 'EOF'
#!/bin/bash

echo "=== Docker Network Connectivity Test Suite ==="

# Test 1: Bridge network functionality
echo "Test 1: Bridge Network"
docker network create --driver bridge test-bridge
docker run -d --name bridge-test --network test-bridge alpine:latest tail -f /dev/null
RESULT=$(docker exec bridge-test ping -c 1 8.8.8.8 > /dev/null 2>&1 && echo "PASS" || echo "FAIL")
echo "  Bridge connectivity: $RESULT"
docker rm -f bridge-test
docker network rm test-bridge

# Test 2: Host network functionality
echo "Test 2: Host Network"
HOST_RESULT=$(docker run --rm --network host alpine:latest ping -c 1 8.8.8.8 > /dev/null 2>&1 && echo "PASS" || echo "FAIL")
echo "  Host connectivity: $HOST_RESULT"

# Test 3: Custom network with DNS
echo "Test 3: Custom Network DNS"
docker network create --driver bridge dns-test
docker run -d --name dns1 --network dns-test alpine:latest tail -f /dev/null
docker run -d --name dns2 --network dns-test alpine:latest tail -f /dev/null
DNS_RESULT=$(docker exec dns1 ping -c 1 dns2 > /dev/null 2>&1 && echo "PASS" || echo "FAIL")
echo "  DNS resolution: $DNS_RESULT"
docker rm -f dns1 dns2
docker network rm dns-test

# Test 4: Port publishing
echo "Test 4: Port Publishing"
docker run -d --name port-test -p 8888:80 nginx:alpine
sleep 2
PORT_RESULT=$(curl -s http://localhost:8888 > /dev/null 2>&1 && echo "PASS" || echo "FAIL")
echo "  Port publishing: $PORT_RESULT"
docker rm -f port-test

echo "=== Test Suite Complete ==="
EOF

chmod +x ~/docker-lab/scripts/network-test.sh
~/docker-lab/scripts/network-test.sh
```

---

### **4.4 Troubleshooting Common Installation Issues**

Network engineers often encounter specific issues when setting up Docker. Here are common problems and solutions.

**🚨 Common Installation Issues**

**Issue 1: Permission Denied**
```bash
# Problem: Got permission denied while trying to connect to Docker daemon
# Symptoms:
docker run hello-world
# Output: Got permission denied while trying to connect to the Docker daemon socket

# Solution:
sudo usermod -aG docker $USER
newgrp docker
# Or logout and login again

# Verify fix:
docker run hello-world
```

**Issue 2: Docker Daemon Not Running**
```bash
# Problem: Cannot connect to Docker daemon
# Symptoms:
docker ps
# Output: Cannot connect to the Docker daemon at unix:///var/run/docker.sock

# Solution:
sudo systemctl start docker
sudo systemctl enable docker  # Start on boot

# Verify fix:
sudo systemctl status docker
docker info
```

**Issue 3: Network Conflicts**
```bash
# Problem: Address already in use or network conflicts
# Symptoms:
docker run -p 80:80 nginx
# Output: Error starting userland proxy: listen tcp 0.0.0.0:80: bind: address already in use

# Solution 1: Find conflicting process
sudo netstat -tlnp | grep :80
sudo lsof -i :80

# Solution 2: Use different port
docker run -p 8080:80 nginx

# Solution 3: Stop conflicting service
sudo systemctl stop apache2  # or nginx, etc.
```

**Issue 4: Docker Bridge Network Issues**
```bash
# Problem: Containers cannot access internet
# Symptoms: Container can start but no internet connectivity

# Diagnosis:
docker run --rm alpine:latest ping -c 3 8.8.8.8
# Times out or fails

# Solution 1: Check Docker bridge
ip addr show docker0
sudo systemctl restart docker

# Solution 2: Check iptables
sudo iptables -t nat -L
sudo systemctl restart docker

# Solution 3: Configure DNS
echo '{"dns": ["8.8.8.8", "1.1.1.1"]}' | sudo tee /etc/docker/daemon.json
sudo systemctl restart docker
```

---

### **🛠️ Chapter 4 Hands-On Exercise**

**Exercise 4.1: Complete Lab Environment Setup**

**Scenario:** Set up a complete Docker lab environment for network engineering practice.

**Task 1: Installation Verification**
```bash
# 1. Verify Docker installation
docker --version
docker info | grep -E "(Server Version|Storage Driver|Network)"

# 2. Test basic functionality
docker run hello-world

# 3. Check user permissions
docker ps  # Should work without sudo
```

**Task 2: Lab Infrastructure Deployment**
```bash
# 1. Create lab directory structure
mkdir -p ~/docker-lab/{configs,logs,scripts,data,backups}

# 2. Deploy multi-tier lab environment
cat > ~/docker-lab/lab-environment.yml << 'EOF'
version: '3.8'

services:
  # Web tier
  web-server:
    image: nginx:alpine
    networks:
      - frontend
    ports:
      - "8080:80"
    restart: unless-stopped

  # Application tier
  app-server:
    image: python:3.9-alpine
    networks:
      - frontend
      - backend
    command: tail -f /dev/null
    restart: unless-stopped

  # Database tier
  database:
    image: postgres:13-alpine
    networks:
      - backend
    environment:
      POSTGRES_DB: labdb
      POSTGRES_USER: labuser
      POSTGRES_PASSWORD: labpass123
    volumes:
      - db-data:/var/lib/postgresql/data
    restart: unless-stopped

  # Network monitoring
  monitor:
    image: nicolaka/netshoot
    networks:
      - frontend
      - backend
      - monitoring
    command: tail -f /dev/null
    privileged: true
    restart: unless-stopped

networks:
  frontend:
    driver: bridge
    ipam:
      config:
        - subnet: 172.20.0.0/24
          gateway: 172.20.0.1
  backend:
    driver: bridge
    ipam:
      config:
        - subnet: 172.21.0.0/24
          gateway: 172.21.0.1
  monitoring:
    driver: bridge
    ipam:
      config:
        - subnet: 172.22.0.0/24
          gateway: 172.22.0.1

volumes:
  db-data:
EOF

# 3. Deploy the lab environment
cd ~/docker-lab
docker-compose -f lab-environment.yml up -d

# 4. Verify deployment
docker-compose -f lab-environment.yml ps
```

**Task 3: Network Connectivity Testing**
```bash
# 1. Test inter-container communication
echo "=== Testing Frontend to Backend ==="
docker exec docker-lab_app-server_1 ping -c 3 docker-lab_database_1

echo "=== Testing Network Isolation ==="
# This should fail (no direct frontend to backend database access)
docker exec docker-lab_web-server_1 ping -c 3 docker-lab_database_1 || echo "✓ Network isolation working"

# 2. Test external connectivity
echo "=== Testing External Connectivity ==="
docker exec docker-lab_app-server_1 curl -s http://httpbin.org/ip

# 3. Test DNS resolution
echo "=== Testing DNS Resolution ==="
docker exec docker-lab_monitor_1 nslookup docker-lab_web-server_1
docker exec docker-lab_monitor_1 nslookup google.com
```

**Expected Outcomes:**
1. Functional Docker installation across different platforms
2. Complete lab environment ready for network engineering experiments
3. Ability to diagnose and resolve common installation issues
4. Established performance baselines
5. Working knowledge of Docker networking troubleshooting

---
