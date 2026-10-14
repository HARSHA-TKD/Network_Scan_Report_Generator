import tempfile
import unittest
from pathlib import Path

from network_report import parse_nmap_xml, create_report


SAMPLE_XML = """<?xml version="1.0"?>
<nmaprun>
  <host>
    <status state="up"/>
    <address addr="127.0.0.1" addrtype="ipv4"/>
    <ports>
      <port protocol="tcp" portid="8000">
        <state state="open"/>
        <service name="http" product="SimpleHTTPServer" version="0.6"/>
      </port>
      <port protocol="tcp" portid="9000">
        <state state="closed"/>
        <service name="unknown"/>
      </port>
    </ports>
  </host>
</nmaprun>
"""


class TestNetworkReport(unittest.TestCase):

    def setUp(self):
        self.temp_dir = tempfile.TemporaryDirectory()
        self.xml_path = Path(self.temp_dir.name) / "sample.xml"
        self.xml_path.write_text(SAMPLE_XML, encoding="utf-8")

    def tearDown(self):
        self.temp_dir.cleanup()

    def test_parse_host_address(self):
        hosts = parse_nmap_xml(self.xml_path)
        self.assertEqual(hosts[0]["ip"], "127.0.0.1")

    def test_parse_host_status(self):
        hosts = parse_nmap_xml(self.xml_path)
        self.assertEqual(hosts[0]["status"], "up")

    def test_parse_open_port(self):
        hosts = parse_nmap_xml(self.xml_path)
        self.assertEqual(hosts[0]["ports"][0]["port"], "8000")
        self.assertEqual(hosts[0]["ports"][0]["state"], "open")

    def test_parse_protocol(self):
        hosts = parse_nmap_xml(self.xml_path)
        self.assertEqual(hosts[0]["ports"][0]["protocol"], "tcp")

    def test_parse_service_name(self):
        hosts = parse_nmap_xml(self.xml_path)
        self.assertEqual(hosts[0]["ports"][0]["service"], "http")

    def test_parse_service_version(self):
        hosts = parse_nmap_xml(self.xml_path)
        self.assertEqual(
            hosts[0]["ports"][0]["version"],
            "SimpleHTTPServer 0.6"
        )

    def test_parse_closed_port(self):
        hosts = parse_nmap_xml(self.xml_path)
        self.assertEqual(hosts[0]["ports"][1]["state"], "closed")

    def test_report_contains_host_and_port(self):
        hosts = parse_nmap_xml(self.xml_path)
        report = create_report(hosts)
        self.assertIn("127.0.0.1", report)
        self.assertIn("8000/tcp", report)

    def test_report_contains_safety_limitations(self):
        hosts = parse_nmap_xml(self.xml_path)
        report = create_report(hosts)
        self.assertIn("does not prove a vulnerability", report)
        self.assertIn("authorized to assess", report)

    def test_missing_port_section(self):
        xml_without_ports = """<nmaprun>
          <host>
            <status state="up"/>
            <address addr="127.0.0.1" addrtype="ipv4"/>
          </host>
        </nmaprun>"""
        self.xml_path.write_text(xml_without_ports, encoding="utf-8")
        hosts = parse_nmap_xml(self.xml_path)
        self.assertEqual(hosts[0]["ports"], [])


if __name__ == "__main__":
    unittest.main()
