import requests
from typing import Optional
from bs4 import BeautifulSoup
from dataclasses import dataclass, field


@dataclass
class AnimeInfo:
    title: str      = 'Unknown'
    genres: str     = 'Unknown'
    episodes: str   = 'Unknown'
    rating: str     = 'Unkwown'
    duration: str   = 'Unknown'
    aired: str      = 'Unknown'
    thumnail: str   = 'Unknown'
    download: dict  = field(default_factory=dict)


def get_anime_info(query: str) -> Optional[AnimeInfo]:
    ''' Get information about an anime including download links if available

    Examples:
    
    >>> get_anime_info('Naruto')
    AnimeInfo(title='Naruto Shippuden (Season 1-21 + Naruto + Movies + OVAs) 1080p Dual Audio HEVC', 
              genres='Action, Adventure, Comedy, Super Power, Martial Arts, Shounen', 
              episodes='(Seasons 1-21 + Movies + OVAs)', 
              rating='PG-13 – Teens 13 or older', 
              duration='23 min. per ep.', 
              aired='Unknown', 
              thumnail='https://kayoanime.com/wp-content/uploads/2021/03/shippud-season-1-21-movies-ovas-1080p-dual-audio-hevc-390x220.jpg', 
              download={'OVA Collections': 'https://drive.google.com/drive/folders/1qswTqH9qFAt8Gs_u-TBJnxlSCrKRVFVX?usp=sharing'}
            )
    
    >>> get_anime_info('Handa Kun') 
    AnimeInfo(title='Handa-Kun (Season 1) 1080p Dual Audio HEVC', 
              genres='Slice of Life, Comedy, Shounen', episodes='12', 
              rating='PG-13 – Teens 13 or older', 
              duration='24 min. per ep.', 
              aired='Jul 8, 2016 to Sep 23, 2016', 
              thumnail='https://kayoanime.com/wp-content/uploads/2021/01/handa-kun-season-1-1080p-dual-audio-hevc-390x220.jpg', 
              download={'1080p': 'https://tinyurl.com/y3bx4wtl'}
            )
    '''
    url = f"https://kayoanime.com/?s={query}"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    results = soup.select('#posts-container > li')

    if not results:
        return None

    anime_info = AnimeInfo()

    post = results[0]
    head = post.select_one('div.post-details > h2 > a')
    link, title = head.get('href'), head.text
    imgurl = post.find('img').get('src')

    anime_info = AnimeInfo()

    anime_info.title = title
    anime_info.thumnail = imgurl


    # Get more details
    response = requests.get(link)
    soup = BeautifulSoup(response.text, 'html.parser')

    post = soup.select_one('#the-post')
    if not post:
        return None

    dwld_div = []
    info_div = []

    for div in post.select('div.toggle.tie-sc-open'):
        head = div.select_one('h3.toggle-head').text
        if head.startswith("Information"):
            info_div = div
        
        elif head.startswith("Download"):
            dwld_div = div
    
    link_tags = dwld_div.select('div.toggle-content > a') if dwld_div else []
    for tag in link_tags:
        download_link = tag.get('href')
        name = tag.text
        anime_info.download[name] = download_link
    
    items = info_div.select('div.toggle-content > ul > li') if info_div else []
    for item in items:
        key, value = item.text.split(': ')
        key = key.lower()
        if key in anime_info.__dict__:
            setattr(anime_info, key, value)
    
    return anime_info