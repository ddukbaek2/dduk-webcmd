#--------------------------------------------------------------------------------
# 참조 모듈 목록.
#--------------------------------------------------------------------------------
from __future__ import annotations
from typing import Any, Final, Optional, Type, TypeVar, Union, Tuple, List, Dict, Set, cast
import builtins
import os
import sys
from dduk.core import Repository


#------------------------------------------------------------------------
# 전역 상수 목록.
#------------------------------------------------------------------------
BACKSLASH : str = "\\"
SLASH : str = "/"
CURRENTFILEPATH : str = os.path.abspath(__file__)
SRCPATH : str = os.path.dirname(CURRENTFILEPATH).replace(BACKSLASH, SLASH)
ROOTPATH : str = os.path.dirname(SRCPATH).replace(BACKSLASH, SLASH)


#--------------------------------------------------------------------------------
# 파일 진입점.
#--------------------------------------------------------------------------------
if __name__ == "__main__":
	# 코드 추가.
	if ROOTPATH and ROOTPATH not in sys.path: sys.path.append(ROOTPATH)
	if SRCPATH and SRCPATH not in sys.path: sys.path.append(SRCPATH)

	# 출력.
	builtins.print("__LAUNCHER__")

	# 변수 설정.
	from src.datamanager import DataManager
	dataManager = Repository.Get(DataManager)
	dataManager.SetRootPath(ROOTPATH)
	dataManager.SetResPath(f"{ROOTPATH}/res")

	# 시작.
	from src.__main__ import Main
	Main(sys.argv)
