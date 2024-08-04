#------------------------------------------------------------------------
# 참조 모듈 목록.
#------------------------------------------------------------------------
from __future__ import annotations
from typing import Any, Final, Optional, Type, TypeVar, Union, List, Dict, cast
import builtins
import os
import platform
from dduk.process.processinfo import ProcessInfo
from dduk.process.processmanager import ProcessManager


#------------------------------------------------------------------------
# 전역 상수 목록.
#------------------------------------------------------------------------
BACKSLASH : str = "\\"
SLASH : str = "/"
CURRENTFILEPATH : str = os.path.abspath(__file__)
SRCPATH : str = os.path.dirname(CURRENTFILEPATH).replace(BACKSLASH, SLASH)
ROOTPATH : str = os.path.dirname(SRCPATH).replace(BACKSLASH, SLASH)


#------------------------------------------------------------------------
# 프로세스 강제 종료.
#------------------------------------------------------------------------
def Kill():
	processName : str = str()
	systemName : str = platform.system().upper()
	if systemName == "WINDOWS":
		processName = "python.exe"
	elif systemName == "DARWIN":
		processName = "python3"
	elif systemName == "LINUX":
		processName = "python3"
	else:
		return

	# 프로젝트 루트 경로의 하위 경로에서 실행되는 파이썬 인터프리터의 프로세스 제거.
	processManager = ProcessManager()
	processInfos : dict[int, ProcessInfo] = processManager.FindProcessInfosByName(processName)
	rootPath = ROOTPATH.upper()
	builtins.print(f"rootPath={rootPath}")
	for processID, processInfo in processInfos.items():
		processInfo = cast(ProcessInfo, processInfo)
		filePath = processInfo.FilePath.replace(BACKSLASH, SLASH).upper()
		if rootPath in filePath:
			builtins.print(f"processID={processID}, FilePath={filePath}")
			try:
				if processManager.DestroyProcessByID(processInfo.ID, 0.0):
					builtins.print(f"Process Kill: {processInfo.ID}")
				else:
					builtins.print(f"Process Kill Failed: {processInfo.ID}")
			except Exception as exception:
				builtins.print(f"Process Kill Exception: {processInfo.ID}, exception={exception}")

#------------------------------------------------------------------------
# 파일 진입점.
#------------------------------------------------------------------------
if __name__ == "__main__":
	Kill()