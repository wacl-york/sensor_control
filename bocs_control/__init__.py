import logging

# TODO remove duplicated elements that are in syslog
logging.basicConfig(
    format="[%(asctime)s.%(msecs)03d] %(levelname)s: %(filename)s:%(lineno)d %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
    level=logging.INFO,
    style="%",
)
