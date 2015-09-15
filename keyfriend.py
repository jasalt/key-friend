#!/usr/bin/env python
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


# from pyechonest import song
import click

from pyechonest import config
from secrets import ECHONEST_KEY
from pyechonest import song
from toolz import take
from tabulate import tabulate

config.ECHO_NEST_API_KEY = ECHONEST_KEY


def print_search_results(results):
    rows = [['Artist', 'Title', 'BPM', 'Key', 'Mode']]  # 'Genre',
    for s in results:
        ssummary = s.get_audio_summary()
        rows.append([s.artist_name, s.title,  # , ','.join(s.song_type)
                     ssummary['tempo'], ssummary['key'], ssummary['mode']])

    print(tabulate(rows))


@click.command()
# @click.option('--artist', default=None, help='Artist name')
@click.option('--query', prompt='Type search query for artist and title',
              help='Search by artist and title')
def song_info(query):
    result = song.search(combined=query)
    print_search_results(take(3, result))
    # it = s[1]
    # it.get_audio_summary()
    # mode (int): 0 or 1 (minor or major)
    # key (int): 0-11 (c, c-sharp, d, e-flat, e, f, f-sharp, g, a-flat, a,
    # b-flat, b)


if __name__ == '__main__':
    song_info()
