from analysis.region_analyser import RegionAnalyser

analyser = RegionAnalyser()

image_path = "outputs/cropped_faces/faces/frame_0000.jpg"

analyser.analyse_image(image_path)
