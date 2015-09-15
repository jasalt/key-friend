# Fetch song metadata from Echonest. Fallback to keyfinder.
# Misc features for automating work with digital recordings

# TODO
# - Parse input files
# - Parse file metadata
# - Command Line Interface
#    http://click.pocoo.org/5/
# - Fetch data from echonest
#    https://github.com/echonest/pyechonest
#    http://developer.echonest.com/raw_tutorials/faqs/faq_04.html
# - Local keyfinder software libary integration
#    http://www.ibrahimshaath.co.uk/keyfinder/
#    C++ lib https://github.com/ibsh/libKeyFinder
# - Drag Drop UI with Qt4 or something
#    http://zetcode.com/gui/pyqt4/dragdrop/
# - Playlist view
# - Harmonic playlist sorting
#    http://djtechtools.com/2013/12/20/advanced-key-mixing-techniques-for-djs/
# - Downloader
#    youtube-dl spotify-onthego spotify-ripper etc.

from pyechonest import song
s = song.search(artist='bluescreens', title='strike one')
it = s[1]
it.get_audio_summary()
