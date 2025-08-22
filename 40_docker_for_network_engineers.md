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

## **Chapter 5: Networking Modes - Bridge, Host, None, and Custom Networks**

---

### **5.1 Understanding Docker Network Drivers**

Docker provides several network drivers that implement different networking behaviors. Each driver serves specific use cases and understanding when to use each is crucial for network engineers.

**🔌 Network Driver Types:**
- **Bridge**: Default mode, provides isolated network
- **Host**: Uses host's networking directly
- **None**: Completely disables networking
- **Overlay**: Multi-host networking (Docker Swarm)
- **Macvlan**: Direct physical network access
- **Custom**: Third-party network plugins

**Viewing Available Drivers:**
```bash
# List all network drivers
docker info | grep -A10 "Network:"

# List current networks
docker network ls

# Inspect network driver details
docker network inspect bridge
docker network inspect host
```

---

### **5.2 Bridge Network Mode (Default)**

Bridge networking is Docker's default mode and most commonly used for single-host container communication.

**🌉 Bridge Network Characteristics:**
- Provides network isolation from host
- Automatic DNS resolution between containers
- NAT-based internet access
- Port publishing for external access

**Default Bridge Network:**
```bash
# Inspect default bridge
docker network inspect bridge

# View bridge interface on host
ip addr show docker0

# Check bridge configuration
brctl show docker0  # If bridge-utils installed
```

**Container Communication on Default Bridge:**
```bash
# Start containers on default bridge
docker run -d --name web1 nginx:alpine
docker run -d --name web2 nginx:alpine

# Check container IPs
docker inspect web1 | grep IPAddress
docker inspect web2 | grep IPAddress

# Note: Container name resolution doesn't work on default bridge
docker exec web1 ping web2  # This will fail

# But IP-based communication works
WEB2_IP=$(docker inspect -f '{{range .NetworkSettings.Networks}}{{.IPAddress}}{{end}}' web2)
docker exec web1 ping $WEB2_IP
```

**Custom Bridge Networks:**
```bash
# Create custom bridge network
docker network create \
  --driver bridge \
  --subnet 172.25.0.0/24 \
  --gateway 172.25.0.1 \
  --ip-range 172.25.0.0/28 \
  custom-bridge

# Deploy containers with custom IPs
docker run -d \
  --name web-server \
  --network custom-bridge \
  --ip 172.25.0.10 \
  nginx:alpine

docker run -d \
  --name app-server \
  --network custom-bridge \
  --ip 172.25.0.20 \
  python:alpine tail -f /dev/null

# Test name resolution (works on custom networks)
docker exec app-server ping web-server
docker exec app-server nslookup web-server
```

**Advanced Bridge Configuration:**
```bash
# Create bridge with advanced options
docker network create \
  --driver bridge \
  --subnet 192.168.100.0/24 \
  --gateway 192.168.100.1 \
  --ip-range 192.168.100.128/25 \
  --dns 8.8.8.8 \
  --dns 1.1.1.1 \
  --opt com.docker.network.bridge.name=br-custom \
  --opt com.docker.network.bridge.enable_icc=true \
  --opt com.docker.network.bridge.enable_ip_masquerade=true \
  --opt com.docker.network.driver.mtu=1500 \
  production-network

# Inspect the created network
docker network inspect production-network

# Verify bridge creation on host
ip addr show br-custom
```

---

### **5.3 Host Network Mode**

Host networking allows containers to use the host's network stack directly, providing maximum performance but reduced isolation.

**🖥️ Host Network Characteristics:**
- No network isolation
- Direct access to host interfaces
- Maximum network performance
- Port conflicts possible
- No port publishing needed

**Using Host Network:**
```bash
# Run container with host networking
docker run -d \
  --name host-web \
  --network host \
  nginx:alpine

# Container listens directly on host's port 80
ss -tlnp | grep :80

# Check container's network view (same as host)
docker exec host-web ip addr show
docker exec host-web ip route show

# Compare with host
ip addr show
ip route show
```

**Host Network Use Cases:**
```bash
# Network monitoring tools
docker run -it --rm \
  --network host \
  --privileged \
  nicolaka/netshoot \
  tcpdump -i eth0

# High-performance applications
docker run -d \
  --name performance-app \
  --network host \
  --cpus="2" \
  --memory="4g" \
  high-performance-network-app:latest

# Network utilities that need host access
docker run --rm \
  --network host \
  nicolaka/netshoot \
  nmap -sn $(ip route | grep eth0 | grep kernel | cut -d' ' -f1 | head -1)
```

