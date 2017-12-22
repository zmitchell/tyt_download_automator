from .automator import MainPage, EpisodePage, QueuedDownload, Downloader


def main():
    main_page = MainPage()
    main_page.go()
    login_page = main_page.click_login_button()
    login_page.enter_credentials()
    page_links = main_page.get_episode_page_links()
    download_details = [EpisodePage(link).get_download_details() for link in page_links]
    queued_downloads = [QueuedDownload(url, filename) for url, filename in download_details]
    downloader = Downloader()
    for item in queued_downloads:
        downloader.add_to_queue(item)
    downloader.process_download_queue()
    main_page.driver.quit()
    return


if __name__ == "__main__":
    main()
