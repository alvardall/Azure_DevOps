import logging
import os


def logger():
    log_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "execut.log")
    logging.basicConfig(
        filename=log_path,
        level=logging.INFO,
        format="%(asctime)s - %(levelname)s - %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S",
        filemode="a",
        encoding="utf-8"
    )