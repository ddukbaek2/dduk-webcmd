#------------------------------------------------------------------------
# 참조 모듈 목록.
#------------------------------------------------------------------------
from __future__ import annotations
import builtins
import os
import sys
from pyappcore import Application, IsBuild, Launching


#------------------------------------------------------------------------
# 전역 상수 목록.
#------------------------------------------------------------------------
CURRENTFILEPATH : str = os.path.abspath(__file__)
SRCPATH : str = os.path.dirname(CURRENTFILEPATH).replace("\\", "/")
ROOTPATH : str = os.path.dirname(SRCPATH).replace("\\", "/")
STARTMODULENAME : str = "src.main"
STARTFUNCTIONNAME : str = "Main"


#------------------------------------------------------------------------
# 파일 진입점.
#------------------------------------------------------------------------
if __name__ == "__main__":
	try:
		Application.Log("__launcher__")
		Application.Log("__main__")
		# Application.Log(f"sys.argv: {sys.argv}")

		# 소스 패키지(루트폴더)를 모듈 검색 경로에 추가.
		if ROOTPATH and ROOTPATH not in sys.path: sys.path.append(ROOTPATH)
		# 소스 패키지의 서브 패키지(소스폴더)를 모듈 검색 경로에 추가.
		if SRCPATH and SRCPATH not in sys.path: sys.path.append(SRCPATH)
		import __pyappcore_dependencies_in_build__ #type: ignore

		# 실행.
		exitCode : int = Launching(STARTMODULENAME, STARTFUNCTIONNAME)
		sys.exit(exitCode)
	except Exception as exception:
		Application.LogException(exception)