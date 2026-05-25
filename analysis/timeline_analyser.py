class TimelineAnalyser:

    def analyse_timeline(
        self,
        timeline,
        fake_score
    ):

        for interval in timeline:

            if fake_score >= 50:
                interval["status"] = "FAKE"

            else:
                interval["status"] = "REAL"

        return timeline
