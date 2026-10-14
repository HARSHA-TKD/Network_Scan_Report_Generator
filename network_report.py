import argparse
import xml.etree.ElementTree as ET
from pathlib import Path


def parse_nmap_xml(xml_file):
    """Read an Nmap XML file and return host and port details."""
    tree = ET.parse(xml_file)
    root = tree.getroot()

    results = []

    for host in root.findall("host"):
        status = host.find("status")
        if status is None:
            continue

        host_status = status.get("state", "unknown")

        address = host.find("address")
        host_ip = address.get("addr", "unknown") if address is not None else "unknown"

        host_data = {
            "ip": host_ip,
            "status": host_status,
            "ports": []
        }

        ports_element = host.find("ports")

        if ports_element is not None:
            for port in ports_element.findall("port"):
                state_element = port.find("state")
                service_element = port.find("service")

                state = (
                    state_element.get("state", "unknown")
                    if state_element is not None else "unknown"
                )

                service_name = (
                    service_element.get("name", "unknown")
                    if service_element is not None else "unknown"
                )

                service_version = ""
                if service_element is not None:
                    product = service_element.get("product", "")
                    version = service_element.get("version", "")
                    service_version = f"{product} {version}".strip()

                host_data["ports"].append({
                    "port": port.get("portid", "unknown"),
                    "protocol": port.get("protocol", "unknown"),
                    "state": state,
                    "service": service_name,
                    "version": service_version
                })

        results.append(host_data)

    return results


def create_report(hosts):
    """Create a readable text report from parsed scan results."""
    lines = [
        "NETWORK SCAN REPORT",
        "=" * 60,
        "Source: Nmap XML output",
        "Note: Findings describe scan observations, not confirmed vulnerabilities.",
        ""
    ]

    if not hosts:
        lines.append("No host records were found in the XML file.")

    for host in hosts:
        lines.append(f"Host: {host['ip']}")
        lines.append(f"Status: {host['status']}")

        if not host["ports"]:
            lines.append("No port records were included in the XML output.")

        for port in host["ports"]:
            lines.append(
                f"  {port['port']}/{port['protocol']} - "
                f"{port['state']} - {port['service']}"
            )

            if port["version"]:
                lines.append(f"    Detected details: {port['version']}")

            if port["state"] == "open":
                lines.append(
                    "    Recommendation: Confirm that this service is needed "
                    "and restrict access appropriately."
                )

        lines.append("")

    lines.extend([
        "LIMITATIONS",
        "-" * 60,
        "Service identification may be incomplete or inaccurate.",
        "A scan result alone does not prove a vulnerability.",
        "Only scan systems you own or are authorized to assess."
    ])

    return "\n".join(lines)


def main():
    parser = argparse.ArgumentParser(
        description="Generate a readable report from Nmap XML output."
    )
    parser.add_argument(
        "xml_file",
        help="Path to an Nmap XML file, for example reports/local_scan.xml"
    )
    parser.add_argument(
        "-o", "--output",
        help="Optional path for saving the text report"
    )
    args = parser.parse_args()

    xml_path = Path(args.xml_file)

    if not xml_path.is_file():
        parser.error(f"Input file not found: {xml_path}")

    try:
        hosts = parse_nmap_xml(xml_path)
    except ET.ParseError as error:
        parser.error(f"Invalid XML file: {error}")

    report = create_report(hosts)
    print(report)

    if args.output:
        output_path = Path(args.output)
        output_path.parent.mkdir(parents=True, exist_ok=True)
        output_path.write_text(report + "\n", encoding="utf-8")
        print(f"\nReport saved to: {output_path}")


if __name__ == "__main__":
    main()