**Host Network Limitations:**
```bash
# Port conflicts demonstration
docker run -d --name web1 --network host nginx:alpine
docker run -d --name web2 --network host nginx:alpine  # This will fail

# Check port usage
docker logs web2  # Shows port binding error

# Cleanup
docker rm -f web1 web2
```

---

### **5.4 None Network Mode**

None networking completely disables networking for containers, useful for batch processing or security-sensitive applications.

**🚫 None Network Characteristics:**
- No network interfaces except loopback
- Complete network isolation
- Ideal for batch processing
- Security through isolation

**Using None Network:**
```bash
# Run container with no networking
docker run -it --rm \
  --network none \
  alpine:latest \
  ip addr show

# Only loopback interface available
# Output: lo (127.0.0.1/8)

# Demonstrate isolation
docker run -it --rm \
  --network none \
  alpine:latest \
  ping 8.8.8.8  # This will fail
```

**None Network Use Cases:**
```bash
# Secure batch processing
docker run --rm \
  --network none \
  -v /host/data:/data \
  data-processor:latest \
  process-sensitive-data.sh

# Isolated computation
docker run --rm \
  --network none \
  -v /host/input:/input:ro \
  -v /host/output:/output \
  compute-engine:latest

# Security scanning (isolated environment)
docker run --rm \
  --network none \
  -v /host/scan-target:/scan:ro \
  security-scanner:latest \
  scan /scan
```

**Adding Network to None Containers:**
```bash
# Start container with no network
docker run -d \
  --name isolated-app \
  --network none \
  busybox:latest \
  tail -f /dev/null

# Add network later
docker network connect bridge isolated-app

# Verify network addition
docker exec isolated-app ip addr show
docker exec isolated-app ping 8.8.8.8
```

---

### **5.5 Custom Networks and Advanced Configuration**

Custom networks provide fine-grained control over container networking and enable complex topologies.

**🔧 Custom Network Creation:**
```bash
# Create multi-tier network architecture
docker network create \
  --driver bridge \
  --subnet 10.0.1.0/24 \
  --gateway 10.0.1.1 \
  frontend-tier

docker network create \
  --driver bridge \
  --subnet 10.0.2.0/24 \
  --gateway 10.0.2.1 \
  backend-tier

docker network create \
  --driver bridge \
  --subnet 10.0.3.0/24 \
  --gateway 10.0.3.1 \
  database-tier

# Deploy application with proper network segmentation
docker run -d \
  --name web-app \
  --network frontend-tier \
  -p 80:80 \
  nginx:alpine

docker run -d \
  --name api-server \
  --network backend-tier \
  python:alpine \
  tail -f /dev/null

docker run -d \
  --name database \
  --network database-tier \
  postgres:13-alpine

# Connect API server to both backend and database tiers
docker network connect frontend-tier api-server
docker network connect database-tier api-server
```

**Network Policies and Security:**
```bash
# Create isolated development network
docker network create \
  --driver bridge \
  --subnet 172.30.0.0/24 \
  --internal \
  dev-isolated

# Internal network (no external access)
docker run -d \
  --name dev-app \
  --network dev-isolated \
  nginx:alpine

# Test isolation (should fail)
docker exec dev-app ping 8.8.8.8 || echo "External access blocked ✓"

# Containers can still communicate internally
docker run -d \
  --name dev-db \
  --network dev-isolated \
  postgres:13-alpine

docker exec dev-app ping dev-db  # This works
```

**Advanced Network Options:**
```bash
# Create network with custom MTU and other options
docker network create \
  --driver bridge \
  --subnet 192.168.200.0/24 \
  --opt com.docker.network.driver.mtu=9000 \
  --opt com.docker.network.bridge.enable_icc=false \
  --opt com.docker.network.bridge.enable_ip_masquerade=false \
  jumbo-frame-network

# Network with specific IPAM driver
docker network create \
  --driver bridge \
  --ipam-driver default \
  --ipam-opt subnet=172.28.0.0/24 \
  --ipam-opt gateway=172.28.0.1 \
  --ipam-opt ip-range=172.28.0.128/25 \
  custom-ipam-network
```

---

### **5.6 Performance Considerations**

Different networking modes have varying performance characteristics that network engineers should understand.

**📊 Performance Comparison:**

