class ReportGenerator:

    def generate_report(
        self,
        fake_result,
        timeline,
        suspicious_frames,
        frame_confidences,
        total_frames_processed,
        total_faces_analyzed
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
            frame_confidences,

            "total_frames_processed":
            total_frames_processed,

            "total_faces_analyzed":
            total_faces_analyzed
        }

        return report
