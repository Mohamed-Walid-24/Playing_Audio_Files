#Convert Mp3 to Wav first
from pydub import AudioSegment
from pydub.playback import play

song = AudioSegment.from_wav("Ahmed.wav")
play(song)