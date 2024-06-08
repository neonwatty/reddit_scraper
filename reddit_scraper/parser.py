from bs4 import BeautifulSoup
from datetime import datetime, timezone


def parse_responses(responses: list, links: list) -> list:
    try:
        created_at = int(datetime.now(tz=timezone.utc).timestamp())
        data = []
        for ind, response in enumerate(responses):
            if response is not None:
                # make request
                text = response.text
                soup = BeautifulSoup(text, features="html.parser")

                # collect total member and online counts
                members_span = soup.select_one('span:-soup-contains("members")')
                total_member_count = int(
                    members_span.findChild("faceplate-number")["number"]
                )

                online_span = soup.select_one('span:-soup-contains("online")')
                total_online_count = int(
                    online_span.findChild("faceplate-number")["number"]
                )

                # create entry
                entry = {}
                entry["reddit_url"] = links[ind]
                entry["timestamp"] = created_at
                entry["total_member_count"] = total_member_count
                entry["total_online_count"] = total_online_count
                data.append(entry)
            else:
                print(f"FAILURE: response for link num {ind} - {links[ind]} failed")
        print("SUCCESS: parse_responses finished successfully")
        return data
    except Exception as e:
        print(f"FAILURE: parse_responses failed with exception {e}")
        return None
