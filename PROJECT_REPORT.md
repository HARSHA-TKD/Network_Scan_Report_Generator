Project Report: Network Scan Report Generator

1. Introduction

Network scanning helps administrators identify hosts, open ports, and visible services. This project uses Nmap for authorized scanning and Python to convert Nmap XML output into a readable text report.

2. Objectives

- Understand basic TCP port states.
- Perform a controlled Nmap scan.
- Export scan results as XML.
- Parse XML using Python.
- Generate a structured text report.
- Validate the program using automated tests.

3. Tools and Technologies

- Kali Linux
- Nmap
- Python 3
- XML ElementTree
- argparse and pathlib
- unittest
- Git and GitHub

4. Methodology

1. Scan an authorized local target.
2. Export the results in Nmap XML format.
3. Parse host, port, state, and service information.
4. Generate a readable report.
5. Run automated tests using sample XML data.

5. Test Environment and Findings

Target: 127.0.0.1 (local loopback address)
Test service: Temporary Python HTTP server
Port: 8000/TCP

During the controlled demonstration, Nmap identified port 8000 as open and detected an HTTP service. This was consistent with the temporary server running on the local machine.

The temporary test server was stopped after the demonstration.

6. Testing

Ten automated tests were reported as passing. They cover:

- Host address and status parsing
- Open and closed port parsing
- Protocol parsing
- Service name and version parsing
- Report content
- Safety limitations
- Hosts without a port section

7. Limitations

- Service identification may be incomplete or inaccurate.
- A port state alone does not establish a vulnerability.
- Results depend on network conditions and scan scope.
- This program parses XML; it does not perform scans itself.
- The program does not verify scanning authorization.

8. Ethical Considerations

Only scan systems you own or have explicit permission to assess. Do not publish reports containing private IP addresses, hostnames, service versions, or other sensitive network details.

9. Conclusion

This project demonstrates a basic defensive-security workflow combining Nmap, XML parsing, report generation, and automated testing.

10. Author

Harsha Vardhan V G

CodeOrbit Internship — Project 4

Submission date: To be added
