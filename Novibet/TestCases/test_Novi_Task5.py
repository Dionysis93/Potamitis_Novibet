import time
import pandas as pd
from BusinessObjects.NoviBusinessObject_Task3 import LiveFootballBusiness
from BusinessObjects.NoviBusinessObject_Task5 import Event


def test_event_monitor(BaseClass):

    try:
        event_page = LiveFootballBusiness()
        event_logic = Event()


        start_time = time.time()

        while True:
            if event_logic.monitor_events(event_page, start_time):
                break
            time.sleep(5)

        data = event_logic.get_data()

        df = pd.DataFrame(data)
        print(df)

        event_logic.generate_xml_report('events_report.xml')
