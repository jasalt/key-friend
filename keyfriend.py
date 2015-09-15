# Fetch song metadata from Echonest. Fallback to keyfinder.
# Misc features for automating work with digital recordings

# TODO
# - Parse input files
# - Parse file metadata
# - Fetch data from echonest
# - Local keyfinder software libary integration
# - Drag Drop UI with Qt4 or something
# - Playlist view
# - Harmonic playlist sorting
# - Downloader

from pyechonest import song
s = song.search(artist='bluescreens', title='strike one')
it = s[1]
it.get_audio_summary()
