class EventTracker:
    def __init__(self, live_schedule_page):
        self.live_schedule_page = live_schedule_page

    def track_events_leaving(self, initial_schedule):
        leaving_events = []

        for match_key in initial_schedule.keys():
            if not self.live_schedule_page.match_exists(match_key):
                leaving_events.append(match_key)

        return leaving_events
