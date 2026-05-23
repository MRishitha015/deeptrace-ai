from extraction.media_extractor import MediaExtractor
from analysis.video_analyser import VideoAnalyser


class DetectionPipeline:
    def __init__(self, video_path):
        self.video_path = video_path

    def run(self):
        extractor = MediaExtractor(self.video_path)

        extractor.extract_frames()
        extractor.extract_audio()

        analyser = VideoAnalyser()
        analyser.analyse([])
