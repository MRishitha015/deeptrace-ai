from analysis.region_analyser import RegionAnalyser
from analysis.fake_score import FakeScoreCalculator

image_path = "outputs/cropped_faces/faces/frame_0000.jpg"

analyser = RegionAnalyser()

analysis_result = analyser.analyse_image(image_path)

calculator = FakeScoreCalculator()

result = calculator.calculate_score(
    analysis_result
)

print(result)
