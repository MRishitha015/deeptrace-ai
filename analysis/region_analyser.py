import cv2
import numpy as np


class RegionAnalyser:

    def analyse_image(self, image_path):

        image = cv2.imread(image_path)

        gray = cv2.cvtColor(
            image,
            cv2.COLOR_BGR2GRAY
        )

        laplacian_var = cv2.Laplacian(
            gray,
            cv2.CV_64F
        ).var()

        mean_intensity = np.mean(gray)

        result = {
            "sharpness_score": float(laplacian_var),
            "brightness_score": float(mean_intensity)
        }

        print(result)

        return result
