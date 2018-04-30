from app.gitlab import Gitlab
import logging

if __name__ == "__main__":
    for _ in ("boto", "elasticsearch", "urllib3"):
        logging.getLogger(_).setLevel(logging.CRITICAL)
    gitlab = Gitlab()
    gitlab.do_extraction()



