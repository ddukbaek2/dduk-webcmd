#--------------------------------------------------------------------------------
# 참조 모듈 목록.
#--------------------------------------------------------------------------------
from __future__ import annotations
from typing import Any, Final, Optional, Type, TypeVar, Union, Tuple, List, Dict, Set, cast
import builtins
import os


#------------------------------------------------------------------------
# 전역 상수 목록.
#------------------------------------------------------------------------
BACKSLASH : str = "\\"
SLASH : str = "/"


#--------------------------------------------------------------------------------
# 데이터 매니저.
#--------------------------------------------------------------------------------
class DataManager:
	#--------------------------------------------------------------------------------
	# 멤버 변수 목록.
	#--------------------------------------------------------------------------------
	__rootPath : str
	__resPath : str


	#--------------------------------------------------------------------------------
	# 생성됨.
	#--------------------------------------------------------------------------------
	def __init__(self) -> None:
		self.__rootPath = str()
		self.__resPath = str()


	#--------------------------------------------------------------------------------
	# 루트 경로 설정.
	#--------------------------------------------------------------------------------
	def SetRootPath(self, rootPath : str) -> None:
		self.__rootPath = rootPath.replace(BACKSLASH, SLASH)
	

	#--------------------------------------------------------------------------------
	# 루트 경로 반환.
	#--------------------------------------------------------------------------------
	def GetRootPath(self) -> str:
		return self.__rootPath
	

	#--------------------------------------------------------------------------------
	# 리소스 경로 설정.
	#--------------------------------------------------------------------------------
	def SetResPath(self, resPath : str) -> None:
		self.__resPath = resPath.replace(BACKSLASH, SLASH)
	

	#--------------------------------------------------------------------------------
	# 리소스 경로 반환.
	#--------------------------------------------------------------------------------
	def GetResPath(self) -> str:
		return self.__resPath
	

	#--------------------------------------------------------------------------------
	# 루트 경로를 기반으로 상대경로를 추가하여 반환.
	#--------------------------------------------------------------------------------
	def GetRootPathWithRelativePath(self, relativePath : str) -> str:
		rootPath = self.GetRootPath()
		if not os.path.isdir(rootPath): os.makedirs(rootPath)
		if not relativePath:
			return rootPath
		relativePath = relativePath.replace(BACKSLASH, SLASH)
		absolutePath = f"{rootPath}/{relativePath}"
		return absolutePath		
	

	#--------------------------------------------------------------------------------
	# 리소스 경로를 기반으로 상대경로를 추가하여 반환.
	#--------------------------------------------------------------------------------
	def GetResPathWithRelativePath(self, relativePath : str) -> str:
		resPath = self.GetResPath()
		if not os.path.isdir(resPath): os.makedirs(resPath)
		if not relativePath:
			return resPath
		relativePath = relativePath.replace(BACKSLASH, SLASH)
		absolutePath = f"{resPath}/{relativePath}"
		return absolutePath		