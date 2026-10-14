Authorized Network Scanning Checklist

Before Scanning

- [ ] Confirm permission and scope.
- [ ] Confirm the target belongs to the approved lab.
- [ ] Choose only the necessary ports and scan options.
- [ ] Avoid scanning unrelated systems.

During Scanning

- [ ] Record the target and scan date.
- [ ] Record the Nmap command used.
- [ ] Save results in XML format.
- [ ] Note open, closed, and filtered port states.
- [ ] Treat service-version detection as an estimate.

After Scanning

- [ ] Parse the XML output.
- [ ] Check the generated report for accuracy.
- [ ] Avoid claiming unverified vulnerabilities.
- [ ] Redact sensitive information before publishing.
- [ ] Stop temporary lab services.
- [ ] Keep the report within the authorized scope.

Understanding Port States

- Open: A service is accepting connections on the port.
- Closed: The host is reachable, but no service is listening on that port.
- Filtered: Filtering or lack of response prevents Nmap from determining the state clearly.

A scan result alone does not prove that a system is vulnerable.
