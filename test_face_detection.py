from analysis.face_detector import FaceDetector

detector = FaceDetector()

image_path = "outputs/frames/frame_0000.jpg"

detector.detect_faces(image_path)
