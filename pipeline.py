import os

from extraction.media_extractor import MediaExtractor

from analysis.face_detector import FaceDetector

from analysis.region_analyser import RegionAnalyser

from analysis.fake_score import FakeScoreCalculator

from extraction.timeline_generator import TimelineGenerator

from analysis.timeline_analyser import TimelineAnalyser

from analysis.report_generator import ReportGenerator


class DeepTracePipeline:

    def __init__(self, video_path):

        self.video_path = video_path

    def run(self):

        print("\nSTEP 1 — Extracting Frames")

        extractor = MediaExtractor(
            self.video_path
        )

        extractor.extract_frames()

        frame_path = "outputs/frames/frame_0000.jpg"

        print("\nSTEP 2 — Detecting Faces")

        detector = FaceDetector()

        detector.detect_faces(frame_path)

        face_found = detector.crop_faces(
            frame_path
        )

        if not face_found:

            return {
                "error":
                "No human face detected in video"
            }

        cropped_face = (
            "outputs/cropped_faces/"
            "frame_0000_face_0.jpg"
        )

        print("\nSTEP 3 — Region Analysis")

        analyser = RegionAnalyser()

        analysis_result = analyser.analyse_image(
            cropped_face
        )

        print(analysis_result)

        print("\nSTEP 4 — Fake Score")

        calculator = FakeScoreCalculator()

        fake_result = calculator.calculate_score(
            analysis_result
        )

        print(fake_result)

        print("\nSTEP 5 — Timeline Analysis")

        timeline_generator = TimelineGenerator()

        timeline = (
            timeline_generator.generate_timeline(
                duration=10
            )
        )

        timeline_analyser = TimelineAnalyser()

        final_timeline = (
            timeline_analyser.analyse_timeline(
                timeline,
                fake_result["fake_score"]
            )
        )

        print("\nSTEP 6 — Generating Report")

        report_generator = ReportGenerator()

        report = report_generator.generate_report(
            fake_result,
            final_timeline
        )

        print("\nFINAL REPORT")

        print(report)

        print("\nPIPELINE COMPLETED")

        return report
