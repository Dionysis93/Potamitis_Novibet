from PageObjects.NoviPageObject_Task3 import LiveFootballPage
from BusinessObjects.NoviBusinessObject_Task3 import LiveFootballBusiness
from BaseClass import BaseClass


class LiveFootballTestCase(BaseClass):

    def test_extract_match_info(self):
        livepage = LiveFootballPage(self.driver)
        livedelay = LiveFootballBusiness(self.driver)
        livepage.liveBet()
        match_info = livedelay.get_all_match_info()
        for info in match_info:
            print(f"{info['team1']} vs {info['team2']} - Score: {info['score']} - Status: {info['status']} - Delayed: {info['is_delayed']}")

    def test_mark_delayed_events(self,livedelay):
        delayed_events = livedelay.mark_delayed_events()
        for event in delayed_events:
            print(f"Delayed Event: {event['team1']} vs {event['team2']} - Score: {event['score']} - Status: {event['status']} - Delayed: {event['is_delayed']}")