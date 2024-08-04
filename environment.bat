@echo off
:: #------------------------------------------------------------------------
:: # 환경 변수 목록. (Windows)
:: #------------------------------------------------------------------------
echo __ENVIRONMENT_WINDOWS__

:: 독립 실행 방지.
if not defined IS_ENVIRONMENT (
	echo This batch file cannot be executed.
	exit /b 1
)

:: 프로젝트 경로 설정.
set PROJECTPATH=%~dp0
set PROJECTPATH=%PROJECTPATH:~0,-1%
for /f "tokens=1 delims=:" %%a in ("%PROJECTPATH%") do set "PROJECTDRIVE=%%a:"

:: 가상 환경 관련 경로 설정.
set VENVNAME=.venv
set VENVPATH=%PROJECTPATH%\.venv
set VENVPYTHONPATH=%VENVPATH%\Scripts
set VENVSITEPACKAGESPATH=%VENVPATH%\Lib\site-packages
set VENVPYTHONFILEPATH=%VENVPYTHONPATH%\python.exe

:: 프로젝트 세부 경로 설정.
set VSCODENAME=.vscode
set VSCODEPATH=%PROJECTPATH%\.vscode
set BUILDPATH=%PROJECTPATH%\build
set BUILDBINPATH=%BUILDPATH%\bin
set BUILDSPECPATH=%BUILDPATH%\spec
set BUILDWORKPATH=%BUILDPATH%\work
set HINTSPATH=%PROJECTPATH%\hints
set HOOKSPATH=%PROJECTPATH%\hooks
set LIBSPATH=%PROJECTPATH%\libs
set LOGSPATH=%PROJECTPATH%\logs
set RESPATH=%PROJECTPATH%\res
set SOURCEPATH=%PROJECTPATH%\src
set TESTSPATH=%PROJECTPATH%\tests
set WORKSPACEPATH=%PROJECTPATH%\workspace