**Latency Test Script:**
```bash
# Create performance test script
cat > ~/docker-lab/scripts/network-performance.sh << 'EOF'
#!/bin/bash

echo "=== Docker Network Performance Test ==="

# Test 1: Host network (baseline)
echo "1. Host Network Performance:"
docker run --rm --network host nicolaka/netshoot \
  ping -c 10 8.8.8.8 | grep -E "(min/avg/max|packet loss)"

# Test 2: Bridge network
echo -e "\n2. Bridge Network Performance:"
docker run --rm nicolaka/netshoot \
  ping -c 10 8.8.8.8 | grep -E "(min/avg/max|packet loss)"

# Test 3: Custom bridge network
echo -e "\n3. Custom Bridge Network Performance:"
docker network create perf-test 2>/dev/null || true
docker run --rm --network perf-test nicolaka/netshoot \
  ping -c 10 8.8.8.8 | grep -E "(min/avg/max|packet loss)"

# Cleanup
docker network rm perf-test 2>/dev/null || true

echo "=== Performance Test Complete ==="
EOF

chmod +x ~/docker-lab/scripts/network-performance.sh
~/docker-lab/scripts/network-performance.sh
```

**Throughput Testing:**
```bash
# iperf3 performance testing between containers
# Start iperf3 server
docker run -d \
  --name iperf-server \
  --network host \
  networkstatic/iperf3 -s

# Test bridge network throughput
docker network create perf-test
docker run -d \
  --name iperf-server-bridge \
  --network perf-test \
  networkstatic/iperf3 -s

# Test from bridge network to host network
SERVER_IP=$(docker inspect -f '{{range .NetworkSettings.Networks}}{{.IPAddress}}{{end}}' iperf-server-bridge)
docker run --rm \
  --network perf-test \
  networkstatic/iperf3 -c $SERVER_IP -t 10

# Test host network (for comparison)
docker run --rm \
  --network host \
  networkstatic/iperf3 -c 127.0.0.1 -t 10

# Cleanup
docker rm -f iperf-server iperf-server-bridge
docker network rm perf-test
```

**Resource Usage Analysis:**
```bash
# Monitor network namespace overhead
echo "=== Network Namespace Analysis ==="

# Count network namespaces
NS_COUNT=$(sudo ip netns list | wc -l)
echo "Network namespaces: $NS_COUNT"

# Monitor container network statistics
docker stats --no-stream --format "table {{.Container}}\t{{.NetIO}}\t{{.MemUsage}}"

# Check bridge interface statistics
echo -e "\nBridge interface statistics:"
cat /proc/net/dev | grep -E "(docker0|br-)"
```

---

### **💡 Best Practices for Network Mode Selection**

**When to Use Each Mode:**

**Bridge Mode (Default):**
- ✅ Multi-container applications
- ✅ Development environments
- ✅ Microservices architectures
- ✅ When you need port isolation

**Host Mode:**
- ✅ High-performance applications
- ✅ Network monitoring tools
- ✅ When you need maximum throughput
- ⚠️ Be careful of port conflicts

**None Mode:**
- ✅ Batch processing jobs
- ✅ Security-sensitive applications
- ✅ Computational workloads
- ✅ Isolated environments

**Custom Networks:**
- ✅ Complex multi-tier applications
- ✅ Network segmentation requirements
- ✅ When you need specific IP addressing
- ✅ Production environments

---

### **🛠️ Chapter 5 Hands-On Exercise**

**Exercise 5.1: Network Mode Comparison**

**Scenario:** Deploy the same application using different network modes and compare their characteristics.

**Task 1: Deploy Application with Different Network Modes**
```bash
# 1. Bridge mode deployment
docker run -d \
  --name app-bridge \
  --network bridge \
  -p 8080:80 \
  nginx:alpine

# 2. Host mode deployment
docker run -d \
  --name app-host \
  --network host \
  nginx:alpine

# 3. Custom network deployment
docker network create \
  --subnet 172.26.0.0/24 \
  app-network

docker run -d \
  --name app-custom \
  --network app-network \
  --ip 172.26.0.10 \
  -p 8081:80 \
  nginx:alpine

# 4. Test accessibility
curl -s http://localhost:8080 | grep -o "Welcome to nginx"  # Bridge
curl -s http://localhost:80 | grep -o "Welcome to nginx"    # Host  
curl -s http://localhost:8081 | grep -o "Welcome to nginx"  # Custom
```

**Task 2: Network Isolation Testing**
```bash
# Create isolated network
docker network create \
  --internal \
  isolated-net

# Deploy isolated application
docker run -d \
  --name isolated-app \
  --network isolated-net \
  nginx:alpine

# Test isolation
docker exec isolated-app ping 8.8.8.8 || echo "✓ Internet access blocked"

# Test internal communication
docker run -d \
  --name isolated-client \
  --network isolated-net \
  alpine:latest tail -f /dev/null

docker exec isolated-client ping isolated-app && echo "✓ Internal communication works"
```

**Exercise 5.2: Multi-Tier Network Architecture**

