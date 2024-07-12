import time
import xml.etree.ElementTree as ET

class Event:
    def __init__(self):
        self.data = []

    def monitor_events(self, page, start_time):
        current_time = time.time()
        elapsed_time = current_time - start_time

        events = page.get_events()

        for event in events:
            event_time = page.get_event_time(event)
            if elapsed_time > 20 * 60:
                event_status = "Dropped"
            else:
                event_status = "On Time"

            event_data = {
                "event_time": event_time,
                "event_status": event_status
            }
            self.data.append(event_data)

        return elapsed_time > 20 * 60

    def get_data(self):
        return self.data

    def generate_xml_report(self, filename='events_report.xml'):
        root = ET.Element("Events")

        for event in self.data:
            if event["event_status"] == "Dropped":
                event_element = ET.SubElement(root, "Event")
                ET.SubElement(event_element, "Time").text = event["event_time"]
                ET.SubElement(event_element, "Status").text = event["event_status"]

        tree = ET.ElementTree(root)
        tree.write(filename, encoding='utf-8', xml_declaration=True)
