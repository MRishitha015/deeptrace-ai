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

        # CLEAN OLD OUTPUT FILES

        frames_folder = "outputs/frames"

        cropped_folder = (
            "outputs/cropped_faces"
        )

        os.makedirs(
            frames_folder,
            exist_ok=True
        )

        os.makedirs(
            cropped_folder,
            exist_ok=True
        )

        for file_name in os.listdir(
            frames_folder
        ):

            file_path = os.path.join(
                frames_folder,
                file_name
            )

            if os.path.isfile(file_path):

                os.remove(file_path)

        for file_name in os.listdir(
            cropped_folder
        ):

            file_path = os.path.join(
                cropped_folder,
                file_name
            )

            if os.path.isfile(file_path):

                os.remove(file_path)

        print("\nSTEP 1 — Extracting Frames")

        extractor = MediaExtractor(
            self.video_path
        )

        extractor.extract_frames()

        print(
            "\nSTEP 2 — Temporal Face Analysis"
        )

        frame_files = os.listdir(
            frames_folder
        )

        all_scores = []

        suspicious_frames = []

        frame_confidences = []

        detector = FaceDetector()

        analyser = RegionAnalyser()

        calculator = FakeScoreCalculator()

        for frame_file in frame_files:

            frame_path = os.path.join(
                frames_folder,
                frame_file
            )

            print(
                f"\nProcessing {frame_file}"
            )

            detector.detect_faces(
                frame_path
            )

            face_found = detector.crop_faces(
                frame_path
            )

            if not face_found:

                continue

            face_files = os.listdir(
                cropped_folder
            )
            total_frames_processed = 0

            total_faces_analyzed = 0
            for face_file in face_files:

                face_path = os.path.join(
                    cropped_folder,
                    face_file
                )
                total_frames_processed += 1

                analysis_result = (
                    analyser.analyse_image(
                        face_path
                    )
                )

                print(
                    f"\nAnalysis for {face_file}"
                )

                print(analysis_result)

                fake_result = (
                    calculator.calculate_score(
                        analysis_result
                    )
                )

                print(fake_result)

                all_scores.append(
                    fake_result["fake_score"]
                )

                # CONFIDENCE ANALYSIS

                score = fake_result[
                    "fake_score"
                ]

                if score >= 75:

                    confidence = "HIGH"

                elif score >= 50:

                    confidence = "MEDIUM"

                else:

                    confidence = "LOW"

                frame_data = {

                    "frame":
                    frame_file,

                    "score":
                    score,

                    "confidence":
                    confidence
                }

                frame_confidences.append(
                    frame_data
                )

                if score >= 50:

                    suspicious_frames.append(
                        frame_data
                    )

        # PREVENT DIVISION BY ZERO

        if len(all_scores) == 0:

            return {
                "error":
                "No analyzable faces found"
            }

        average_fake_score = int(
            sum(all_scores) / len(all_scores)
        )

        if average_fake_score >= 50:

            final_verdict = "FAKE"

        else:

            final_verdict = "REAL"

        fake_result = {

            "fake_score":
            average_fake_score,

            "verdict":
            final_verdict
        }

        print("\nSTEP 5 — Timeline Analysis")

        timeline_generator = (
            TimelineGenerator()
        )

        timeline = (
            timeline_generator.generate_timeline(
                duration=10
            )
        )

        timeline_analyser = (
            TimelineAnalyser()
        )

        final_timeline = (
            timeline_analyser.analyse_timeline(
                timeline,
                fake_result["fake_score"]
            )
        )

        print("\nSTEP 6 — Generating Report")

        report_generator = (
            ReportGenerator()
        )

        report = report_generator.generate_report(
            fake_result,
            final_timeline,
            suspicious_frames,
            frame_confidences,
            total_frames_processed,
            total_faces_analyzed
        )

        print("\nFINAL REPORT")

        print(report)

        print("\nPIPELINE COMPLETED")

        return report
