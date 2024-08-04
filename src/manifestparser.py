#--------------------------------------------------------------------------------
# 참조 모듈 목록.
#--------------------------------------------------------------------------------
from __future__ import annotations
from typing import Final, Optional, Type, TypeVar, Union, Tuple, Callable, Any, List, Dict, Set, cast
import builtins
import json
import os


#--------------------------------------------------------------------------------
# 전역 상수 목록.
#--------------------------------------------------------------------------------
DEFAULT_HOST : str = "0.0.0.0"
DEFAULT_PORT : int = 5000
READ : str = "r"
UTF8 : str = "utf-8"
HOST : str = "host"
PORT : str = "port"
SERVER : str = "server"
SERVICES : str = "services"
NAME : str = "name"
EXECUTABLEPATH : str = "executablePath"


#--------------------------------------------------------------------------------
# 매니페스트 해석기.
#--------------------------------------------------------------------------------
class ManifestParser:
	#--------------------------------------------------------------------------------
	# 멤버 변수 목록.
	#--------------------------------------------------------------------------------
	Host : str
	Port : int
	Services : dict[str, str] # name, path


	#--------------------------------------------------------------------------------
	# 생성됨.
	#--------------------------------------------------------------------------------
	def __init__(self) -> None:
		self.Host = DEFAULT_HOST
		self.Port = DEFAULT_PORT
		self.Services = dict()


	#--------------------------------------------------------------------------------
	# 해석.
	#--------------------------------------------------------------------------------
	def Parse(self, manifestFilePath : str) -> bool:
		try:
			if not os.path.isfile(manifestFilePath):
				return False
			
			with open(manifestFilePath, READ, encoding = UTF8) as file:
				jsonManifestData : dict = json.load(file)
				if not jsonManifestData:
					return False
				
				if SERVER in jsonManifestData:
					builtins.print(SERVER)
					jsonServerData : dict = jsonManifestData.get(SERVER, {HOST : DEFAULT_HOST, PORT : DEFAULT_PORT })
					self.Host = jsonServerData.get(HOST, DEFAULT_HOST)
					self.Port = jsonServerData.get(PORT, DEFAULT_PORT)

				if SERVICES in jsonManifestData:
					builtins.print(SERVICES)
					jsonServicesData : list = jsonManifestData.get(SERVICES, list())
					for jsonServiceData in jsonServicesData:
						jsonServiceData = cast(dict, jsonServiceData)
						serviceName = jsonServiceData.get(NAME, str())
						serviceExecutablePath = jsonServiceData.get(EXECUTABLEPATH, str())
						self.Services[serviceName] = serviceExecutablePath
			builtins.print(self.Services)
			return True		
		except Exception as exception:
			builtins.print(exception)
			return False