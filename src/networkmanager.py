#--------------------------------------------------------------------------------
# 참조 모듈 목록.
#--------------------------------------------------------------------------------
from __future__ import annotations
from typing import Any, Final, Optional, Type, TypeVar, Union, Tuple, List, Dict, Set, cast
import builtins
import os
import subprocess
import sys
from http import HTTPStatus
from flask import Flask, request, jsonify, make_response, redirect, url_for, render_template
from dduk.core import Repository
from src.datamanager import DataManager
from src.serviceinfo import ServiceInfo, ServiceState
from src.servicemanager import ServiceManager


#--------------------------------------------------------------------------------
# 네트워크 매니저.
#--------------------------------------------------------------------------------
class NetworkManager:
	#--------------------------------------------------------------------------------
	# 멤버 변수 목록.
	#--------------------------------------------------------------------------------
	__app : Flask


	#--------------------------------------------------------------------------------
	# 생성됨.
	#--------------------------------------------------------------------------------
	def __init__(self) -> None:
		
		# 데이터 매니저 설정.
		dataManager = Repository.Get(DataManager)
		templatesPath = dataManager.GetResPathWithRelativePath("templates")

		self.__app = Flask("DDUK-SERVICES", template_folder = templatesPath)
		self.__app.add_url_rule("/", "MainDocument", self.VoidDocument, methods = ["GET"])
		self.__app.add_url_rule("/execute", "Execute", self.Execute, methods = ["POST"])
		self.__app.add_url_rule("/restart", "RestartService", self.RestartService, methods = ["GET"])
		self.__app.add_url_rule("/start", "StartService", self.StartService, methods = ["GET"])
		self.__app.add_url_rule("/stop", "StopService", self.StopService, methods = ["GET"])
		self.__app.add_url_rule("/status", "StatusService", self.StatusService, methods = ["GET"])
		self.__app.add_url_rule("/list", "ListServices", self.ListServices, methods = ["GET"])	


	#--------------------------------------------------------------------------------
	# 서버 시작.
	#--------------------------------------------------------------------------------
	def Run(self, host : str = "0.0.0.0", port : int = 5000) -> None:
		self.__app.run(host = host, port = port)


	#--------------------------------------------------------------------------------
	# 빈 화면.
	#--------------------------------------------------------------------------------
	def VoidDocument(self) -> Union[str, Tuple[str, int]]:
		# return redirect(url_for("ViewDocument"))
		return render_template("index.html", output = None)


	#--------------------------------------------------------------------------------
	# 실행.
	#--------------------------------------------------------------------------------
	def Execute(self) -> Union[str, Tuple[str, int]]:
		command = request.json.get("command") # request.form["command"]
		result = str()
		try:
			process = subprocess.Popen([command], stdout = subprocess.PIPE, stderr = subprocess.PIPE, text = True)
			result = process.stdout + process.stderr
		except Exception as exception:
			result = str(exception)

		# return render_template("index.html", output = result)
		return jsonify({ "output" : result })


	#--------------------------------------------------------------------------------
	# 서비스 재시작.
	#--------------------------------------------------------------------------------
	def RestartService(self) -> Union[str, Tuple[str, int]]:
		try:
			serviceName = request.args.get("SERVICENAME")
			serviceManager = Repository.Get(ServiceManager)
			serviceInfo = serviceManager.FindService(serviceName)
			if serviceInfo:
				if serviceInfo.State == ServiceState.START: serviceManager.StopService(serviceName)
				serviceManager.StartService(serviceName)
				return "Service started successfully", HTTPStatus.OK
			else:
				return "Service not found", HTTPStatus.NOT_FOUND
		except Exception as exception:
			return exception, HTTPStatus.INTERNAL_SERVER_ERROR


	#--------------------------------------------------------------------------------
	# 서비스 시작.
	#--------------------------------------------------------------------------------
	def StartService(self) -> Union[str, Tuple[str, int]]:
		try:
			serviceName = request.args.get("SERVICENAME")
			serviceManager = Repository.Get(ServiceManager)
			serviceInfo = serviceManager.FindService(serviceName)
			if serviceInfo:
				if serviceInfo.State == ServiceState.STOP:
					serviceManager.StartService(serviceName)
					return "Service started successfully", HTTPStatus.OK
				else:
					return "Service is already running.", HTTPStatus.BAD_REQUEST
			else:
				return "Service not found", HTTPStatus.NOT_FOUND
		except Exception as exception:
			return exception, HTTPStatus.INTERNAL_SERVER_ERROR


	#--------------------------------------------------------------------------------
	# 서비스 정지.
	#--------------------------------------------------------------------------------
	def StopService(self) -> Union[str, Tuple[str, int]]:
		try:
			serviceName = request.args.get("SERVICENAME")
			serviceManager = Repository.Get(ServiceManager)
			serviceInfo = serviceManager.FindService(serviceName)
			if serviceInfo:
				if serviceInfo.State == ServiceState.START:
					serviceManager.StopService(serviceName)
					return "Service stop successfully", HTTPStatus.OK
				else:
					return "Service is not running.", HTTPStatus.BAD_REQUEST
			else:
				return "Service not found", HTTPStatus.NOT_FOUND

		except Exception as exception:
			return exception, HTTPStatus.INTERNAL_SERVER_ERROR


	#--------------------------------------------------------------------------------
	# 서비스 상태 확인.
	#--------------------------------------------------------------------------------
	def StatusService(self) -> Union[str, Tuple[str, int]]:
		try:
			serviceName = request.args.get("SERVICENAME")
			serviceManager = Repository.Get(ServiceManager)
			serviceInfo = serviceManager.FindService(serviceName)
			if serviceInfo:
				return jsonify(serviceInfo)
			else:
				return "Service not found.", HTTPStatus.NOT_FOUND
		except Exception as exception:
			return exception, HTTPStatus.INTERNAL_SERVER_ERROR


	#--------------------------------------------------------------------------------
	# 서비스 목록 확인.
	#--------------------------------------------------------------------------------
	def ListServices(self) -> Union[str, Tuple[str, int]]:
		try:
			serviceManager = Repository.Get(ServiceManager)
			return jsonify(serviceManager.GetAllServices())
		except Exception as exception:
			return exception, HTTPStatus.INTERNAL_SERVER_ERROR