**Scenario:** Design and implement a three-tier web application with proper network segmentation.

```bash
# 1. Create tier-specific networks
docker network create \
  --subnet 172.27.1.0/24 \
  web-tier

docker network create \
  --subnet 172.27.2.0/24 \
  app-tier

docker network create \
  --subnet 172.27.3.0/24 \
  --internal \
  db-tier

# 2. Deploy database tier (most restricted)
docker run -d \
  --name database \
  --network db-tier \
  -e POSTGRES_PASSWORD=secret \
  postgres:13-alpine

# 3. Deploy application tier (connects to web and db)
docker run -d \
  --name app-server \
  --network app-tier \
  python:alpine tail -f /dev/null

docker network connect db-tier app-server

# 4. Deploy web tier (public-facing)
docker run -d \
  --name web-server \
  --network web-tier \
  -p 80:80 \
  nginx:alpine

docker network connect app-tier web-server

# 5. Test connectivity matrix
echo "=== Testing Network Connectivity ==="
echo "Web to App: $(docker exec web-server ping -c 1 app-server >/dev/null 2>&1 && echo "✓" || echo "✗")"
echo "App to DB: $(docker exec app-server ping -c 1 database >/dev/null 2>&1 && echo "✓" || echo "✗")"
echo "Web to DB: $(docker exec web-server ping -c 1 database >/dev/null 2>&1 && echo "✗ (blocked)" || echo "✓ (isolated)")"
echo "DB to Internet: $(docker exec database ping -c 1 8.8.8.8 >/dev/null 2>&1 && echo "✗ (not isolated)" || echo "✓ (blocked)")"
```

**Expected Outcomes:**
1. Understanding of different Docker network modes and their use cases
2. Practical experience with bridge, host, and none networking
3. Knowledge of custom network creation and configuration
4. Ability to design multi-tier network architectures
5. Performance considerations for different networking modes

---

## **Chapter 6: Practical Examples - Network Simulations & Topologies**

---

### **6.1 Creating Virtual Network Topologies**

Docker enables network engineers to create complex virtual topologies for testing, learning, and development without requiring physical hardware.

**🏗️ Topology Design Principles:**
- Use custom networks to simulate different network segments
- Leverage container placement for geographic simulation
- Implement realistic latency and bandwidth constraints
- Create scalable and repeatable topologies

**Basic Three-Tier Architecture:**
```bash
# Create networks representing different network segments
docker network create \
  --subnet 10.0.10.0/24 \
  --gateway 10.0.10.1 \
  dmz-network

docker network create \
  --subnet 192.168.1.0/24 \
  --gateway 192.168.1.1 \
  internal-network

docker network create \
  --subnet 172.16.1.0/24 \
  --gateway 172.16.1.1 \
  --internal \
  database-network

# Deploy DMZ services (public-facing)
docker run -d \
  --name web-server-1 \
  --network dmz-network \
  --ip 10.0.10.10 \
  -p 80:80 \
  nginx:alpine

docker run -d \
  --name web-server-2 \
  --network dmz-network \
  --ip 10.0.10.11 \
  -p 8080:80 \
  nginx:alpine

# Deploy internal application servers
docker run -d \
  --name app-server-1 \
  --network internal-network \
  --ip 192.168.1.10 \
  python:alpine tail -f /dev/null

docker run -d \
  --name app-server-2 \
  --network internal-network \
  --ip 192.168.1.11 \
  python:alpine tail -f /dev/null

# Deploy database servers (most secure)
docker run -d \
  --name database-primary \
  --network database-network \
  --ip 172.16.1.10 \
  -e POSTGRES_PASSWORD=secret \
  postgres:13-alpine

docker run -d \
  --name database-replica \
  --network database-network \
  --ip 172.16.1.11 \
  -e POSTGRES_PASSWORD=secret \
  postgres:13-alpine

# Connect application servers to database network
docker network connect database-network app-server-1
docker network connect database-network app-server-2

# Connect web servers to internal network for app communication
docker network connect internal-network web-server-1
docker network connect internal-network web-server-2
```

