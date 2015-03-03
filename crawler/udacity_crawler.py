from bs4 import BeautifulSoup
from urlparse import urlparse, urljoin
import urllib
import robotparser

def crawl_web(seed): # returns index, graph of inlinks
    if is_udacity(seed):
        tocrawl = [seed]
    else: 
        print "This seed is not a Udacity site!"
        return
    crawled = []
    graph = {}  # <url>, [list of pages it links to]
    index = {} 
    while tocrawl: 
        page = tocrawl.pop()
        if page not in crawled:
            soup, url = get_page(page)
            add_page_to_index(index, page, soup)
            outlinks = get_all_links(soup, url)
            graph[page] = outlinks
            add_new_links(tocrawl, outlinks)
            crawled.append(page)
    return index, graph

def get_all_links(page, url):
    links = []
    page_url = urlparse(url)
    base = page_url[0] + '://' + page_url[1]
    robots_url = base + 'robots.txt'
    rp = robotparser.RobotFileParser()
    rp.set_url(robots_url)
    print "Page url: " , page_url
    for link in page.find_all('a'):
        link_url = link.get('href')
        print "Found a link: ", link_url
        #Ignore links that are 'None'.
        if link_url == None: 
            pass
        elif not rp.can_fetch('*', link_url):
            print "Page off limits!" 
            pass        
        #Ignore links that are internal page anchors. 
        #Urlparse considers internal anchors 'fragment identifiers', at index 5. 
        elif urlparse(link_url)[5] and not urlparse(link_url)[2]: 
            pass
        elif urlparse(link_url)[1]:
            links.append(link_url)
        else:
            newlink = urljoin(base, link_url)
            links.append(newlink)
    return links

def add_new_links(tocrawl, outlinks):
    for link in outlinks:
        if link not in tocrawl:
            if is_udacity(link):
                tocrawl.append(link)

def add_page_to_index(index, url, content):
    try:
        text = content.get_text()
    except:
        return
    words = text.split()
    for word in words:
        add_to_index(index, word, url)
        
def add_to_index(index, keyword, url):
    if keyword in index:
        index[keyword].append(url)
    else:
        index[keyword] = [url]

def lookup(index, keyword):
    if keyword in index:
        return index[keyword]
    else:
        return None

def get_page(url):
    if url in cache:
        return cache[url]
    else:
        print "Page not in cache: " + url
        try: 
            content = urllib.urlopen(url).read()
            return BeautifulSoup(content)
        except:
            return BeautifulSoup(""), ""


def is_udacity(url):
    parsed_url = urlparse(url)
    if parsed_url[1] == 'www.udacity.com':
        return True
    else:
        return False
            
cache = {}
print crawl_web('http://www.udacity.com/cs101x/index.html')