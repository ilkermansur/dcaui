{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "authorship_tag": "ABX9TyNeePoeNMsNBADlmO/H1F8o",
      "include_colab_link": true
    },
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3"
    },
    "language_info": {
      "name": "python"
    }
  },
  "cells": [
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "view-in-github",
        "colab_type": "text"
      },
      "source": [
        "<a href=\"https://colab.research.google.com/github/ilkermansur/dcaui/blob/main/dcaui_python.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "# Python Refresher\n",
        "\n",
        "## Data Types\n",
        "\n",
        "- String\n",
        "- Integer\n",
        "- Float\n",
        "- Boolean\n",
        "- List\n",
        "- Dictionary\n",
        "- Set\n",
        "- None"
      ],
      "metadata": {
        "id": "-vKVjxNIrbMR"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "# Examples of string data type and methods with a network engineer perspective\n",
        "\n",
        "# String examples\n",
        "ip_address = \"192.168.1.1\"\n",
        "hostname = \"router1.example.com\"\n",
        "interface_name = \"GigabitEthernet0/1\"\n",
        "mac_address = \"00:1A:2B:3C:4D:5E\"\n",
        "config_line = \"  ip address 192.168.1.1 255.255.255.0\"\n",
        "\n",
        "print(f\"IP Address: {ip_address}\")\n",
        "print(f\"Hostname: {hostname}\")\n",
        "print(f\"Interface Name: {interface_name}\")\n",
        "print(f\"MAC Address: {mac_address}\")\n",
        "print(f\"Configuration Line: {config_line}\")\n",
        "\n",
        "# String methods\n",
        "\n",
        "# .split() - useful for parsing output or configurations\n",
        "output = \"interface GigabitEthernet0/1\\n ip address 192.168.1.1 255.255.255.0\\n no shutdown\"\n",
        "lines = output.split('\\n')\n",
        "print(\"\\nOutput split into lines:\")\n",
        "for line in lines:\n",
        "    print(line)\n",
        "\n",
        "# .strip() - useful for removing leading/trailing whitespace from configuration lines\n",
        "cleaned_config_line = config_line.strip()\n",
        "print(f\"\\nCleaned config line: '{cleaned_config_line}'\")\n",
        "\n",
        "# .startswith() and .endswith() - useful for checking line types in configurations\n",
        "print(f\"\\nDoes config_line start with '  ip address'? {config_line.strip().startswith('ip address')}\")\n",
        "print(f\"Does hostname end with '.com'? {hostname.endswith('.com')}\")\n",
        "\n",
        "# .replace() - useful for modifying configurations or data\n",
        "new_ip_address = ip_address.replace(\"192.168.1.1\", \"192.168.1.10\")\n",
        "print(f\"\\nNew IP Address: {new_ip_address}\")\n",
        "\n",
        "# .upper() and .lower() - useful for standardizing input or comparisons (e.g., MAC addresses)\n",
        "mac_address_upper = mac_address.replace(\":\", \"\").upper()\n",
        "print(f\"\\nMAC Address (uppercase, no colons): {mac_address_upper}\")\n",
        "\n",
        "# .find() or .index() - useful for finding specific substrings (e.g., finding the interface number)\n",
        "interface_number_start = interface_name.find('/') + 1\n",
        "interface_number = interface_name[interface_number_start:]\n",
        "print(f\"Interface Number: {interface_number}\")\n",
        "\n",
        "# .join() - useful for constructing strings (e.g., creating a path or a command)\n",
        "path_elements = [\"home\", \"user\", \"configs\", \"router1.cfg\"]\n",
        "config_path = \"/\".join(path_elements)\n",
        "print(f\"\\nConfig Path: {config_path}\")"
      ],
      "metadata": {
        "id": "Ub0fiAQSrhek"
      },
      "execution_count": null,
      "outputs": []
    }
  ]
}