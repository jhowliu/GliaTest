from lib.crawler import *

import sys

def start(board):
    c = PttWebCrawler(as_lib=True) 
    last_page = c.getLastPage(board)
    start_page = last_page-5 if last_page > 5 else 0
    c.parse_articles(start_page, last_page, board)

if __name__ == '__main__':

    if len(sys.argv) < 2:
        print('Usage: python pttCrawler.py <BoardName>')
        sys.exit(1)

    start(sys.argv[1])