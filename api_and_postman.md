# API & Postman

# 1. API Usage

---

## 1.1 REST API Fundamentals

### 1.1.1 What is a REST API?

A **REST API** (Representational State Transfer Application Programming Interface) is a way for different software systems to communicate over the internet using standard **HTTP methods**. It’s a common architectural style used to build web services.

### 1.1.2 HTTP Methods

| Method | Purpose | Network Example |
| --- | --- | --- |
| GET | Retrieve data | Get router hostname or interface status |
| POST | Create new resource | Add a new device to inventory system |
| PUT | Update entire resource | Replace access-list configuration |
| PATCH | Update part of resource | Change hostname only |
| DELETE | Remove resource | Delete a VLAN or disable a user |

## 1.2 CURL

`CURL` stands for Client URL. It is a command-line tool used to transfer data to or from a server using supported protocols like:

- HTTP / HTTPS (most common)
- FTP / SFTP
- SCP
- LDAP, SMTP, POP3 etc.
basic structure is:
`curl [options] [URL]`

| Option | Description |
| --- | --- |
| -X | HTTP/HTTPS Methods |
| -d | Data form or Json |
| -H | HTTP Header |
| -u | For basic AUTH (-u usr:passwd) |

We use <https://httpbin.org> for testing API call.

`ilkermansur@Mac devcor % curl https://httpbin.org/get`

or

`ilkermansur@Mac devcor % curl -X GET https://httpbin.org/get`

**PS:** GET is default method.
**Response** is below

```json
{
	"args": {},
	"headers": {
		"Accept": "*/*",
		"Host": "httpbin.org",
		"User-Agent": "curl/8.7.1",
		"X-Amzn-Trace-Id": "Root=1-68357a57-688e72026315aaad390f345b"
	},
	"origin": "95.70.135.4",
	"url": "<https://httpbin.org/get>"
}

```

| **Status Code** | **Meaning** | **Example** |
| --- | --- | --- |
| 200 OK | Success | Device list retrieved |
| 201 Created | Resource successfully added | A new VLAN created |
| 204 No Content | Success without body | Device deleted |
| 400 Bad Request | Invalid syntax | Missing field in request body |
| 401 Unauthorized | No valid auth | Token missing or expired |
| 403 Forbidden | Auth ok but not allowed | Trying to delete a restricted device |
| 404 Not Found | Resource doesn’t exist | Asking for a non-existent VLAN |
| 500 Server Error | API crashed | Controller internal error |
| it works. Let's `POST` some data. It can be possible to sent data various formats like. You should know before sending data. |  |  |

*Methods :* `x-www-form-urlencoded`, `json`, `text/plain`
Let's test them

`x-www-form-urlencoded`

```bash
curl -X POST -d "username=ilker&password=1234" \\
     -H "Content-Type:application/x-www-form-urlencoded" \\
     <https://httpbin.org/post>

```

`json`

```bash
curl -X POST -d "{"username":"ilker", "password":"1234"}" \\
     -H "Content-Type:application/json" \\
     <https://httpbin.org/post>

```

`text/plain`

```bash
curl -X POST -H "Content-Type: text/plain" \\
     -d "Hello curl" <https://httpbin.org/post>

```

## 1.3 Requests Library

The requests library in Python is a high-level HTTP library that allows you to send HTTP/1.1 requests easily. It abstracts the complexity of handling sockets, connections, and raw HTTP requests. It is widely used for interacting with web APIs, scraping web data, and testing web services.

**requests** is not a built-in library, you should install it before use

`pip install requests`

**Request**

```python
import requests, json

response = requests.request('GET','<https://httpbin.org/get>')

print(response.status_code)
print(response.text)
print(response.json())

```

**Response**

