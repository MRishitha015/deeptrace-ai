class FakeScoreCalculator:

    def calculate_score(self, analysis_result):

        sharpness = analysis_result["sharpness_score"]

        brightness = analysis_result["brightness_score"]

        fake_score = 0

        if sharpness < 100:
            fake_score += 40

        if brightness < 60 or brightness > 190:
            fake_score += 30

        fake_score = min(fake_score, 100)

        result = {
            "fake_score": fake_score,
            "verdict": "FAKE" if fake_score >= 50 else "REAL"
        }

        return result
