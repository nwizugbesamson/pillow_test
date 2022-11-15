
from cli import Audio
from dag_pipeline import pipeline
from make_vid import VideoCompiler
from state_mapping import Animator_Sequencer



chunks = make_chunks(Audio)
process_pipeline = pipeline(
    ...
)
from multiprocessing import Pool

with Pool(10) as pool:
    results = pool.map(process_pipeline, chunks)
compiled_video = compile_videos(results)