```json
200

{
  "args": {},
  "headers": {
    "Accept": "*/*",
    "Accept-Encoding": "gzip, deflate",
    "Host": "httpbin.org",
    "User-Agent": "python-requests/2.32.3",
    "X-Amzn-Trace-Id": "Root=1-6837177a-4e18518e42db533e0d49d73d"
  },
  "origin": "178.244.227.138",
  "url": "<https://httpbin.org/get>"
}

{'args': {}, 'headers': {'Accept': '*/*', 'Accept-Encoding': 'gzip, deflate', 'Host': 'httpbin.org', 'User-Agent': 'python-requests/2.32.3', 'X-Amzn-Trace-Id': 'Root=1-6837177a-4e18518e42db533e0d49d73d'}, 'origin': '178.244.227.138', 'url': '<https://httpbin.org/get>'}

```

### 1.3.1 Post data in Request

```python
import requests, json

# with data
payload = {'username': 'ilker', 'password': '1234'}
response = requests.post('<https://httpbin.org/post>', data=payload)
print(response.json())

# with json
payload = {'username': 'ilker', 'password': '1234'}
response = requests.post('<https://httpbin.org/post>', json=payload)
print(response.json())

#with token
headers = {'Authorization': 'Bearer mytoken123'}
response = requests.get('<https://httpbin.org/headers>', headers=headers)
print(response.json())

```

### 1.3.2 Delete data in Request

```bash

curl -X DELETE "<https://httpbin.org/delete?id=42>"

curl -X DELETE -H "Content-Type: application/json" \\
    -d '{"id": "42"}' <https://httpbin.org/delete>

```

```
every detail should be given in product API reference guide. Without product detail, you cant know that data format, authentication parameters etc

```

### 1.3.3 Error Handling in Request

The try-except block in Python is used to catch and handle exceptions (errors) during program execution.
• Without it, your program would crash when an error occurs.
• With it, you can control what happens when something goes wrong (e.g. log, retry, show user-friendly message).

```python
import requests

try:
	response = requests.post("<https://httpbin.org/status/200>")
	if response.status_code == 200:
		print ('request occured succesfully')
	else:
		print (f'error is occured {response.status_code}')
except requests.exceptions.InvalidURL as inv:
	print (f'Invalid Url: {inv}')
except requests.exceptions.HTTPError as http:
	print (f'HTTP error {http}')
except requests.exceptions.RequestException as re:
	print (re)

```

```
You can use `raise` for manuel exception.

```

```python
import requests

response = requests.post("<https://httpbin.org/status/404>")
if response.status_code != 200:
	raise Exception ('Not ok')
else :
	print ('everything is ok')

```

```
There is an important topic in request is `ssl verification` and `warnning`

```

**Request with out certification info**

```python
import requests

response = requests.get("<https://self-signed.badssl.com/>")
print(response)

```

**Response**

```bash
raise SSLError(e, request=request)

requests.exceptions.SSLError: HTTPSConnectionPool(host='self-signed.badssl.com', port=443): Max retries exceeded with url: / (Caused by SSLError(SSLCertVerificationError(1, '[SSL: CERTIFICATE_VERIFY_FAILED] certificate verify failed: self-signed certificate (_ssl.c:1006)')))

```

with `verify=False` or `verify='/path/to/certificate.crt'` in production second method is recommended.

**Request with warning**

```python
import requests

response = requests.get("<https://self-signed.badssl.com/>", verify=False)
print(response)

```

**Response**

```python
/opt/homebrew/lib/python3.11/site-packages/urllib3/connectionpool.py:1099: InsecureRequestWarning: Unverified HTTPS request is being made to host 'self-signed.badssl.com'. Adding certificate verification is strongly advised. See: <https://urllib3.readthedocs.io/en/latest/advanced-usage.html#tls-warnings>

warnings.warn(

<Response [200]>

```

it works but there is a warning. If you want to suppress this this alert use below code

```python
import requests
from urllib3.exceptions import InsecureRequestWarning

requests.packages.urllib3.disable_warnings(InsecureRequestWarning)
response = requests.get("<https://self-signed.badssl.com/>", verify=False)
print(response)

```

### 1.3.4 Cache Control in Cisco API Communication (Client-Side)

