import grequests


def make_requests(links: list) -> list:
    try:
        # "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36"
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36"
        }
        rs = (grequests.get(u, headers=headers) for u in links)

        def exception_handler(request, exception):
            print(exception)

        responses = grequests.map(rs, exception_handler=exception_handler)
        for ind, resp in enumerate(responses):
            if resp.status_code != 200:
                print(
                    f"FAILURE: link {links[ind]} responded with status_code {resp.status_code}"
                )
            else:
                print(
                    f"SUCCESS: link {links[ind]} responded with status_code {resp.status_code}"
                )

        print("SUCCESS: make_requests finished successfully")
        return responses
    except Exception as e:
        print(f"FAILURE: make_requests failed with exception {e}")
        return None
