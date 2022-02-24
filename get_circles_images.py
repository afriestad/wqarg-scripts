import os
import re
import logging
import requests
import hashlib

SPREADSHEET_URL = 'https://opensheet.elk.sh/1Y4qoXTpd0ZO2CRZzgYV3Lvd1Aihui_Ya6p0V89nKdNU/Unique%20Codes'
EARLY_ACCESS_DENIED_MD5 = 'ignore'

logger = logging.getLogger(__name__)


def download_file(url):
    logger.info('Fetching %s', url)
    local_filename = os.path.join('imgs', url.split('/')[-1])

    if os.path.exists(local_filename):
        print("==> exists, skipping")
        return

    try:
        with requests.get(url) as r:
            r.raise_for_status()
            
            with open(local_filename, 'wb') as f:
                f.write(r.content)
    except requests.exceptions.HTTPError as e:
        logger.error('%s', e)


def main():
    
    os.makedirs('imgs', exist_ok=True)
    sheet_json = requests.get(SPREADSHEET_URL).json()

    url_re = re.compile('^https://www.bungie.net/pubassets/wqarg/strips/[a-z0-9]{8}-[a-z0-9]{4}-[a-z0-9]{4}-[a-z0-9]{4}-[a-z0-9]{12}.png')
    image_urls = [x['Image Link'] for x in sheet_json if url_re.match(x['Image Link'])]
    for url in image_urls:
        print(url)
        download_file(url)


if __name__ == "__main__":
    main()