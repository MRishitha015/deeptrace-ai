class FakeScoreCalculator:

    def calculate_score(
        self,
        analysis_result
    ):

        fake_score = 0

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

        edge_score = (
            analysis_result[
                "edge_score"
            ]
        )

        texture_score = (
            analysis_result[
                "texture_score"
            ]
        )

        if sharpness < 80:

            fake_score += 30

        if brightness < 50:

            fake_score += 10

        if edge_score < 20:

            fake_score += 30

        if texture_score < 30:

            fake_score += 30

        if fake_score >= 50:

            verdict = "FAKE"

        else:

            verdict = "REAL"

        return {

            "fake_score":
            fake_score,

            "verdict":
            verdict
        }
