class ReportGenerator:

    def generate_report(
        self,
        fake_result,
        timeline
    ):

        report = {

            "verdict":
            fake_result["verdict"],

            "fake_score":
            fake_result["fake_score"],

            "timeline":
            timeline
        }

        return report
