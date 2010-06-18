import sys

from rsstracker import RSSTracker
from Growl import GrowlNotifier

def main(url, fname, tmpfname = None):
    gn = GrowlNotifier('rssgrowler', ['newarticle'])
    gn.register()
    for article in RSSTracker(url, fname, tmpfname = tmpfname):
        gn.notify('newarticle', article.title, article.summary)
        article.save()

if __name__ == '__main__':
    assert len(sys.argv) in (3, 4)
    url = sys.argv[1]
    fname = sys.argv[2]
    tmpfname = sys.argv[3] if len(sys.argv) == 4 else None

    main(url, fname, tmpfname)
