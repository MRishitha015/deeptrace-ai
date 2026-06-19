
from analysis.report_generator import ReportGenerator
from analysis.timeline_analyser import TimelineAnalyser
from extraction.timeline_generator import TimelineGenerator
from analysis.fake_score import FakeScoreCalculator
from analysis.region_analyser import RegionAnalyser
from analysis.face_detector import FaceDetector
from extraction.media_extractor import MediaExtractor
import os


class DeepTracePipeline:

    def __init__(self, video_path):
        self.video_path = video_path

    def run(self):

        # -------------------------------
        # CLEAN OLD OUTPUT FILES
        # -------------------------------

        frames_folder = "outputs/frames"
        cropped_folder = "outputs/cropped_faces"

        os.makedirs(frames_folder, exist_ok=True)
        os.makedirs(cropped_folder, exist_ok=True)

        # Remove old frames
        for file_name in os.listdir(frames_folder):
            file_path = os.path.join(frames_folder, file_name)

            if os.path.isfile(file_path):
                os.remove(file_path)

        # Remove old cropped faces
        for file_name in os.listdir(cropped_folder):
            file_path = os.path.join(cropped_folder, file_name)

            if os.path.isfile(file_path):
                os.remove(file_path)

        # -------------------------------
        # STEP 1 - Extract Frames
        # -------------------------------

        print("\nSTEP 1 — Extracting Frames")

        extractor = MediaExtractor(self.video_path)
        extractor.extract_frames()

        # -------------------------------
        # STEP 2 - Face Analysis
        # -------------------------------

        print("\nSTEP 2 — Temporal Face Analysis")

        frame_files = sorted(os.listdir(frames_folder))

        all_scores = []
        suspicious_frames = []
        frame_confidences = []

        detector = FaceDetector()
        analyser = RegionAnalyser()
        calculator = FakeScoreCalculator()

        total_frames_processed = 0
        total_faces_analyzed = 0

        for frame_file in frame_files:

            # Clear cropped faces before each frame
            for old_file in os.listdir(cropped_folder):

                old_path = os.path.join(
                    cropped_folder,
                    old_file
                )

                if os.path.isfile(old_path):
                    os.remove(old_path)

            frame_path = os.path.join(
                frames_folder,
                frame_file
            )

            print(f"\nProcessing {frame_file}")

            # Detect faces
            faces = detector.detect_faces(
                frame_path
            )

            face_count = len(faces)

            # Crop faces
            face_found = detector.crop_faces(
                frame_path
            )

            if not face_found:
                continue

            face_files = sorted(
                os.listdir(cropped_folder)
            )

            for face_file in face_files:

                face_path = os.path.join(
                    cropped_folder,
                    face_file
                )

                total_faces_analyzed += 1

                analysis_result = analyser.analyse_image(
                    face_path
                )

                print(f"\nAnalysis for {face_file}")
                print(analysis_result)

                fake_result = calculator.calculate_score(
                    analysis_result,
                    face_count
                )

                print(fake_result)

                score = fake_result["fake_score"]

                all_scores.append(score)

                if score >= 75:
                    confidence = "HIGH"

                elif score >= 50:
                    confidence = "MEDIUM"

                else:
                    confidence = "LOW"

                frame_data = {
                    "frame": frame_file,
                    "score": score,
                    "confidence": confidence
                }

                frame_confidences.append(
                    frame_data
                )

                if score >= 50:
                    suspicious_frames.append(
                        frame_data
                    )

            total_frames_processed += 1

        # -------------------------------
        # PREVENT DIVISION BY ZERO
        # -------------------------------

        if len(all_scores) == 0:

            return {
                "error": "No analyzable faces found"
            }

        average_fake_score = int(
            sum(all_scores) / len(all_scores)
        )

        if average_fake_score >= 50:
            final_verdict = "FAKE"

        else:
            final_verdict = "REAL"

        fake_result = {
            "fake_score": average_fake_score,
            "verdict": final_verdict
        }

        # -------------------------------
        # STEP 5 - Timeline Analysis
        # -------------------------------

        print("\nSTEP 5 — Timeline Analysis")

        timeline_generator = TimelineGenerator()

        timeline = timeline_generator.generate_timeline(
            duration=10
        )

        timeline_analyser = TimelineAnalyser()

        final_timeline = timeline_analyser.analyse_timeline(
            timeline,
            fake_result["fake_score"]
        )

        # -------------------------------
        # STEP 6 - Generate Report
        # -------------------------------

        print("\nSTEP 6 — Generating Report")

        report_generator = ReportGenerator()

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
