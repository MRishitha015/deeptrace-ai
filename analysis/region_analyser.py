import cv2

import numpy as np


class RegionAnalyser:

    def analyse_image(
        self,
        image_path
    ):

        image = cv2.imread(image_path)

        gray = cv2.cvtColor(
            image,
            cv2.COLOR_BGR2GRAY
        )

        sharpness_score = (
            cv2.Laplacian(
                gray,
                cv2.CV_64F
            ).var()
        )

        brightness_score = np.mean(gray)

        edges = cv2.Canny(
            gray,
            100,
            200
        )

        edge_score = np.mean(edges)

        texture_score = np.std(gray)

        result = {

            "sharpness_score":
            float(sharpness_score),

            "brightness_score":
            float(brightness_score),

            "edge_score":
            float(edge_score),

            "texture_score":
            float(texture_score)
        }

        return result
