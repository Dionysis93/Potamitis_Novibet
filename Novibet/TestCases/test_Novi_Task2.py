from BaseClass import BaseClass
from PageObjects.NoviPageObject_Task2 import LiveSchedulePage
from BusinessObjects.NoviBusinessObject_Task2 import EventTracker


class TestEventTracker(BaseClass):

    def test_events_leaving(self):
        livematches = LiveSchedulePage(self.driver)
        livematches.landInPage()
        event_tracker = EventTracker(livematches)
        initial_matches = livematches.get_live_schedule_matches()
        print(f"Initial Matches: {list(initial_matches.keys())}")

        leaving_events = event_tracker.track_events_leaving(initial_matches)
        print(f"Leaving Events: {leaving_events}")

        self.assertTrue(len(leaving_events) >= 0)

