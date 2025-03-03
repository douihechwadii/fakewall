import json
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

    # Randomize other fields
    src_port = random.randint(1024, 65535)
    dst_port = 80 if service == "HTTP" else 443
    sent_bytes = random.randint(100, 10000)
    received_bytes = random.randint(100, 10000)
    duration = random.randint(1, 10)

    # Start building the log entry with mandatory fields
    log_entry = (
        f"date={timestamp.strftime('%Y-%m-%d')} "
        f"time={timestamp.strftime('%H:%M:%S')} "
        f"logid=\"0000000013\" "
        f"type=\"traffic\" subtype=\"forward\" level=\"notice\" vd=\"vdom1\" "
        f"eventtime={int(timestamp.timestamp())} "
        f"srcip={src_ip} dstip={dst_ip} "
        f"srcport={src_port} dstport={dst_port} "
        f"srcintf=\"internal\" dstintf=\"external\" "
        f"proto=6 action=\"{action}\" service=\"{service}\" "
        f"sentbyte={sent_bytes} rcvdbyte={received_bytes} "
        f"duration={duration} "
        f"policyid=1 policymode=\"normal\" "
        f"srccountry=\"Reserved\" dstcountry=\"United States\""
    )

    # Dynamically add optional attributes if they exist in the scenario file
    optional_fields = [
        ("poluuid", "poluuid"),
        ("sessionid", "sessionid"),
        ("policytype", "policytype"),
        ("trandisp", "trandisp"),
        ("transip", "transip"),
        ("transport", "transport"),
        ("appid", "appid"),
        ("app", "app"),
        ("appcat", "appcat"),
        ("apprisk", "apprisk"),
        ("utmaction", "utmaction"),
        ("countapp", "countapp"),
        ("devtype", "devtype"),
        ("osname", "osname"),
        ("mastersrcmac", "mastersrcmac"),
        ("srcmac", "srcmac"),
        ("srcserver", "srcserver"),
        ("utmref", "utmref"),
        ("srcname", "srcname"),
        ("dstname", "dstname"),
        ("srcintfrole", "srcintfrole"),
        ("dstintfrole", "dstintfrole"),
        ("sentpkt", "sentpkt"),
        ("rcvdpkt", "rcvdpkt")
    ]

    for field_name, key in optional_fields:
        if key in scenario:  # Check if the key exists in the scenario file
            value = scenario[key]
            if isinstance(value, list):  # Handle lists (e.g., multiple values)
                value = random.choice(value)
            log_entry += f" {field_name}=\"{value}\""

    return log_entry
    
    
def generate_logs(scenario, output_file):
    """Generate log entries for the given scenario and write them to a file."""
    start_time = datetime.now()
    end_time = start_time + timedelta(seconds=scenario['duration_seconds'])
    interval = scenario['interval_seconds']
    
    with open(output_file, 'w') as file:
        current_time = start_time
        while current_time <= end_time:
            log_entry = generate_log_entry(scenario, current_time)
            file.write(log_entry + "\n")
            current_time += timedelta(seconds=interval)

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