from PageObjects.NoviPageObject_Task3 import LiveFootballPage

class LiveFootballBusiness:
    def __init__(self,driver):
        self.driver=driver
        self.NoviPageObject_Task3 = LiveFootballPage(self.driver)

    def common_events(self,data,lb_data):
        common_values = []
        for row1 in LiveFootballPage.get_matches_live_programm():
            for row2 in LiveFootballPage.get_matches_live_bet():
                common_elements = set(row1) & set(row2)
                if common_elements:
                    common_values.append(common_elements)
        return common_values

    def mark_delayed_events(self):
        live_events = self.common_events()
        delayed_events = []
        for event in live_events:
            if self.page.is_delayed(event):
                team1, team2, score, status = self.page.extract_match_info(event)
                delayed_events.append({
                    'team1': team1,
                    'team2': team2,
                    'score': score,
                    'status': status,
                    'is_delayed': True
                })
        return delayed_events
