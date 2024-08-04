#--------------------------------------------------------------------------------
# 참조 모듈 목록.
#--------------------------------------------------------------------------------
from __future__ import annotations
from typing import Final, Optional, Type, TypeVar, Union, Tuple, Callable, Any, List, Dict, Set, cast
import builtins
import os
import subprocess
import sys
from threading import Thread
from src.manifestparser import ManifestParser
from src.serviceinfo import ServiceInfo, ServiceState



#--------------------------------------------------------------------------------
# 서비스 정보.
#--------------------------------------------------------------------------------
class ServiceManager:
	#--------------------------------------------------------------------------------
	# 멤버 변수 목록.
	#--------------------------------------------------------------------------------
	__serviceInfos : dict[str, ServiceInfo] # Name, ServiceInfo


	#--------------------------------------------------------------------------------
	# 생성됨.
	#--------------------------------------------------------------------------------
	def __init__(self) -> None:
		self.__serviceInfos = dict()


	#--------------------------------------------------------------------------------
	# 서비스 매니저 시작.
	#--------------------------------------------------------------------------------
	def Run(self, manifestParser : ManifestParser) -> bool:
		for name, executablePath in manifestParser.Services.items():
			name = name.upper()
			serviceInfo = ServiceInfo()
			serviceInfo.ID = 1
			serviceInfo.Name = name
			serviceInfo.FilePath = executablePath
			self.__serviceInfos[name] = serviceInfo
		return True


	#--------------------------------------------------------------------------------
	# 서비스 동작 중.
	#--------------------------------------------------------------------------------
	def __OnTaskService(self, serviceInfo : ServiceInfo) -> None:
		try:
			command : str = serviceInfo.FilePath

			# 신규 프로세스 시작.
			serviceInfo.State = ServiceState.START
			serviceInfo.Process = subprocess.Popen(command, stdout = subprocess.PIPE, stderr = subprocess.PIPE, text = True)
	
			# 종료 대기.
			stdout, stderr = serviceInfo.Process.communicate()
			exitcode = serviceInfo.Process.returncode

			# 종료시 업데이트.
			serviceInfo.State = ServiceState.STOP
			serviceInfo.Process = None
			serviceInfo.Thread = None
		except Exception as exception:
			# 예외로 인한 종료시 업데이트.
			serviceInfo.State = ServiceState.STOP
			serviceInfo.Process = None
			serviceInfo.Thread = None


	#--------------------------------------------------------------------------------
	# 서비스 시작.
	#--------------------------------------------------------------------------------
	def StartService(self, serviceName : str) -> False:
		serviceInfo = self.FindService(serviceName)
		if not serviceInfo:
			return False
		if serviceInfo.State == ServiceState.START:
			self.StopService(serviceName)

		# 신규 쓰레드 생성.
		serviceInfo.Thread = Thread(target = self.__OnTaskService, args = tuple([serviceInfo]))
		serviceInfo.Thread.start()


	#--------------------------------------------------------------------------------
	# 서비스 중지.
	#--------------------------------------------------------------------------------
	def StopService(self, serviceName : str) -> bool:
		serviceInfo = self.FindService(serviceName)
		if not serviceInfo:
			return False
		if serviceInfo.State == ServiceState.STOP:
			return False
		
		# 강제 종료.
		if serviceInfo.Process: serviceInfo.Process.kill()		
		if serviceInfo.Thread: serviceInfo.Thread.join()

		# 값 초기화.
		serviceInfo.State = ServiceState.STOP
		serviceInfo.Process = None
		serviceInfo.Thread = None
		
		return True


	#--------------------------------------------------------------------------------
	# 서비스가 동작 중인지 여부.
	#--------------------------------------------------------------------------------
	def IsStartedService(self, serviceName : str) -> bool:
		serviceInfo = self.FindService(serviceName)
		if not serviceInfo:
			return False
		return serviceInfo.State == ServiceState.START
	

	#--------------------------------------------------------------------------------
	# 서비스 이름으로 서비스를 찾아 반환.
	#--------------------------------------------------------------------------------
	def FindService(self, serviceName : str) -> Union[ServiceInfo, None]:
		serviceName = serviceName.upper()
		return self.__serviceInfos.get(serviceName, None)


	#--------------------------------------------------------------------------------
	# 모든 서비스 반환.
	#--------------------------------------------------------------------------------
	def GetAllServices(self) -> list[ServiceInfo]:
		return list(self.__serviceInfos.values())