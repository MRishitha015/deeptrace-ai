from extraction.timeline_generator import TimelineGenerator

from analysis.timeline_analyser import (
    TimelineAnalyser
)

generator = TimelineGenerator()

timeline = generator.generate_timeline(
    duration=10
)

analyser = TimelineAnalyser()

result = analyser.analyse_timeline(
    timeline,
    fake_score=70
)

print(result)
