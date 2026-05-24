import cv2
import os


class FaceDetector:
    def __init__(self):
        self.face_cascade = cv2.CascadeClassifier(
            cv2.data.haarcascades +
            "haarcascade_frontalface_default.xml"
        )

    def detect_faces(self, image_path):

        image = cv2.imread(image_path)

        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

        faces = self.face_cascade.detectMultiScale(
            gray,
            scaleFactor=1.1,
            minNeighbors=5,
            minSize=(30, 30)
        )

        for (x, y, w, h) in faces:

            cv2.rectangle(
                image,
                (x, y),
                (x + w, y + h),
                (0, 255, 0),
                2
            )

        output_dir = "outputs/faces"

        os.makedirs(output_dir, exist_ok=True)

        filename = os.path.basename(image_path)

        output_path = os.path.join(
            output_dir,
            filename
        )

        cv2.imwrite(output_path, image)

        print(f"Detected {len(faces)} face(s)")

        print(f"Saved: {output_path}")
