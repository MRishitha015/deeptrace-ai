class TimelineGenerator:

    def __init__(self, interval=2):
        self.interval = interval

    def generate_timeline(self, duration):

        timeline = []

        start = 0

        while start < duration:

            end = start + self.interval

            timeline.append({
                "start": start,
                "end": end,
                "status": "PENDING"
            })

            start += self.interval

        return timeline
