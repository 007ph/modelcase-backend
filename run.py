# _*_ coding: utf-8 _*_
""" run.py """
from app import create_app
from waitress import serve  # type: ignore
from config.utils import parse_args
import sys

app = create_app()

if __name__ == "__main__":
    kwargs = parse_args(sys.argv)
    serve(app, **kwargs)
