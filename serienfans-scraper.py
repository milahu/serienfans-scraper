#!/usr/bin/env python3

import re
import sys
import time
import json
import asyncio
import argparse
import logging
import urllib.parse

# pypi modules
import requests
import aiohttp
import psutil
import nest_asyncio
from bs4 import BeautifulSoup


# allow nesting multiple asyncio event loops
# fix: RuntimeError: This event loop is already running
nest_asyncio.apply()



#class SerienfansScraper(BaseScraper): # todo

class SerienfansScraper:

    def __init__(self):
        self.domain = "serienfans.org"
        self.parse_args()
        self.init_logger()

    async def async_init(self):
        await self.args.func()

    def __await__(self) -> "ClientSession":
        """
        async constructor

        scraper = await SerienfansScraper()
        # ...
        await scraper.close()
        """
        return self.async_init().__await__()

    def init_logger(self):
        logging_level = "INFO"
        if self.args.debug:
            # TODO disable debug log from selenium (too verbose)
            logging_level = "DEBUG"
        logging.basicConfig(
            format="%(asctime)s %(name)s %(levelname)s %(message)s",
            level=logging_level,
        )
        self.logger = logging.getLogger("fetch-subs")

    def init_aiohttp_chromium(self):
        #sys.path.append("lib/thirdparty/aiohttp_chromium/src")
        import aiohttp_chromium
        #print("imported aiohttp_chromium", aiohttp_chromium)

    def log(self, *args):
        self.logger.info(" ".join(map(str, args)))

    def parse_args(self):
        parser = argparse.ArgumentParser(
            prog="serienfans-scraper",
            #description="",
            #epilog="Text at the bottom of help",
        )
        parser.add_argument(
            "--debug",
            default=False,
            action="store_true",
            help="show debug messages",
        )
        subparsers = parser.add_subparsers(title="subcommands", required=True)
        self.add_parser_search(subparsers)
        self.add_parser_get(subparsers)
        #args = parser.parse_args(sys.argv)
        self.args = parser.parse_args()

    def add_parser_search(self, subparsers):
        parser = subparsers.add_parser("search")
        parser.add_argument("query")
        parser.set_defaults(func=self.search)

    def add_parser_get(self, subparsers):
        parser = subparsers.add_parser("get")
        parser.add_argument("url")
        parser.set_defaults(func=self.get)

    async def search(self):
        query = urllib.parse.urlencode({
            "q": self.args.query,
            "ql": "DE",
        })
        url = f"https://serienfans.org/api/v2/search?{query}"
        # TODO aiohttp
        #print("query", self.args.query)
        #print("url", url)
        response = requests.get(url) # , **requests_get_kwargs)
        assert response.status_code == 200
        #response_status = response.response_status
        #print("response.status_code", response.status_code)
        #print("response.headers", response.headers)
        #print("response.text", response.text)
        result = response.json()
        #print("result", json.dumps(result, indent=2))
        for res_key in ["result", "resultCounterPart"]:
            for res in result.get(res_key, []):
                if res_key == "result":
                    #url = "https://serienfans.org/" + res["url_id"]
                    url = f"https://{self.domain}/" + res["url_id"]
                else:
                    url = "https://" + result["counterPartIs"] + "/" + res["url_id"]
                title_year = res["title"] + " (" + str(res["year"]) + ")"
                print(url, "#", title_year, "#", res["description"].replace("\n", "\\n"))

    async def get(self):
        """
        query = urllib.parse.urlencode({
            "q": self.args.url,
            "ql": "DE",
        })
        url = f"https://serienfans.org/api/v2/search?{query}"

        https://serienfans.org/api/v1/HzUXRYhqxEFNr7CWQPJcddwPNCe4dFfT/season/1?lang=ALL&_=1726173474938
        https://serienfans.org/api/v1/HzUXRYhqxEFNr7CWQPJcddwPNCe4dFfT/season/2?_=1726173480931

        TODO? headers: cookie, Referer

        initSeason initSeason('cyD5Ayq52BtxzC1Mf5ATvQRLmeFRTbze', 5, '', 'ALL'); cyD5Ayq52BtxzC1Mf5ATvQRLmeFRTbze 5

        """

        url = self.args.url

        # TODO aiohttp
        #print("query", self.args.query)
        #print("url", url)
        # TODO retry on timeout
        response = requests.get(url) # , **requests_get_kwargs)

        assert response.status_code == 200
        #response_status = response.response_status
        #print("response.status_code", response.status_code)
        #print("response.headers", response.headers)
        #print("response.text", response.text)
        #result = response.json()
        #print("result", json.dumps(result, indent=2))
        html = response.text

        r"""
        num_initSeason_matches = 0
        for x in re.finditer(r"initSeason\('([0-9a-zA-Z]+)', ([0-9]+), '', 'ALL'\);", html):
            num_initSeason_matches += 1
        # TODO is this always 1?
        # yes, this should be unique:
        #   initSeason('HzUXRYhqxEFNr7CWQPJcddwPNCe4dFfT', 5, '', 'ALL');
        if num_initSeason_matches != 1:
            print(f"num_initSeason_matches: {num_initSeason_matches} != 1")
        """

        init_season_match = re.search(r"initSeason\('([0-9a-zA-Z]+)', ([0-9]+), '', 'ALL'\);", html)
        #print("init_season_match", init_season_match.group(0), init_season_match.group(1), init_season_match.group(2))
        # example: "cyD5Ayq52BtxzC1Mf5ATvQRLmeFRTbze"
        session_id = init_season_match.group(1)
        # example: 5
        num_seasons = int(init_season_match.group(2))

        # loop seasons
        for season_num in range(1, 1 + num_seasons):
            # sleep between requests
            time.sleep(1)
            request_time = int(time.time() * 1000)
            season_url = f"https://serienfans.org/api/v1/{session_id}/season/{season_num}?_={request_time}"
            season_response = requests.get(season_url) # , **requests_get_kwargs)

            print(f"season {season_num}")

            assert season_response.status_code == 200

            season = season_response.json()

            # debug
            write_response_files = False
            #write_response_files = True
            if write_response_files:
                print(f"  writing season-{season_num}.json")
                with open(f"season-{season_num}.json", "w") as f:
                    json.dump(season, f, indent=2)
                print(f"  writing season-{season_num}.html")
                with open(f"season-{season_num}.html", "w") as f:
                    f.write(season["html"])

            # season["qualitys"] # ["1080p", "480p", "720p"]
            # TODO filter by quality
            #   but only as a secondary filter after the season + episode filter

            # season["bubblesQuality"] # ?

            # season["languages"] # ["DE", "EN"]
            # TODO filter by language
            #   but only as a secondary filter after the season + episode filter

            # season["bubblesLanguage"] # ?

            season_html = season["html"]

            # release_name
            # selector = ""
            # # body > div:nth-child(1) # what?
            # example: "Solar.Opposites.S01.GERMAN.DL.1080P.WEB.H264-WAYNE"

            season_soup = BeautifulSoup(season_html, "html.parser")

            for entry in season_soup.select("div.entry"):

                # entry: div.row, div.row, div.list.simple
                release_name = entry.select_one("small").text.strip()
                print(f"  release {release_name}")

                # 480p | 1.3 GB # TODO parse quality + size
                release_morespec = entry.select_one("div:nth-child(1) > div > h3 > span.morespec").text.strip()

                # 4SF # release_group_name
                release_grouptag = entry.select_one("div:nth-child(1) > div > h3 > span.grouptag").text.strip()

                # loop hosters: complete seasons

                # body > div:nth-child(2) > div:nth-child(1) > div > small
                # body > div:nth-child(4) > div:nth-child(1) > div > small
                # body > div:nth-child(6) > div:nth-child(1) > div > small

                for hoster_link in entry.select("div:nth-child(2) > a"):

                    # FIXME skip offline links
                    # status:
                    # body > div:nth-child(2) > div:nth-child(2) > a:nth-child(1) > i.st.off # offline, red
                    # body > div:nth-child(2) > div:nth-child(2) > a:nth-child(1) > i.st.mix # mixed, orange
                    # body > div:nth-child(2) > div:nth-child(2) > a:nth-child(4) > i.st
                    link_online = True
                    if hoster_link.select_one("i.st.off"):
                        link_online = False
                    elif hoster_link.select_one("i.st.mix"):
                        # status: mixed
                        # only some links are online
                        link_online = None
                    #elif hoster_link.select_one("i.st"):
                    #    link_online = True
                    
                    if link_online == False:
                        # skip offline link
                        continue

                    link_status = "online" if link_online else "mixed"

                    hoster_name = hoster_link.select_one("div > span").text.strip()
                    # hoster_url returns redirect to filecrypt.co (etc)
                    # hoster_url expires after some time

                    hoster_url = "https://serienfans.org" + hoster_link["href"]
                    # avoid rate-limiting (response status 429)

                    time.sleep(3)
                    response = requests.head(hoster_url) # , **requests_get_kwargs)

                    if response.status_code != 302:
                        # status_code can be 429 = too many requests
                        print("      response.status_code", response.status_code)

                    assert response.status_code == 302

                    hoster_url_2 = response.headers['Location']
                    #print(f"      redirect {hoster_url} -> {hoster_url_2}")
                    hoster_url = hoster_url_2
                    print(f"    hoster {hoster_name} {link_status} {hoster_url}")

                    # TODO group hoster_url by container ID
                    # example
                    # hoster 1fichier   https://filecrypt.cc/Container/6e6eb65ace.html?mirror=0
                    # hoster rapidgator https://filecrypt.cc/Container/6e6eb65ace.html?mirror=1
                    # hoster ddownload  https://filecrypt.cc/Container/6e6eb65ace.html?mirror=2
                    # hoster katfile    https://filecrypt.cc/Container/6e6eb65ace.html?mirror=3

                    #break # TODO remove

                include_episode_links = False

                if include_episode_links:

                    # loop hosters: episodes
                    # NOTE most download links are complete seasons

                    # body > div:nth-child(6) > div.list.simple > div:nth-child(2) > div:nth-child(2)
                    # body > div:nth-child(6) > div.list.simple > div:nth-child(3) > div:nth-child(2)
                    # body > div:nth-child(6) > div.list.simple > div:nth-child(4) > div:nth-child(2)

                    for episode_div in entry.select("div.list.simple > div.row:not(.head)"):
                    #for episode_div in entry.select("div.list.simple > div.row"):

                        # body > div:nth-child(2) > div.list.simple > div:nth-child(2) > div:nth-child(1)
                        # body > div:nth-child(2) > div.list.simple > div:nth-child(3) > div:nth-child(1)
                        # body > div:nth-child(2) > div.list.simple > div:nth-child(4) > div:nth-child(1)
                        episode_num = episode_div.select_one("div:nth-child(1)").text.strip() # "1." "2." "3." ...
                        episode_num = episode_num.replace(".", "")
                        episode_num = int(episode_num)

                        # body > div:nth-child(2) > div.list.simple > div:nth-child(2) > div:nth-child(2)
                        # body > div:nth-child(2) > div.list.simple > div:nth-child(3) > div:nth-child(2)
                        # body > div:nth-child(2) > div.list.simple > div:nth-child(4) > div:nth-child(2)
                        episode_name = episode_div.select_one("div:nth-child(2)").text.strip()

                        print(f"  episode {episode_num} {episode_name}")

                        # for episode_div in entry.select("div.list.simple > div.row"):

                        # loop hosters

                        # body > div:nth-child(2) > div.list.simple > div:nth-child(2) > div.row > a:nth-child(1) > div > span
                        # body > div:nth-child(2) > div.list.simple > div:nth-child(2) > div.row > a:nth-child(2) > div > span
                        #        entry                                episode_div                  hoster_link

                        # body > div:nth-child(2) > div.list.simple > div:nth-child(3) > div.row > a:nth-child(1) > div > span
                        # body > div:nth-child(2) > div.list.simple > div:nth-child(3) > div.row > a:nth-child(2) > div > span
                        #        entry                                episode_div                  hoster_link

                        done_head = False

                        #for hoster_link in episode_div.select("div:nth-child(2) > div.row > a"):
                        for hoster_link in episode_div.select("div.row > a"):
                            """
                            if not done_head:
                                print(f"    episode {episode_num} {episode_name}")
                                done_head = True
                            """
                            short_hoster_name = hoster_link.select_one("div > span").text.strip()
                            hoster_url = "https://serienfans.org" + hoster_link["href"]
                            print(f"      hoster {short_hoster_name} {hoster_url}")

            #break # TODO remove

# season picker
"""
initSeason('Nawdpy3RULN3KGanf6yVMfbvHDCYudAr', $(this).val(), '', 'ALL');
       <script>
        if('5' != '') {
          initSeason('Nawdpy3RULN3KGanf6yVMfbvHDCYudAr', 5, '', 'ALL');
        }
       </script>
"""

async def main():
    scraper = await SerienfansScraper()



if __name__ == "__main__":
    # asyncio.gather is needed to fix "Task exception was never retrieved"
    # https://stackoverflow.com/questions/46890646
    asyncio.run(asyncio.gather(main()))
