import youtube_queuer.youtube_download as yt


class TestFindTitle(object):
    def test_single_video(self):
        url = 'https://www.youtube.com/watch?v=COlIstNfkZk'
        assert yt.find_title(url) == 'Benjamin Fry - TrustDNS [Bay Area Rust @ Cloudflare, May 2018]'

    def test_playlist(self):
        url = 'https://www.youtube.com/watch?v=mxlpQMJt8XA&list=PL4o6UvJIdPNooxA4WQskzhF0_qe5GTMED'
        assert yt.find_title(url) == 'Factorio: Entry Level to Megabase'
