# **Scenario Design Guidelines for Log Entry Generation**

This README provides guidelines for designing scenarios and generating log entries that mimic real-world traffic patterns in FortiGate firewalls. It covers attributes that must change or remain constant based on the scenario type, source/destination details, and other factors.

---

## **1. General Considerations**

### **1.1 Duration of the Scenario**
- Define the total duration of the scenario (e.g., 60 seconds, 5 minutes).
- Ensure the timestamp (`date`, `time`, `eventtime`) progresses incrementally throughout the logs to reflect the duration.

### **1.2 Log Type**
- Specify the type of log (`traffic`, `utm`, `event`, etc.) based on the scenario.
- For example:
  - Use `traffic` for network traffic logs.
  - Use `utm` for logs involving UTM features like antivirus, web filtering, or IPS.

### **1.3 Virtual Domain (vd)**
- If using multiple virtual domains, specify the relevant `vd` for each log entry.
- Example: `vd="vdom1"`.

---

## **2. Source and Destination Attributes**

### **2.1 Source IP Address (`srcip`)**
- **Internal Source**: Use private IP ranges (e.g., `10.x.x.x`, `172.16.x.x–172.31.x.x`, `192.168.x.x`).
- **External Source**: Use public IP addresses.
- **srccountry**: 
  - Internal: `"Reserved"` or `"Private"`.
  - External: Real country name (e.g., `"United States"`, `"Germany"`).

### **2.2 Destination IP Address (`dstip`)**
- **Internal Destination**: Use private IP ranges.
- **External Destination**: Use public IP addresses.
- **dstcountry**:
  - Internal: `"Reserved"` or `"Private"`.
  - External: Real country name.

### **2.3 Source Interface (`srcintf`)**
- **Internal Source**: Use internal interfaces (e.g., `internal`, `lan`).
- **External Source**: Use external interfaces (e.g., `wan1`, `wan2`).

### **2.4 Destination Interface (`dstintf`)**
- **Internal Destination**: Use internal interfaces.
- **External Destination**: Use external interfaces.

### **2.5 Source Port (`srcport`)**
- Randomize high-numbered ports (e.g., `1024–65535`) for realistic traffic.

### **2.6 Destination Port (`dstport`)**
- Use well-known ports for standard services:
  - HTTP: `80`
  - HTTPS: `443`
  - SSH: `22`
  - FTP: `21`

---

## **3. NAT-Related Attributes**

### **3.1 Translation Disposition (`trandisp`)**
- **SNAT**: Use `trandisp="snat"` for outbound traffic from internal sources.
- **DNAT**: Use `trandisp="dnat"` for inbound traffic to internal destinations.

### **3.2 Translated IP Address (`transip`)**
- **SNAT**: Set `transip` to the public IP address of the firewall's external interface.
- **DNAT**: Set `transip` to the private IP address of the internal destination.

### **3.3 Translated Port (`transport`)**
- Randomize the translated port if applicable.

---

## **4. Application Inspection Attributes**

### **4.1 Application ID (`appid`)**
- Include `appid` only if application inspection is enabled.
- Randomize `appid` values based on the service being used.

### **4.2 Application Name (`app`)**
- Use specific application names (e.g., `HTTP.BROWSER`, `HTTPS.BROWSER`, `FTP.CLIENT`).

### **4.3 Application Category (`appcat`)**
- Categorize applications (e.g., `Web.Client`, `File.Transfer`).

### **4.4 Application Risk (`apprisk`)**
- Assign risk levels (`low`, `medium`, `high`) based on the application.

---

## **5. Traffic Statistics**

### **5.1 Bytes Sent/Received (`sentbyte`, `rcvdbyte`)**
- Randomize byte counts for realistic traffic patterns.
- Example: `sentbyte=100–10000`, `rcvdbyte=100–50000`.

### **5.2 Packets Sent/Received (`sentpkt`, `rcvdpkt`)**
- Randomize packet counts based on the session duration and service type.
- Example: `sentpkt=10–100`, `rcvdpkt=10–200`.

### **5.3 Session Duration (`duration`)**
- Randomize session durations (e.g., `1–60` seconds).

---

## **6. Policy and Session Attributes**

### **6.1 Policy ID (`policyid`)**
- Use consistent `policyid` values for all log entries within the same policy.

### **6.2 Policy Mode (`policymode`)**
- Use modes such as `normal`, `learn`, or `transparent` based on the policy configuration.

### **6.3 Session ID (`sessionid`)**
- Randomize `sessionid` values for each unique session.

---

## **7. Unified Threat Management (UTM) Attributes**

### **7.1 UTM Action (`utmaction`)**
- Include `utmaction` only if UTM features are involved.
- Example actions: `allow`, `block`, `scan`.

### **7.2 Device Type (`devtype`)**
- Specify the type of device (e.g., `Linux PC`, `Windows Server`).

### **7.3 Operating System (`osname`)**
- Specify the operating system (e.g., `Linux`, `Windows 10`).

---

## **8. Attributes That Must Change**

### **8.1 Timestamps**
- Increment `date`, `time`, and `eventtime` for each log entry to reflect the scenario duration.

### **8.2 Source/Destination Details**
- Change `srcip`, `dstip`, `srcport`, `dstport`, and related fields based on the traffic direction and service.

### **8.3 Traffic Statistics**
- Randomize `sentbyte`, `rcvdbyte`, `sentpkt`, `rcvdpkt`, and `duration` for each log entry.

---

## **9. Attributes That Must Not Change**

### **9.1 Policy Configuration**
- Keep `policyid`, `policymode`, and `vd` consistent throughout the scenario.

### **9.2 Service Type**
- Maintain the same `service` (e.g., `HTTP`, `HTTPS`) for all log entries within the same session.

### **9.3 GeoIP Information**
- Keep `srccountry` and `dstcountry` consistent unless the source/destination changes.

---

## **10. Scenario-Specific Considerations**

### **10.1 DDoS Attack**
- Generate a large number of log entries with varying `srcip` but the same `dstip`.
- Use high byte counts and short durations to simulate high traffic volume.

### **10.2 Malware Download**
- Include UTM-related fields (`utmaction`, `url`) to indicate blocked or allowed downloads.
- Use specific `app` and `appcat` values (e.g., `Malware.Download`).

### **10.3 Brute Force Attack**
- Generate repeated login attempts with different `srcip` and `dstport`.
- Use `utmaction="block"` for failed attempts.

---

## **11. Example Scenarios**

### **11.1 Outbound Traffic**
- **Source**: Internal (`srcip=192.168.1.10`, `srcintf=internal`).
- **Destination**: External (`dstip=203.0.113.45`, `dstintf=wan1`).
- **Attributes**: Include `trandisp=snat`, `transip=public_ip`.

### **11.2 Inbound Traffic**
- **Source**: External (`srcip=203.0.113.45`, `srcintf=wan1`).
- **Destination**: Internal (`dstip=192.168.1.10`, `dstintf=internal`).
- **Attributes**: Include `trandisp=dnat`, `transip=private_ip`.

---

By following these guidelines, you can create realistic and consistent scenarios for generating log entries that closely resemble those produced by a FortiGate firewall. Adjust the attributes as needed to fit the specific requirements of each scenario.