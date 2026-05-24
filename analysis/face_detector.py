import cv2
import os


class FaceDetector:

    def __init__(self):

        self.face_cascade = cv2.CascadeClassifier(
            cv2.data.haarcascades +
            "haarcascade_frontalface_default.xml"
        )

    # Detect faces and draw rectangles
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

    # Crop detected faces
    def crop_faces(self, image_path):

        image = cv2.imread(image_path)

        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

        faces = self.face_cascade.detectMultiScale(
            gray,
            scaleFactor=1.1,
            minNeighbors=5,
            minSize=(30, 30)
        )

        output_dir = "outputs/cropped_faces"

        os.makedirs(output_dir, exist_ok=True)

        count = 0

        for (x, y, w, h) in faces:

            face_crop = image[y:y+h, x:x+w]

            filename = os.path.basename(image_path)

            name, ext = os.path.splitext(filename)

            output_path = os.path.join(
                output_dir,
                f"{name}_face_{count}.jpg"
            )

            cv2.imwrite(output_path, face_crop)

            print(f"Cropped face saved: {output_path}")

            count += 1


# Example Usage
if __name__ == "__main__":

    detector = FaceDetector()

    image_path = "test.jpg"

    detector.detect_faces(image_path)

    detector.crop_faces(image_path)
