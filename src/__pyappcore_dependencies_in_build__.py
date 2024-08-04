# Automatic dependency generation code used when building pyinstaller.
# Created time : 2024-08-04 18:59:00.123366


from __future__ import annotations
import bpy
from PIL import ImageOps, ImageDraw, Image
import bmesh # type: ignore
from boto3.session import Session
from botocore.client import Config, BaseClient
from botocore.exceptions import ClientError, PartialCredentialsError, NoCredentialsError
import builtins # type: ignore
import certifi
from collections import Counter
from src.data import *
from datetime import datetime # type: ignore
from dduk.process.processinfo import ProcessInfo
from dduk.process.processmanager import ProcessManager
import debugpy
from dotenv import load_dotenv
from enum import Enum, auto
import hashlib
from http import HTTPStatus
import io
import json
import src.main
from math import radians # type: ignore
from mathutils import Euler, Vector
import os
import platform
from pyappcore import Application, makecode, str_util
from requests import Response
import service
from shapely.geometry import mapping, Polygon
from shapely.ops import transform
import shutil
from slack_sdk import WebClient
from slack_sdk.errors import SlackApiError
from src.data import * # type: ignore
from src.service.modeldata import ModelData, ModelState # type: ignore
from src.service.network import AltavaAPIHelper, R2APIHelper, SlackAPIHelper # type: ignore
from src.service.process import Process # type: ignore
from src.service.r2 import R2 # type: ignore
from src.service.servicetype import ServiceType # type: ignore
from src.service.slack import Slack # type: ignore
from src.validator import GetJsonData # type: ignore
import sys # type: ignore
import time # type: ignore
from typing import Optional, TypeVar, Union, cast, List, Any, Dict, Set, Type, Final
import validator
import validator.blender # type: ignore
import validator.check_list # type: ignore
import zipfile