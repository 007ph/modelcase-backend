# _*_ coding: utf-8 _*_
""" run.py """
import json
import os
from app import create_app,load_config
from waitress import serve  # type: ignore
from config.utils import parse_args
import sys



if __name__ == "__main__":
    kwargs = parse_args(sys.argv)
    db_config_file = kwargs.pop("db_config_file", None)
    if not db_config_file:
        raise TypeError("db_config_file is not support")
    app = create_app(db_config_file)
    serve(app, **kwargs)
else:
    app = create_app()