**Campus Network Simulation:**
```bash
# Create campus network topology
cat > ~/docker-lab/configs/campus-network.yml << 'EOF'
version: '3.8'

services:
  # Core network services
  core-switch-1:
    image: nicolaka/netshoot
    command: tail -f /dev/null
    networks:
      core-network:
        ipv4_address: 10.0.0.10
      building-a-network:
        ipv4_address: 10.1.0.1
      building-b-network:
        ipv4_address: 10.2.0.1

  core-switch-2:
    image: nicolaka/netshoot
    command: tail -f /dev/null
    networks:
      core-network:
        ipv4_address: 10.0.0.11
      building-a-network:
        ipv4_address: 10.1.0.2
      building-b-network:
        ipv4_address: 10.2.0.2

  # Building A services
  building-a-switch:
    image: nicolaka/netshoot
    command: tail -f /dev/null
    networks:
      building-a-network:
        ipv4_address: 10.1.0.10

  building-a-server:
    image: nginx:alpine
    networks:
      building-a-network:
        ipv4_address: 10.1.0.100

  # Building B services
  building-b-switch:
    image: nicolaka/netshoot
    command: tail -f /dev/null
    networks:
      building-b-network:
        ipv4_address: 10.2.0.10

  building-b-server:
    image: nginx:alpine
    networks:
      building-b-network:
        ipv4_address: 10.2.0.100

  # Management network
  network-monitor:
    image: nicolaka/netshoot
    command: tail -f /dev/null
    networks:
      - core-network
      - building-a-network
      - building-b-network
      - management-network
    privileged: true

networks:
  core-network:
    driver: bridge
    ipam:
      config:
        - subnet: 10.0.0.0/24
          gateway: 10.0.0.1

  building-a-network:
    driver: bridge
    ipam:
      config:
        - subnet: 10.1.0.0/24
          gateway: 10.1.0.1

  building-b-network:
    driver: bridge
    ipam:
      config:
        - subnet: 10.2.0.0/24
          gateway: 10.2.0.1

  management-network:
    driver: bridge
    ipam:
      config:
        - subnet: 192.168.100.0/24
          gateway: 192.168.100.1
EOF

# Deploy campus network
docker-compose -f ~/docker-lab/configs/campus-network.yml up -d
```

---

### **6.2 Multi-Container Network Scenarios**

Real-world network scenarios often involve complex interactions between multiple services. Docker allows us to simulate these scenarios effectively.

**Load Balancer Scenario:**
```bash
# Create load balancer topology
docker network create \
  --subnet 172.20.0.0/24 \
  lb-frontend

docker network create \
  --subnet 172.21.0.0/24 \
  lb-backend

# Deploy backend web servers
for i in {1..3}; do
  docker run -d \
    --name web-backend-$i \
    --network lb-backend \
    --ip 172.21.0.1$i \
    nginx:alpine
  
  # Customize each server's response
  docker exec web-backend-$i sh -c "echo 'Server: web-backend-$i' > /usr/share/nginx/html/index.html"
done

# Deploy load balancer
cat > ~/docker-lab/configs/nginx-lb.conf << 'EOF'
upstream backend {
    server 172.21.0.11:80;
    server 172.21.0.12:80;
    server 172.21.0.13:80;
}

server {
    listen 80;
    location / {
        proxy_pass http://backend;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
    }
}
EOF

docker run -d \
  --name load-balancer \
  --network lb-frontend \
  --network lb-backend \
  -p 8080:80 \
  -v ~/docker-lab/configs/nginx-lb.conf:/etc/nginx/conf.d/default.conf \
  nginx:alpine

# Test load balancing
for i in {1..6}; do
  echo "Request $i: $(curl -s http://localhost:8080)"
done
```

**Service Mesh Simulation:**
```bash
# Create service mesh topology
docker network create mesh-network

# Deploy multiple microservices
services=("user-service" "product-service" "order-service" "payment-service")

for service in "${services[@]}"; do
  docker run -d \
    --name $service \
    --network mesh-network \
    --label service=$service \
    python:alpine \
    sh -c "python -m http.server 8080"
done

# Deploy service mesh proxy (envoy-like behavior simulation)
docker run -d \
  --name service-mesh-proxy \
  --network mesh-network \
  -p 9901:9901 \
  nicolaka/netshoot \
  tail -f /dev/null

# Test service discovery
docker exec service-mesh-proxy nslookup user-service
docker exec service-mesh-proxy nslookup product-service
```

**Database Replication Scenario:**
```bash
# Create database replication topology
docker network create \
  --subnet 172.25.0.0/24 \
  db-replication

# Deploy primary database
docker run -d \
  --name db-primary \
  --network db-replication \
  --ip 172.25.0.10 \
  -e POSTGRES_PASSWORD=secret \
  -e POSTGRES_REPLICATION_USER=replicator \
  -e POSTGRES_REPLICATION_PASSWORD=replicator_pass \
  postgres:13-alpine

# Deploy read replicas
for i in {1..2}; do
  docker run -d \
    --name db-replica-$i \
    --network db-replication \
    --ip 172.25.0.2$i \
    -e POSTGRES_PASSWORD=secret \
    -e POSTGRES_MASTER_SERVICE=db-primary \
    postgres:13-alpine
done

# Deploy connection pooler
docker run -d \
  --name db-pooler \
  --network db-replication \
  --ip 172.25.0.5 \
  -p 5432:5432 \
  pgbouncer/pgbouncer:latest

# Test database connectivity
docker run --rm \
  --network db-replication \
  postgres:13-alpine \
  psql -h db-primary -U postgres -c "SELECT version();"
```

