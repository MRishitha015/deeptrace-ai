class FakeScoreCalculator:

    def calculate_score(
        self,
        analysis_result,
        face_count
    ):

        sharpness = (
            analysis_result[
                "sharpness_score"
            ]
        )

        brightness = (
            analysis_result[
                "brightness_score"
            ]
        )

        # Updated scoring logic
        score = 0

        if sharpness < 100:

            score += 40

        if brightness < 80:

            score += 30

        if face_count > 1:

            score += 10

        score = min(score, 100)

        if score >= 50:

            verdict = "FAKE"

        else:

            verdict = "REAL"

        return {

            "fake_score":
            score,

            "verdict":
            verdict
        }