When you interact with Cisco devices or platforms via API (e.g., DNA Center, IOS XE RESTCONF, ACI), it’s important to make sure you’re always getting **fresh, up-to-date data** — not something stored in a local cache or proxy.

```
To prevent your client (Python script, browser, or proxy server) from storing or reusing old API responses.

```

### Common Cache-Control Headers:

| **Header** | **Meaning** |
| --- | --- |
| Cache-Control: no-cache | The client **must revalidate** with the server before using cached data. Cached copies may still exist. |
| Cache-Control: no-store | **Do not store** the response in any cache (browser, proxy, or local). |
| Cache-Control: max-age=0 | Treat the response as **immediately expired**; revalidate with the server every time. |

**Example in Python:**

```python
import requests

headers = {
    "Accept": "application/json",
    "Cache-Control": "no-store"  # Prevent local caching
}

response = requests.get("<https://cisco-api-url.com/api/devices>", headers=headers, verify=False)
print(response.json())

```

### 1.3.5 Rate Limit

**Rate limiting** is a technique used by API providers (like Cisco, GitHub, Webex, etc.) to **control how many requests** a user or app can make **in a given time period**.

**🔒 Purpose:**

- Protect the API server from overload
- Ensure **fair usage** between users
- Prevent **abuse** (e.g., DDoS or overly frequent polling)

**Example Concept**

| **Term** | **Meaning** |
| --- | --- |
| Limit | Maximum number of requests allowed |
| Window | Time period for the limit (e.g., per minute, hour) |
| Remaining | How many requests you have left in the current window |
| Reset time | When your limit will be refreshed and reset |

**You are allowed 100 requests per 60 seconds.**

| **Situation** | **Result** |
| --- | --- |
| You make 10 requests | ✅ 90 remaining |
| You make 100 requests | ✅ Limit reached, 0 remaining |
| You make 1 more request | ❌ Error: 429 Too Many Requests |
| After 60 seconds | ✅ Limit resets, you can send again |

---

**HTTP Headers Used for Rate Limiting**

Many APIs return rate-limit information in the **response headers**.

**Example headers:**

```
X-RateLimit-Limit: 100
X-RateLimit-Remaining: 12
X-RateLimit-Reset: 1717003500

```

| **Header** | **Meaning** |
| --- | --- |
| X-RateLimit-Limit | Total allowed requests |
| X-RateLimit-Remaining | Requests you can still make |
| X-RateLimit-Reset | Time (usually in UNIX timestamp) when limit resets |

**What Happens When You Exceed the Limit?**

You get an HTTP **429 Too Many Requests** error:

```
{
  "error": "Rate limit exceeded",
  "retry_after": 60
}

```

**How to Handle It in Python?**

You can check the response headers and pause if needed:

```python
import requests
import time

response = requests.get("<https://api.example.com/devices>")
if response.status_code == 429:
    retry_after = int(response.headers.get("Retry-After", "60"))
    print(f"Rate limit hit. Retrying in {retry_after} seconds.")
    time.sleep(retry_after)

```

**Examples:**

- **Cisco Webex API**: Limit of 100 API calls per 10 seconds per token
- **Cisco DNA Center**: May also limit bulk or frequent requests
- **Cisco SD-WAN**: Limits vary based on your vManage configuration

You can usually see this in API documentation or test it by checking headers.

## 1.4 Postman Usage

Postman is a **popular API development and testing tool** that allows developers and network engineers to **send, debug, and automate API requests** in an easy-to-use interface. It supports **REST, SOAP, and GraphQL APIs** and provides features for **authentication, scripting, and automation**.

**Step -1** Install `Postman`

<img width="1920" height="632" alt="image" src="https://github.com/user-attachments/assets/18f38e00-b3f1-4779-bbd9-5486fa67dc63" />

**Step - 2** Make request

<img width="1920" height="690" alt="image" src="https://github.com/user-attachments/assets/44d13d2e-2752-4e52-9353-be4eb6052909" />

