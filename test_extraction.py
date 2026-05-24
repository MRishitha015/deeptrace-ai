from extraction.media_extractor import MediaExtractor

video_path = "sample.mp4"

extractor = MediaExtractor(video_path)

extractor.extract_frames()
