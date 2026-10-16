🛡️ Network Scan Report Generator

Turn Nmap scan results into clear, structured network security reports.

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.x-3776AB?style=for-the-badge&logo=python&logoColor=white" alt="Python">
  <img src="https://img.shields.io/badge/Nmap-XML%20Parser-2E8B57?style=for-the-badge" alt="Nmap XML Parser">
  <img src="https://img.shields.io/badge/Testing-Unittest-success?style=for-the-badge" alt="Python unittest">
  <img src="https://img.shields.io/badge/Platform-Kali%20Linux%20%7C%20Windows-557C94?style=for-the-badge" alt="Platforms">
</p>---

📌 Overview

Network Scan Report Generator is a beginner-friendly cybersecurity project that converts Nmap XML scan output into a readable, structured text report using Python.

Nmap helps identify visible hosts, ports, and services. This project focuses on the next step: organizing those scan observations into a report that is easier to review and document.

The tool parses existing XML output—it does not perform network scans itself.

✨ Features

- 🔍 Nmap XML Parsing — Extracts host addresses, host status, port numbers, protocols, port states, and service details.
- 📄 Automatic Report Generation — Produces a structured, readable text report.
- 🧠 Service Information — Includes detected service names and version details when available.
- ⚠️ Basic Security Recommendations — Provides a reminder to review and restrict access to detected open services.
- 💾 Save Reports to Files — Supports specifying an output path from the command line.
- 🧪 Automated Unit Tests — Tests parsing and report-generation behavior using Python's built-in "unittest" framework.
- 🛡️ Responsible Scanning — Includes limitations and reminders about authorized security testing.

⚙️ How It Works

Authorized Test Environment
          │
          ▼
     Run Nmap Scan
          │
          ▼
    Export XML Output
          │
          ▼
     network_report.py
          │
          ▼
     Parse XML Data
          │
          ▼
   Generate Text Report
          │
          ▼
 Review Findings & Limitations

🧰 Tech Stack

Technology| Purpose
Python 3| Main programming language
Nmap| Produces network scan results
"xml.etree.ElementTree"| Parses Nmap XML
"argparse"| Handles command-line arguments
"pathlib"| Handles file paths
"unittest"| Runs automated tests
Kali Linux / Windows| Development and testing environments

📁 Project Structure

Network_Scan_Report_Generator/
│
├── network_report.py
├── test_network_report.py
├── README.md
├── PROJECT_REPORT.md
├── CHECKLIST.md
├── .gitignore
│
└── reports/
    └── (generated scan files are kept out of Git)

🚀 Getting Started

1. Prerequisites

Install or have available:

- Python 3
- Nmap
- Git (optional, for version control)

Nmap is needed to generate scan XML. The Python report generator can be run separately using an existing compatible XML file.

2. Clone the Repository

git clone https://github.com/HARSHA-TKD/Network_Scan_Report_Generator.git
cd Network_Scan_Report_Generator

3. Generate XML from an Authorized Local Scan

For a local demonstration, start a temporary HTTP server in one terminal:

python -m http.server 8000 --bind 127.0.0.1

In a second terminal, run:

nmap -sV -p 8000 -oX reports/local_scan.xml 127.0.0.1

Ensure the "reports" directory exists first:

mkdir reports

Important: Start the server before scanning. Stop it afterward with "Ctrl+C". Only scan systems you own or have explicit permission to assess.

4. Generate the Report

python network_report.py reports/local_scan.xml --output reports/scan_report.txt

The program prints the report to the terminal and saves it to the specified output file.

5. Run the Tests

python -m unittest -v test_network_report.py

The test suite covers XML parsing, host and port details, service information, report content, and handling of missing port records.

🧪 Testing

The project includes automated tests for:

- Host address parsing
- Host status parsing
- Open-port parsing
- Protocol parsing
- Service-name parsing
- Service-version parsing
- Closed-port parsing
- Generated report content
- Safety and limitation notes
- Hosts without a port section

The test suite was run successfully during development. Run the command above in your own environment to verify the current version.

📊 Understanding the Results

Port state| General meaning
"open"| A service is accepting connections on the scanned port.
"closed"| The host is reachable, but no service is listening on that port.
"filtered"| Filtering or lack of response prevents a clear determination.

An open port is not automatically a vulnerability. Service-version detection can be incomplete or inaccurate, so findings require context and further authorized review.

🔐 Security & Responsible Use

- Scan only systems you own or have explicit authorization to assess.
- Keep scan scope within the approved environment.
- Review findings before making security conclusions.
- Do not publish private host addresses, sensitive service details, or raw scan output without permission.
- Generated XML and text reports are excluded through ".gitignore" to reduce the risk of exposing environment-specific information.

🎯 Learning Outcomes

Through this project, I practiced:

- Basic network-scanning concepts
- Nmap XML output
- XML parsing in Python
- Command-line argument handling
- Text report generation
- Automated testing with "unittest"
- Git and GitHub project workflows
- Responsible cybersecurity documentation

🔮 Future Improvements

- Export reports to HTML or PDF
- Add severity categories based on transparent, documented rules
- Support JSON output
- Improve error handling and input validation
- Add configurable report templates
- Compare scan results over time

👨‍💻 Author

HARSHA VARDHAN V G

Computer Science Engineering — Cybersecurity

CodeOrbit Internship · Project 4

⚠️ Disclaimer

This project is intended for educational use and authorized defensive-security activities only. It does not independently verify vulnerabilities or replace a professional security assessment.

---

<p align="center">
  <i>Learn the network. Understand the evidence. Document responsibly.</i>
</p>