---

### **6.3 Simulating Network Devices and Services**

Docker can simulate various network devices and services, making it an excellent tool for network testing and education.

**Router Simulation:**
```bash
# Create multi-homed router simulation
docker network create \
  --subnet 192.168.1.0/24 \
  --gateway 192.168.1.1 \
  lan-network

docker network create \
  --subnet 192.168.2.0/24 \
  --gateway 192.168.2.1 \
  dmz-network

docker network create \
  --subnet 10.0.0.0/24 \
  --gateway 10.0.0.1 \
  wan-network

# Deploy router container
docker run -d \
  --name virtual-router \
  --network lan-network \
  --ip 192.168.1.1 \
  --privileged \
  --cap-add NET_ADMIN \
  nicolaka/netshoot \
  tail -f /dev/null

# Connect router to multiple networks
docker network connect dmz-network virtual-router --ip 192.168.2.1
docker network connect wan-network virtual-router --ip 10.0.0.1

# Enable IP forwarding in router
docker exec virtual-router sysctl -w net.ipv4.ip_forward=1

# Configure routing
docker exec virtual-router ip route add 192.168.2.0/24 via 192.168.2.1
docker exec virtual-router ip route add 10.0.0.0/24 via 10.0.0.1

# Deploy clients in different networks
docker run -d \
  --name lan-client \
  --network lan-network \
  --ip 192.168.1.10 \
  alpine:latest tail -f /dev/null

docker run -d \
  --name dmz-server \
  --network dmz-network \
  --ip 192.168.2.10 \
  nginx:alpine

# Test routing
docker exec lan-client ping 192.168.2.10  # Should route through virtual router
```

**DNS Server Simulation:**
```bash
# Create DNS infrastructure
docker network create \
  --subnet 172.30.0.0/24 \
  dns-network

# Deploy primary DNS server
cat > ~/docker-lab/configs/named.conf << 'EOF'
zone "example.local" {
    type master;
    file "/etc/bind/db.example.local";
};
EOF

cat > ~/docker-lab/configs/db.example.local << 'EOF'
$TTL    604800
@       IN      SOA     ns1.example.local. admin.example.local. (
                              2         ; Serial
                         604800         ; Refresh
                          86400         ; Retry
                        2419200         ; Expire
                         604800 )       ; Negative Cache TTL
;
@       IN      NS      ns1.example.local.
@       IN      A       172.30.0.10
ns1     IN      A       172.30.0.10
web     IN      A       172.30.0.20
app     IN      A       172.30.0.21
db      IN      A       172.30.0.22
EOF

# Deploy DNS server (simplified with dnsmasq)
docker run -d \
  --name dns-server \
  --network dns-network \
  --ip 172.30.0.10 \
  -p 53:53/udp \
  --cap-add NET_ADMIN \
  andyshinn/dnsmasq:latest \
  --address=/web.example.local/172.30.0.20 \
  --address=/app.example.local/172.30.0.21 \
  --address=/db.example.local/172.30.0.22

# Deploy services with DNS resolution
docker run -d \
  --name web-service \
  --network dns-network \
  --ip 172.30.0.20 \
  --dns 172.30.0.10 \
  nginx:alpine

docker run -d \
  --name app-service \
  --network dns-network \
  --ip 172.30.0.21 \
  --dns 172.30.0.10 \
  python:alpine tail -f /dev/null

# Test DNS resolution
docker exec app-service nslookup web.example.local
docker exec app-service ping web.example.local
```