Download postman from `postman.com`

1. Open Postman and click **New Request**.
2. Select the HTTP method (GET, POST, etc.).
3. Enter the **API URL** (e.g., [http://dummyjson.com](http://dummyjson.com/)).
4. Click **Send** to execute the request.
- *Step - 3 Use Authentication
- Go to the **Authorization** tab and select:
- API Key
- Basic Auth (Username/Password)
- OAuth 2.0 / Bearer Token

<img width="1920" height="615" alt="image" src="https://github.com/user-attachments/assets/56b32a6e-4b79-4ea9-bbd2-69a9ac2d6202" />

---

<img width="1920" height="448" alt="image" src="https://github.com/user-attachments/assets/20da9820-492a-437b-ae3c-c2d017221b0a" />

---

<img width="1920" height="1000" alt="image" src="https://github.com/user-attachments/assets/d910e9e8-6404-4eb1-b12e-5752f991b507" />

Add product

<img width="1920" height="658" alt="image" src="https://github.com/user-attachments/assets/96d0b21b-9df7-48e3-b04a-03ffcf881148" />

**Step - 4 Use Environment**

<img width="1920" height="491" alt="image" src="https://github.com/user-attachments/assets/e992f289-b20e-4f13-aca9-ad53fa8b5406" />

- Define global variables for **API URLs, tokens, or credentials**.
- Example: {{base_url}}/users/1 instead of hardcoding the full URL.

**Step - 5 Create new Environment**

<img width="1920" height="436" alt="image" src="https://github.com/user-attachments/assets/fb0cf434-0bad-41e5-9618-b8c9d5bf2b1d" />

Use this environment in `request`

<img width="1920" height="1102" alt="image" src="https://github.com/user-attachments/assets/efaf27c8-76df-4e2c-8342-aef4e5c871b9" />

### 1.4.1 Collection Usage in Postman

A **collection** in Postman is a **group of related API requests** saved together. It helps you organize, reuse, and share requests easily.

<img width="3298" height="1100" alt="image" src="https://github.com/user-attachments/assets/6af1a5f6-fbbd-48ed-ad7a-6b358e1fffc1" />

## 1.5 Rest-API in Cisco ACI

Cisco ACI use two step method, Your requests must contain `cookie` with token.  For taking token you must authenticate before.

### ACI API Test Scenario

Use Cisco sandbox for testing :

- URL : "[https://sandboxapicdc.cisco.com](https://sandboxapicdc.cisco.com/)"
- username : "admin"
- password : "!v3G@!4@Y"

```python
import requests
import json

# APIC info
apic_url = "<https://10.0.0.1>"  # Replace with your APIC IP address
username = "admin"
password = "your_password"

# Disable SSL warnings for testing (not recommended for production)
requests.packages.urllib3.disable_warnings()

# Login endpoint
login_url = f"{apic_url}/api/aaaLogin.json"

# Login payload
login_payload = {
    "aaaUser": {
        "attributes": {
            "name": username,
            "pwd": password
        }
    }
}

# Send login request
response = requests.post(login_url, json=login_payload, verify=False)

# Check login success
if response.status_code == 200:
    print("Login successful.")
    token = response.json()['imdata'][0]['aaaLogin']['attributes']['token']
    cookies = {'APIC-cookie': token}
else:
    print(f"Login failed with status code {response.status_code}")

```

use this token next request as `cookie`

```python
tenants_url = f"{apic_url}/api/node/class/fvTenant.json"

# Make request with cookie
tenants_response = requests.get(tenants_url, cookies=cookies, verify=False)

# Parse and print tenant names
if tenants_response.status_code == 200:
    data = tenants_response.json()
    for tenant in data['imdata']:
        print(tenant['fvTenant']['attributes']['name'])
else:
    print("Failed to get tenant data.")

```

**Output**

```bash
Login successful.
Myfirm-Tenant
infra
common
mgmt
tayssirtenant
etc.

```
