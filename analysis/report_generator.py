class ReportGenerator:

    def generate_report(
        self,
        fake_result,
        timeline,
        suspicious_frames,
        frame_confidences
    ):

        report = {

            "verdict":
            fake_result["verdict"],

            "fake_score":
            fake_result["fake_score"],

            "timeline":
            timeline,

            "suspicious_frames":
            suspicious_frames,

            "frame_confidences":
            frame_confidences
        }

        return report
