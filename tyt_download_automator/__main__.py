from .automator import MainPage, EpisodePage, format_show_filename


def main():
    main_page = MainPage()
    main_page.go()
    login_page = main_page.click_login_button()
    login_page.enter_credentials()
    page_links = main_page.get_episode_page_links()
    download_details = []
    for link in page_links:
        page = EpisodePage(link)
        download_url, filename = page.get_download_details()
        download_details.append((download_url, filename))
    return


if __name__ == "__main__":
    main()
