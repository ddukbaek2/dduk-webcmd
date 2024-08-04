#------------------------------------------------------------------------
# 참조 모듈 목록.
#------------------------------------------------------------------------
from __future__ import annotations
import builtins
import os
from pyappcore import makecode, str_util, Application


#------------------------------------------------------------------------
# 전역 상수 목록.
#------------------------------------------------------------------------
BACKSLASH : str = "\\"
SLASH : str = "/"
CURRENTFILEPATH : str = os.path.abspath(__file__)
SRCPATH : str = os.path.dirname(CURRENTFILEPATH).replace(BACKSLASH, SLASH)
ROOTPATH : str = os.path.dirname(SRCPATH).replace(BACKSLASH, SLASH)


#------------------------------------------------------------------------
# 파일 진입점.
#------------------------------------------------------------------------
if __name__ == "__main__":
	try:
		builtins.print("__prebuild__")
		# 1. 바이너리 빌드시 VSCODE 상의 심볼을 읽을 수 있도록 코드 생성.
		vscodeSettings = makecode.GetVisualStudioCodeSettings(ROOTPATH)
		if vscodeSettings:
			symbolsString : str = vscodeSettings["pyappcore"]["build"]["symbols"]
			symbols : list[str] = str_util.GetStringFromSeperatedStringList(symbolsString, SLASH)
			makecode.CreateSymbolsInBuildToFile(symbols, SRCPATH)

		# 2. 바이너리 빌드시 pyinstaller에 포함시키기 위해 의존성이 있는 다른 소스 폴더 추가 및 저장.
		moduleNames = set()
		moduleNames.add("debugpy")
		makecode.CreateDependenciesInBuildToFile([SRCPATH], SRCPATH, moduleNames)
	except Exception as exception:
		Application.LogException(exception)