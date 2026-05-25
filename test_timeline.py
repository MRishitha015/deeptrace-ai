from extraction.timeline_generator import TimelineGenerator

generator = TimelineGenerator()

timeline = generator.generate_timeline(
    duration=10
)

print(timeline)
