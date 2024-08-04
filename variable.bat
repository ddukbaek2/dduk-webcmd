@echo off
::------------------------------------------------------------------------
:: 설정 변수 목록. (Windows)
::------------------------------------------------------------------------
echo __VARIABLE_WINDOWS__

:: 독립 실행 방지.
if not defined IS_VARIABLE (
	echo This batch file cannot be executed.
	exit /b 1
)

:: 파이썬 인터프리터 경로.
set PYTHONFILEPATH=C:\Program Files\Python312\python.exe

:: 빌드 이름.
set BUILDNAME=dduk-webcmd

:: 빌드 파일 경로. 
set BUILDFILEPATH=%BUILDBINPATH%\%BUILDNAME%.exe

:: 빌드시 CLI 감추기 여부 설정.
set BUILD_NOCONSOLE=false