from reddit_scraper.links import links
from reddit_scraper.make_requests import make_requests
from reddit_scraper.parser import parse_responses
from reddit_scraper.sqlite_interactions import put_rows
from schedule import every, repeat, run_pending
import time


@repeat(every(30).minutes)
def main() -> None:
    try:
        responses = make_requests(links)
        data = parse_responses(responses, links)
        put_rows(data)
        print("SUCCESS: main finished successfully")
    except Exception as e:
        print(f"FAILURE: main failed with exception {e}")
        raise e


if __name__ == "__main__":
    main()
    while True:
        run_pending()
        time.sleep(1)