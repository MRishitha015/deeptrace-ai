class ReportGenerator:

    def generate_report(
        self,
        fake_result,
        timeline,
        suspicious_frames
    ):

        report = {

            "verdict":
            fake_result["verdict"],

            "fake_score":
            fake_result["fake_score"],

            "timeline":
            timeline,

            "suspicious_frames":
            suspicious_frames
        }

        return report
