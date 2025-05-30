import json
import time
import random
from datetime import datetime, timedelta
import argparse # for adding the scenario as an argument to the script

# loading the json settings file
def load_scenario(scenario_file):
    with open(scenario_file, 'r') as file:
        return json.load(file)

def generate_log_entry(scenario, timestamp):
    """Generate a single log entry based on the scenario."""
    src_ip = random.choice(scenario['src_ips'])
    dst_ip = random.choice(scenario['dst_ips'])
    service = random.choice(scenario['services'])
    action = random.choice(scenario['actions'])
    utmaction = random.choice(scenario['utmaction'])

    # Randomize other fields
    src_port = random.randint(1024, 65535)
    dst_port = 80 if service == "HTTP" else 443
    sent_bytes = random.randint(100, 10000)
    received_bytes = random.randint(100, 10000)
    duration = random.randint(1, 10)
    sentpkt = random.randint(1, 30)
    rcvdpkt = random.randint(1, 30)
    sessionid = random.randint(1000, 9999)
    appid = random.randint(10000, 99999)
    transport = random.randint(10000, 99999)
    
    # Source and Destination Country code
    if "srccountry" in scenario and "dstcountry" in scenario:
        srccountry = random.choice(scenario["srccountry"])
        dstcountry = random.choice(scenario["dstcountry"])
    else:
        if "10." in src_ip or "172.16" in src_ip or "172.31" in src_ip or "192.168." in src_ip:
            srccountry = "Reserved"
            dstcountry = "United State"
        else:
            dstcountry = "Reserved"
            srccountry = "Tunisia"
    
    # Type and Subtype code
    if "type" in scenario:
        type = scenario["type"]
    else:
        types = ["traffic", "event", "utm"]
        type = random.choice(types)
        
    
    if "subtype" in scenario:
        subtype = scenario["subtype"]
    else:
        traffic_subtypes = ["forward", "http-transaction", "local", "multicast", "sniffer", "ztna"]
        random_traffic_subtype = random.choice(traffic_subtypes)
        
        event_subtypes = ["cifs-auth-fail", "connector", "endpoint", "fortiextender", "ha", "rest-api", "router"]
        random_event_subtype = random.choice(event_subtypes)
        
        utm_subtypes = ["virus", "webfilter", "ips", "emailfilter", "anomaly", "voip", "dlp", "app-ctrl", "waf",
                 "gtp", "dns", "ssh", "ssl", "file-filter", "icap", "forti-switch", "virtual-patch", "casb"]
        random_utm_subtype = random.choice(utm_subtypes)
        
        if type == "traffic":
            subtype = random_traffic_subtype
        elif type == "event":
            subtype = random_event_subtype
        else:
            subtype = random_utm_subtype
        
    
    # srcintf and dstintf code
    if "srcintf" in scenario and "dstintf" in scenario:
        srcintf = random.choice(scenario["srcintf"])
        dstintf = random.choice(scenario["dstintf"])
    else:
        if srccountry == "Reserved":
            srcintf = "wlan1"
            dstintf = "internal"
        else:
            srcintf = "internal"
            dstintf = "wlan1"
            
    # srcmac and mastersrcmac
    random_mac = ":".join(f"{random.randint(0, 255):02x}" for _ in range(6))    
    
    # Start building the log entry with mandatory fields
    log_entry = (
        f"date={timestamp.strftime('%Y-%m-%d')} "
        f"time={timestamp.strftime('%H:%M:%S')} "
        f"logid=\"0000000013\" "
        f"type=\"{type}\" subtype=\"{subtype}\" level=\"{scenario["level"]}\" vd=\"vdom1\" "
        f"eventtime={int(timestamp.timestamp())} "
        f"srcip={src_ip} dstip={dst_ip} "
        f"srcport={src_port} dstport={dst_port} "
        f"srcintf=\"{srcintf}\" dstintf=\"{dstintf}\" "
        f"srcintfrole=\"undefined\" dstintfrole=\"undefined\""
        f"proto=6 action=\"{action}\" service=\"{service}\" "
        f"sentbyte={sent_bytes} rcvdbyte={received_bytes} "
        f"duration={duration} "
        f"policyid=1 policymode=\"{scenario["policymode"]}\" "
        f"srccountry=\"{srccountry}\" dstcountry=\"{dstcountry}\""
        f"sentpkt=\"{sentpkt}\" rcvdpkt=\"{rcvdpkt}\""
        f"devtype=\"Linux PC\" osname=\"Linux\""
        f"mastersrcmac=\"{random_mac}\" srcmac=\"{random_mac}\""
        f"utmaction=\"{utmaction}\" countapp=\"{scenario["countapp"]}\""
        f"srcserver=0 sessionid=\"{sessionid}\" appid=\"{appid}\""
        f"apprisk=\"{scenario["apprisk"]}\" transport=\"{transport}\""
    )

    # Dynamically add optional attributes if they exist in the scenario file
    optional_fields = [
        ("poluuid", "poluuid"),
        ("policytype", "policytype"),
        ("trandisp", "trandisp"),
        ("transip", "transip"),
        ("app", "app"),
        ("appcat", "appcat"),
        ("utmref", "utmref"),
        ("srcname", "srcname"),
        ("dstname", "dstname"),
    ]

    for field_name, key in optional_fields:
        if key in scenario:  # Check if the key exists in the scenario file
            value = scenario[key]
            if isinstance(value, list):  # Handle lists (e.g., multiple values)
                value = random.choice(value)
            log_entry += f" {field_name}=\"{value}\""

    return log_entry
    
    
def generate_logs(scenario, output_file):
    """Continuously generate log entries for the given scenario and append to a file."""
    interval = scenario['interval_seconds']

    with open(output_file, 'a') as file:
        while True:
            current_time = datetime.now()
            log_entry = generate_log_entry(scenario, current_time)
            file.write(log_entry + "\n")
            file.flush()  # Ensure it's written immediately
            print(f"[LOG] {log_entry}")
            time.sleep(interval)


#! Doesn't need to be changed 
if __name__ == "__main__":
    # command-line argument parsing setup
    parser = argparse.ArgumentParser(description="Generate FortiGate log entries based on a scenario file.")
    parser.add_argument("scenario_file", help="Path to the JSON scenario file")
    parser.add_argument("-o", "--output", default="generated_logs.txt", help="Output file name (default: generated_logs.txt)")

    # Parse the arguments
    args = parser.parse_args()
    
    # Load the scenario file
    scenario = load_scenario(args.scenario_file)
    
    # Generate logs and save specified output file
    output_file = args.output
    generate_logs(scenario, output_file)
    
    print(f"Logs generated successfully and saved to {output_file}")