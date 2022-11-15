import ffmpeg
import json
import time

# from ffmpeg import stream

""" split_wav `audio file` `time listing`
    `audio file` is any file known by local FFmpeg
    `time listing` is a file containing multiple lines of format:
        `start time` `end time` output name 
    times can be either MM:SS or S*
"""


class AudioSplit:

    def __init__(self, speaker, start, end, index) -> None:
        self.speaker  = speaker
        self.start = start
        self.end = end
        self.index = index
        self._stream =None

    @property
    def start_seconds(self):
        minute, sec = map(int, self.start.split(':'))
        total_time = (minute * 60) + sec
        return total_time


    @property
    def duration(self):
        minute, sec = map(int, self.end.split(':'))
        total_time = (minute * 60) + sec
        duration = total_time - self.start_seconds
        return duration

    @property
    def stream(self):
        return self._stream

    @stream.setter
    def stream(self, input_audio):
        self._stream = input_audio

    def __repr__(self) -> str:
        return f"SPEAKER: <{self.speaker}>, START: <{self.start_seconds}>, DURATION: <{self.duration}>, STREAM: <{self.stream}>"


_in_file = "data/Audio/Recording.m4a"

def make_time(elem: str):
    # allow user to enter times on CLI
    t = elem.split('-')
    try:
        # will fail if no ':' in time, otherwise add together for total seconds
        return int(t[0]) * 60 + float(t[1])
    except IndexError:
        return float(t[0])


def collect_from_file() -> list[AudioSplit]:
    """user can save times in a file, with start and end time on a line"""

    

    time_pairs = []
    with open("timestamp.json") as in_times:
        times_db = json.load(in_times)
        number_speakers = times_db["number_of_speakers"]
        diarize_parser = times_db["diarization"]
        for _id in diarize_parser:
            start, end = diarize_parser[_id][1].split('-')
            time_pairs.append(AudioSplit(diarize_parser[_id][0], start=start, end=end, index=_id))
    return time_pairs


def main():
    audios = []
    for audio_split in collect_from_file():
        # open a file, from `ss`, for duration `t`
        stream = ffmpeg.input(_in_file, ss=audio_split.start_seconds, t=audio_split.duration)
        print(type(stream))
        audio_split._stream = stream
        audios.append(audio_split)
        # and actually run
        # ffmpeg.run(stream)
        print(audio_split)

    return audios



if __name__ == "__main__":
    start = time.time()
    main()
    duration = time.time() - start
    print(f"Program runtime: {duration}s")