**Firewall Simulation:**
```bash
# Create network with firewall
docker network create \
  --subnet 172.40.0.0/24 \
  protected-network

docker network create \
  --subnet 172.41.0.0/24 \
  external-network

# Deploy firewall container
docker run -d \
  --name firewall \
  --network protected-network \
  --ip 172.40.0.1 \
  --privileged \
  --cap-add NET_ADMIN \
  nicolaka/netshoot \
  tail -f /dev/null

docker network connect external-network firewall --ip 172.41.0.1

# Configure firewall rules (iptables)
docker exec firewall iptables -F
docker exec firewall iptables -P FORWARD DROP
docker exec firewall iptables -A FORWARD -i eth0 -o eth1 -p tcp --dport 80 -j ACCEPT
docker exec firewall iptables -A FORWARD -i eth1 -o eth0 -m state --state ESTABLISHED,RELATED -j ACCEPT

# Deploy protected server
docker run -d \
  --name protected-server \
  --network protected-network \
  --ip 172.40.0.10 \
  nginx:alpine

# Deploy external client
docker run -d \
  --name external-client \
  --network external-network \
  --ip 172.41.0.10 \
  alpine:latest tail -f /dev/null

# Test firewall rules
docker exec external-client wget -qO- http://172.40.0.10/  # Should work (HTTP allowed)
docker exec external-client ping 172.40.0.10 || echo "Ping blocked by firewall"  # Should fail
```

---

### **6.4 Network Performance Testing**

Docker environments are excellent for conducting repeatable network performance tests.

**Bandwidth Testing:**
```bash
# Create performance testing environment
docker network create \
  --subnet 172.50.0.0/24 \
  perf-network

# Deploy iperf3 servers
docker run -d \
  --name iperf-server-1 \
  --network perf-network \
  --ip 172.50.0.10 \
  networkstatic/iperf3 -s

docker run -d \
  --name iperf-server-2 \
  --network perf-network \
  --ip 172.50.0.11 \
  networkstatic/iperf3 -s

# Performance test script
cat > ~/docker-lab/scripts/performance-test.sh << 'EOF'
#!/bin/bash

echo "=== Network Performance Testing ==="

# Single stream test
echo "1. Single Stream Test:"
docker run --rm \
  --network perf-network \
  networkstatic/iperf3 -c 172.50.0.10 -t 10 -f M

# Parallel streams test
echo -e "\n2. Parallel Streams Test (4 streams):"
docker run --rm \
  --network perf-network \
  networkstatic/iperf3 -c 172.50.0.10 -t 10 -P 4 -f M

# UDP test
echo -e "\n3. UDP Test:"
docker run --rm \
  --network perf-network \
  networkstatic/iperf3 -c 172.50.0.10 -u -b 100M -t 10

# Bidirectional test
echo -e "\n4. Bidirectional Test:"
docker run --rm \
  --network perf-network \
  networkstatic/iperf3 -c 172.50.0.10 -d -t 10 -f M

echo "=== Performance Testing Complete ==="
EOF

chmod +x ~/docker-lab/scripts/performance-test.sh
~/docker-lab/scripts/performance-test.sh
```

**Latency and Jitter Testing:**
```bash
# Create latency testing setup
docker network create latency-test

# Deploy test targets
docker run -d \
  --name target-1 \
  --network latency-test \
  alpine:latest tail -f /dev/null

docker run -d \
  --name target-2 \
  --network latency-test \
  alpine:latest tail -f /dev/null

# Latency test script
cat > ~/docker-lab/scripts/latency-test.sh << 'EOF'
#!/bin/bash

echo "=== Network Latency Testing ==="

# Basic ping test
echo "1. Basic Ping Test:"
docker exec target-1 ping -c 100 target-2 | grep -E "(min/avg/max|packet loss)"

# Flood ping test
echo -e "\n2. Flood Ping Test:"
docker exec target-1 ping -f -c 1000 target-2 | grep -E "(min/avg/max|packet loss)"

# Interval ping test
echo -e "\n3. Interval Ping Test (0.1s intervals):"
docker exec target-1 ping -i 0.1 -c 50 target-2 | grep -E "(min/avg/max|packet loss)"

echo "=== Latency Testing Complete ==="
EOF

chmod +x ~/docker-lab/scripts/latency-test.sh
~/docker-lab/scripts/latency-test.sh
```

---

### **💡 Advanced Topology Scenarios**

**Multi-Cloud Simulation:**
```bash
# Simulate multi-cloud connectivity
docker network create \
  --subnet 10.1.0.0/24 \
  cloud-provider-a

docker network create \
  --subnet 10.2.0.0/24 \
  cloud-provider-b

docker network create \
  --subnet 192.168.100.0/24 \
  vpn-tunnel

# Deploy cloud resources
docker run -d \
  --name cloud-a-web \
  --network cloud-provider-a \
  --ip 10.1.0.10 \
  nginx:alpine

docker run -d \
  --name cloud-b-db \
  --network cloud-provider-b \
  --ip 10.2.0.10 \
  postgres:13-alpine

# Deploy VPN gateways
docker run -d \
  --name vpn-gateway-a \
  --network cloud-provider-a \
  --network vpn-tunnel \
  --ip 10.1.0.1 \
  --privileged \
  nicolaka/netshoot tail -f /dev/null

docker run -d \
  --name vpn-gateway-b \
  --network cloud-provider-b \
  --network vpn-tunnel \
  --ip 10.2.0.1 \
  --privileged \
  nicolaka/netshoot tail -f /dev/null

# Test cross-cloud connectivity through VPN
docker exec cloud-a-web ping 10.2.0.10  # Through VPN tunnel
```

