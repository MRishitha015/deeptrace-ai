class TimelineGenerator:
    def __init__(self, interval=2):
        self.interval = interval

    def generate_intervals(self, duration):
        intervals = []

        start = 0

        while start < duration:
            end = min(start + self.interval, duration)

            intervals.append({
                "start": start,
                "end": end
            })

            start += self.interval

        return intervals
