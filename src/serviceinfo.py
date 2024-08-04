#--------------------------------------------------------------------------------
# 참조 모듈 목록.
#--------------------------------------------------------------------------------
from __future__ import annotations
from typing import Any, Final, Optional, Type, TypeVar, Union, Tuple, List, Dict, Set, cast
import builtins
import os
import subprocess
from threading import Thread
from enum import Enum, auto


#--------------------------------------------------------------------------------
# 서비스 상태.
#--------------------------------------------------------------------------------
class ServiceState(Enum):
	STOP = auto()
	START = auto()


#--------------------------------------------------------------------------------
# 서비스 정보.
#--------------------------------------------------------------------------------
class ServiceInfo:
	#--------------------------------------------------------------------------------
	# 멤버 변수 목록.
	#--------------------------------------------------------------------------------
	ID : int
	Name : str
	FilePath : str
	State : ServiceState
	Process : subprocess.Popen
	Thread : Thread


	#--------------------------------------------------------------------------------
	# 생성됨.
	#--------------------------------------------------------------------------------
	def __init__(self) -> None:
		self.ID = int()
		self.Name = str()
		self.FilePath = str()
		self.State = ServiceState.STOP
		self.Process = None
		self.Thread = None
