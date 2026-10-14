🔍 Network Scan Report Generator

"Python" (https://img.shields.io/badge/Python-3.x-blue?logo=python)
"Nmap" (https://img.shields.io/badge/Tool-Nmap-informational)
"Platform" (https://img.shields.io/badge/Platform-Kali%20Linux-purple)
"Status" (https://img.shields.io/badge/Status-Completed-success)

A beginner-friendly cybersecurity project that converts Nmap XML scan results into readable text reports using Python.

📌 Project Overview

Network administrators use port scanning to understand which services are exposed on a host. This project demonstrates an authorized local scanning workflow and automates the process of organizing scan results.

✨ Features

- Parses Nmap XML output.
- Extracts host addresses and status.
- Identifies port states, protocols, and service information.
- Generates a readable text report.
- Saves reports to a specified output path.
- Handles missing input files and malformed XML.
- Includes automated unit tests.

🛠️ Technologies

- Python 3
- Nmap
- XML ElementTree
- argparse
- pathlib
- unittest
- Kali Linux

📁 Project Structure

Network_Scan_Report_Generator/
├── network_report.py
├── test_network_report.py
├── README.md
├── PROJECT_REPORT.md
├── CHECKLIST.md
├── .gitignore
├── reports/
└── tests/

🚀 Getting Started

1. Install the requirements

Use a Python 3 installation and Nmap in your authorized lab environment.

On Kali Linux:

sudo apt update
sudo apt install nmap python3

2. Create a reports folder

mkdir -p reports

3. Scan your own local machine

This example scans the local loopback address:

nmap -sV -p 8000 -oX reports/local_scan.xml 127.0.0.1

For a useful demonstration, start a temporary HTTP server on "127.0.0.1:8000" in another terminal before running the scan:

python3 -m http.server 8000 --bind 127.0.0.1

Stop the temporary server with "Ctrl+C" when finished.

4. Generate the report

python3 network_report.py reports/local_scan.xml --output reports/scan_report.txt

The report will be printed in the terminal and saved to the specified output file.

🧪 Run the Tests

python3 -m unittest -v test_network_report.py

The project includes ten tests covering XML parsing, host and port details, report content, and safety limitations.

📄 Documentation

- "PROJECT_REPORT.md" — project objectives, methodology, findings, and limitations.
- "CHECKLIST.md" — responsible network-scanning checklist.
- ".gitignore" — excludes generated reports and temporary files.

🔐 Security and Ethics

Only scan systems you own or have explicit permission to assess.

- Keep scans within the authorized scope.
- Treat service detection as an estimate.
- Do not interpret an open port as proof of a vulnerability.
- Review and redact sensitive information before publishing scan results.

⚠️ Limitations

This project parses existing Nmap XML output; it does not run Nmap scans automatically. The accuracy of the generated report depends on the supplied XML data.

🎓 Learning Outcomes

- Basic network scanning concepts
- Nmap XML output
- Python XML parsing
- Command-line arguments
- Automated testing
- Cybersecurity documentation and ethical scanning

👨‍💻 Author

Harsha Vardhan V G

CodeOrbit Internship — Project 4
