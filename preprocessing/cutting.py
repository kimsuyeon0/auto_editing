#!pip install pydub 라이브러리 설치
#!apt install ffmpeg


from pydub import AudioSegment
song = AudioSegment.from_mp3('14 YEAR OLD DRiVES TESLA! (online-audio-converter.com).wav')
ten_seconds = 10 * 1000 #10초
thirty_seconds=ten_seconds*3 #30초
one_min = ten_seconds * 6 #1분
ts=thirty_seconds

a1=song[:ts] #가져온 음악의 0초에서 30초까지

a1.export('result.wav', format='wav', parameters=["-q:a", "10", "-ac", "1"]) #내보내기 