---

### **🛠️ Chapter 6 Hands-On Exercise**

**Exercise 6.1: Enterprise Network Simulation**

**Scenario:** Create a realistic enterprise network topology with multiple VLANs, servers, and security zones.

**Task 1: Design and Deploy Network Topology**
```bash
# 1. Create network segments
docker network create \
  --subnet 10.0.1.0/24 \
  --gateway 10.0.1.1 \
  management-vlan

docker network create \
  --subnet 10.0.10.0/24 \
  --gateway 10.0.10.1 \
  user-vlan

docker network create \
  --subnet 10.0.20.0/24 \
  --gateway 10.0.20.1 \
  server-vlan

docker network create \
  --subnet 192.168.100.0/24 \
  --gateway 192.168.100.1 \
  dmz-vlan

# 2. Deploy core infrastructure
docker run -d \
  --name core-switch \
  --network management-vlan \
  --ip 10.0.1.10 \
  nicolaka/netshoot tail -f /dev/null

# Connect core switch to all VLANs
docker network connect user-vlan core-switch --ip 10.0.10.1
docker network connect server-vlan core-switch --ip 10.0.20.1
docker network connect dmz-vlan core-switch --ip 192.168.100.1

# 3. Deploy servers in appropriate VLANs
docker run -d \
  --name file-server \
  --network server-vlan \
  --ip 10.0.20.10 \
  nginx:alpine

docker run -d \
  --name database-server \
  --network server-vlan \
  --ip 10.0.20.11 \
  postgres:13-alpine

docker run -d \
  --name web-server \
  --network dmz-vlan \
  --ip 192.168.100.10 \
  -p 80:80 \
  nginx:alpine

# 4. Deploy user workstations
docker run -d \
  --name workstation-1 \
  --network user-vlan \
  --ip 10.0.10.10 \
  alpine:latest tail -f /dev/null

docker run -d \
  --name workstation-2 \
  --network user-vlan \
  --ip 10.0.10.11 \
  alpine:latest tail -f /dev/null
```

**Task 2: Implement and Test Network Policies**
```bash
# 1. Test inter-VLAN communication through core switch
echo "=== Testing Inter-VLAN Communication ==="
docker exec workstation-1 ping -c 3 10.0.20.10  # User to Server VLAN
docker exec workstation-1 ping -c 3 192.168.100.10  # User to DMZ

# 2. Test network services
echo "=== Testing Network Services ==="
docker exec workstation-1 curl -s http://192.168.100.10 | grep -o "Welcome to nginx"

# 3. Document network topology
cat > ~/docker-lab/enterprise-topology.txt << 'EOF'
Enterprise Network Topology:
- Management VLAN: 10.0.1.0/24
- User VLAN: 10.0.10.0/24  
- Server VLAN: 10.0.20.0/24
- DMZ VLAN: 192.168.100.0/24

Deployed Services:
- Core Switch: Connected to all VLANs
- File Server: 10.0.20.10
- Database Server: 10.0.20.11
- Web Server: 192.168.100.10 (Public)
- Workstations: 10.0.10.10, 10.0.10.11
EOF
```

**Exercise 6.2: Network Failure Simulation**

**Scenario:** Simulate network failures and test resilience.

```bash
# 1. Create redundant topology
docker network create primary-path
docker network create backup-path

# Deploy redundant services
docker run -d \
  --name primary-server \
  --network primary-path \
  nginx:alpine

docker run -d \
  --name backup-server \
  --network backup-path \
  nginx:alpine

docker run -d \
  --name client \
  --network primary-path \
  --network backup-path \
  alpine:latest tail -f /dev/null

# 2. Test normal operation
docker exec client ping primary-server
docker exec client ping backup-server

# 3. Simulate primary path failure
docker network disconnect primary-path client
echo "Primary path failed - testing backup connectivity:"
docker exec client ping backup-server

# 4. Restore primary path
docker network connect primary-path client
echo "Primary path restored:"
docker exec client ping primary-server
```

**Expected Outcomes:**
1. Ability to design and implement complex network topologies
2. Understanding of VLAN simulation using Docker networks
3. Experience with multi-tier application deployments
4. Knowledge of network performance testing methodologies
5. Skills in simulating network failures and testing resilience

---
