#--------------------------------------------------------------------------------
# 참조 모듈 목록.
#--------------------------------------------------------------------------------
from __future__ import annotations
from typing import Any, Final, Optional, Type, TypeVar, Union, Tuple, List, Dict, Set, cast
import builtins
from dduk.core import Repository
from src.datamanager import DataManager
from src.manifestparser import ManifestParser
from src.servicemanager import ServiceManager
from src.networkmanager import NetworkManager


#--------------------------------------------------------------------------------
# 메인 함수.
#--------------------------------------------------------------------------------
def Main(arguments : list) -> None:
	
	# 출력.
	builtins.print("__MAIN__")
	builtins.print("DDUK-SERVICES")

	# 데이터 매니저 설정.
	dataManager = Repository.Get(DataManager)
	manifestFilePath = dataManager.GetResPathWithRelativePath("manifest.json")
	
	# 매니페스트 로드.
	manifestParser = ManifestParser()
	manifestParser.Parse(manifestFilePath)

	# 서비스 매니저 시작.
	serviceManager = Repository.Get(ServiceManager)
	serviceManager.Run(manifestParser)

	# 서버 시작.
	networkManager = Repository.Get(NetworkManager)
	networkManager.Run(manifestParser.Host, manifestParser.Port)