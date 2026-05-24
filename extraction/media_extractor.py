import cv2
import os


class MediaExtractor:
    def __init__(self, video_path, output_dir="outputs/frames"):
        self.video_path = video_path
        self.output_dir = output_dir

        os.makedirs(self.output_dir, exist_ok=True)

    def extract_frames(self, frame_interval=30):
        cap = cv2.VideoCapture(self.video_path)

        if not cap.isOpened():
            print("Error opening video")
            return

        frame_count = 0
        saved_count = 0

        while True:
            success, frame = cap.read()

            if not success:
                break

            if frame_count % frame_interval == 0:

                frame_name = f"frame_{saved_count:04d}.jpg"

                frame_path = os.path.join(
                    self.output_dir,
                    frame_name
                )

                cv2.imwrite(frame_path, frame)

                print(f"Saved: {frame_path}")

                saved_count += 1

            frame_count += 1

        print(f"Total frames processed: {frame_count}")
        print(f"Frames saved: {saved_count}")

        cap.release()

        print("Frame extraction completed")
