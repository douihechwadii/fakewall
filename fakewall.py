from datetime import *
import random

# Date and Time
current_date = datetime.now().date()
current_time = datetime.now().time().strftime("%H:%M:%S")

# Type and Subtype
types = ["traffic", "event", "utm"]
random_type = random.choice(types)

traffic_subtypes = ["forward", "http-transaction", "local", "multicast", "sniffer", "ztna"]
random_traffic_subtype = random.choice(traffic_subtypes)

event_subtypes = ["cifs-auth-fail", "connector", "endpoint", "fortiextender", "ha", "rest-api", "router"]
random_event_subtype = random.choice(event_subtypes)

utm_subtypes = ["virus", "webfilter", "ips", "emailfilter", "anomaly", "voip", "dlp", "app-ctrl", "waf",
                 "gtp", "dns", "ssh", "ssl", "file-filter", "icap", "forti-switch", "virtual-patch", "casb"]
random_utm_subtype = random.choice(utm_subtypes)

if random_type == "traffic":
    random_subtype = random_traffic_subtype
elif random_type == "event":
    random_subtype = random_event_subtype
else:
    random_subtype = random_utm_subtype


log_entry = (
    f"date={current_date} "
    f"time={current_time} "
    "logid=\"0000000013\" "
    f"type=\"{random_type}\" "
    f"subtype=\"{random_subtype}\" "
    "level=\"notice\" "
    "vd=\"vdom1\" "
    "eventtime=1510775056 "
    "srcip=10.1.100.155 "
    "srcname=\"pc1\" "
    "srcport=40772 "
    "srcintf=\"port12\" "
    "srcintfrole=\"undefined\" "
    "dstip=35.197.51.42 "
    "dstname=\"fortiguard.com\" "
    "dstport=443 "
    "dstintf=\"port11\" "
    "dstintfrole=\"undefined\" "
    "poluuid=\"707a0d88-c972-51e7-bbc7-4d421660557b\" "
    "sessionid=8058 "
    "proto=6 "
    "action=\"close\" "
    "policyid=1 "
    "policytype=\"policy\" "
    "policymode=\"learn\" "
    "service=\"HTTPS\" "
    "dstcountry=\"United States\" "
    "srccountry=\"Reserved\" "
    "trandisp=\"snat\" "
    "transip=172.16.200.2 "
    "transport=40772 "
    "appid=40568 "
    "app=\"HTTPS.BROWSER\" "
    "appcat=\"Web.Client\" "
    "apprisk=\"medium\" "
    "duration=2 "
    "sentbyte=1850 "
    "rcvdbyte=39898 "
    "sentpkt=25 "
    "rcvdpkt=37 "
    "utmaction=\"allow\" "
    "countapp=1 "
    "devtype=\"Linux PC\" "
    "osname=\"Linux\" "
    "mastersrcmac=\"a2:e9:00:ec:40:01\" "
    "srcmac=\"a2:e9:00:ec:40:01\" "
    "srcserver=0 "
    "utmref=0-220586"
)

print(log_entry)