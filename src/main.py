#--------------------------------------------------------------------------------
# 참조 모듈 목록.
#--------------------------------------------------------------------------------
from __future__ import annotations
from typing import Any, Final, Optional, Type, TypeVar, Union, List, Dict, Set, cast
import builtins
from pyappcore import Application
import service
import validator
import sys


#--------------------------------------------------------------------------------
# 전역 상수 목록.
#--------------------------------------------------------------------------------
SERVICE : str = "SERVICE"


#--------------------------------------------------------------------------------
# 진입점.
# - 서비스(dev, test, live), 메타버스종류, 카테고리, FBX파일 경로.
#--------------------------------------------------------------------------------
def Main(arguments : list) -> int:
	# 프로젝트 이름 및 입력값.
	Application.Log("ConversionModelValidator")
	Application.Log(f"arguments: {arguments}")

	# 설정 파일 불러오기.
	configuration : dict = Application.GetConfiguration()
	if not configuration:
		Application.LogError("not found 'res/configuration.json'")
		return 1

	# 서비스 모드.
	if Application.HasSymbol(SERVICE): return service.Main(arguments)
 
	# 디버그 일 때.
	# 외부에서 받은 아규먼트 깡그리 다 무시하고 내부에서 아규먼트 구축.
	if not Application.IsBuild() and Application.IsDebug():
		fbxFilePath = Application.GetWorkspacePathWithRelativePath("test.fbx")
		arguments.clear()
		arguments.append("dev")
		arguments.append("altava")
		arguments.append("top")
		arguments.append(fbxFilePath)
		sys.argv = arguments

	try:
		return validator.Main(arguments)
	except Exception as exception:
		Application.LogException(exception)