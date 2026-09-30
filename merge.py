import requests

ICS_URLS = [
    "https://um6p.instructure.com/feeds/calendars/user_amVBPLnSsM6jiffhQXSvac71HG05BdOEkpVMOYuu.ics",
    "https://um6p.instructure.com/feeds/calendars/user_OdWc5SEkRb8Xb0qnEDC9YcOUi2SAS8rstjTZTM6v.ics",
    "https://um6p.instructure.com/feeds/calendars/user_50Lk68NhlhAPk3qgQoMyWkPmiqeSOBiERtuYks3S.ics",
    "LINK4",
    "LINK5",
    "LINK6",
    "LINK7",
    "LINK8",
    "LINK9",
    "LINK10"
]

events = []

for url in ICS_URLS:
    try:
        data = requests.get(url, timeout=30).text
        inside = False
        current = []

        for line in data.splitlines():
            if line.startswith("BEGIN:VEVENT"):
                inside = True
                current = [line]
            elif line.startswith("END:VEVENT"):
                current.append(line)
                events.append("\n".join(current))
                inside = False
            elif inside:
                current.append(line)

    except Exception as e:
        print(f"Error loading {url}: {e}")

with open("merged.ics", "w", encoding="utf-8") as f:
    f.write("BEGIN:VCALENDAR\n")
    f.write("VERSION:2.0\n")
    f.write("PRODID:-//Bureau Calendar//EN\n")

    for event in events:
        f.write(event + "\n")

    f.write("END:VCALENDAR\n")
