import logging
from argparse import ArgumentParser

import uvicorn

from .log import logger


def main():
    parser = ArgumentParser(prog="txexpl", description="Transaction explainer.")

    parser.add_argument(
        "-s", "--server", help="Start a decoder http server", action="store_true"
    )

    parser.add_argument("-p", "--port", default=8081, type=int, help="Http server port")

    parser.add_argument("-v", "--verbose", help="Print log info", action="store_true")

    parser.add_argument("-u", "--url-base", help="External url base.")

    args = parser.parse_args()

    if args.verbose:
        logger.setLevel(logging.DEBUG)

    if args.server:
        from .server import URL_BASE, app, conf

        if args.url_base:
            conf[URL_BASE] = args.url_base
            logger.info(f"{URL_BASE}: {args.url_base}")
        else:
            if args.port:
                conf[URL_BASE] = f"http://localhost:{args.port}"
                logger.info(f"{URL_BASE}: {conf[URL_BASE]}")

        uvicorn.run(app, host="localhost", port=args.port)
    else:
        logger.error("Nothing to do")


if __name__ == "__main__":
    main()
