#--------------------------------------------------------------------------------
# 참조 모듈 목록.
#--------------------------------------------------------------------------------
from __future__ import annotations
from typing import Any, Final, Optional, Type, TypeVar, Union, Tuple, List, Dict, Set, cast
import builtins
import os
import sys
from dduk.core import Repository
from .manifestparser import ManifestParser
from .servicemanager import ServiceManager
from .networkmanager import NetworkManager


#--------------------------------------------------------------------------------
# 파일 진입점.
#--------------------------------------------------------------------------------
if __name__ == "__main__":
	builtins.print("DDUK-SERVICES")

	# 매니페스트 로드.
	manifestParser = ManifestParser()
	manifestParser.Parse("service.manifest")

	# 서비스 매니저 시작.
	serviceManager = Repository.Get(ServiceManager)
	serviceManager.Run()

	# 서버 시작.
	networkManager = Repository.Get(NetworkManager)
	networkManager.Run("0.0.0.0", 5000)