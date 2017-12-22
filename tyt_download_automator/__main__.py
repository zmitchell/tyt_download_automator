import time

import logzero

from .automator import MainPage, EpisodePage, QueuedDownload, Downloader


def main():
    main_page = MainPage()
    main_page.go()
    login_page = main_page.click_login_button()
    login_page.enter_credentials()
    while True:
        main_page.go()
        logger.info("Scraping...")
        page_links = main_page.get_episode_page_links()
        download_details = [EpisodePage(link).get_download_details() for link in page_links]
        queued_downloads = [QueuedDownload(url, filename) for url, filename in download_details]
        downloader = Downloader()
        for item in queued_downloads:
            downloader.add_to_queue(item)
        logger.info("Processing download queue...")
        downloader.process_download_queue()
        main_page.go()
        logger.info("Sleeping...")
        time.sleep(300)  # check every 5 minutes
    main_page.driver.quit()
    return


if __name__ == "__main__":
    log_fmt = "%(color)s[%(levelname)1.1s %(asctime)s]%(end_color)s %(message)s"
    log_formatter = logzero.LogFormatter(fmt=log_fmt)
    logzero.setup_default_logger(formatter=log_formatter)
    logger = logzero.logger
    main()
