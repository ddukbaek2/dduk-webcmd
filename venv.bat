@echo off
chcp 65001 >nul
::------------------------------------------------------------------------
:: 가상 환경 관련 통합 배치 파일. (Windows 전용)
::------------------------------------------------------------------------
echo __VENV_WINDOWS__

:: 환경 변수 목록 불러오기.
set IS_ENVIRONMENT=1
call "environment.bat"
set IS_ENVIRONMENT=

:: 설정 변수 목록 불러오기.
set IS_VARIABLE=1
call "variable.bat"
set IS_VARIABLE=

:: 변수 설정.
set EXECUTEFILENAME=%0
set COMMAND=%1
set TEXT=

:: 입력된 레이블이 없을 경우.
if "%COMMAND%" == "" (
	:: 레이블 설명 출력.
	setlocal enabledelayedexpansion
	set TEXT=Usage: %EXECUTEFILENAME% {create^|destroy^|enable^|disable^|update}
	echo !TEXT!
	set TEXT=venv create: 가상 환경 생성
	echo !TEXT!
	set TEXT=venv enable: 가상 환경 활성화
	echo !TEXT!
	set TEXT=venv update: 가상 환경 패키지 신규 설치 혹은 설치된 패키지 업데이트
	echo !TEXT!
	set TEXT=venv disable: 가상 환경 비활성화
	echo !TEXT!
	set TEXT=venv destroy: 가상환경 제거
	echo !TEXT!
	endlocal
	exit /b 0
) else (
	:: 레이블 실행.
	call :%1
)

:: 레이블을 실행한 뒤 오류 갯수 검사.
if %errorlevel% equ 0 (
	:: 레이블이 성공적으로 종료 되었으면 성공.
	exit /b 0
) else (
	:: 레이블이 성공적으로 종료되지 못했다면 실패.
	setlocal enabledelayedexpansion
	set TEXT=명령어: %COMMAND%, 오류: %errorlevel%
	echo !TEXT!
	endlocal
	exit /b 1
)


::--------------------------------------------------------------------------------
:: 가상 환경 생성.
:: - 기존 가상 환경이 활성화 되어있으면 비활성화.
:: - 기존 가상 환경이 존재하면 제거.
:: - 가상 환경이 없으면 새로운 가상 환경 생성.
:: - 가상 환경이 활성화 되어있지 않으면 활성화. 
::--------------------------------------------------------------------------------
:create
	echo __VENV_CREATE_WINDOWS__
	if defined VIRTUAL_ENV ( .venv\Scripts\deactivate.bat )
	if exist "%VENVPATH%" (  rmdir /s /q "%VENVPATH%" )
	if not exist "%VENVPATH%" ( "%PYTHONFILEPATH%" -m venv "%VENVPATH%" )
	if not defined VIRTUAL_ENV ( .venv\Scripts\activate.bat )
exit /b 0


::--------------------------------------------------------------------------------
:: 가상 환경 제거.
:: - 기존 가상 환경이 활성화 되어있으면 비활성화.
:: - 기존 가상 환경이 존재하면 제거.
::--------------------------------------------------------------------------------
:destroy
	echo __VENV_DESTROY_WINDOWS__
	if defined VIRTUAL_ENV ( .venv\Scripts\deactivate.bat )
	if exist "%VENVPATH%" ( rmdir /s /q "%VENVPATH%" )
exit /b 0


::--------------------------------------------------------------------------------
:: 가상 환경 활성화.
:: - 가상 환경이 없으면 새로운 가상 환경 생성.
:: - 가상 환경이 활성화 되어있지 않으면 활성화. 
::--------------------------------------------------------------------------------
:enable
	echo __VENV_ENABLE_WINDOWS__
	if not exist "%VENVPATH%" ( "%PYTHONFILEPATH%" -m venv "%VENVPATH%" )
	if not defined VIRTUAL_ENV ( .venv\Scripts\activate.bat )
exit /b 0


::--------------------------------------------------------------------------------
:: 가상 환경 비활성화.
:: - 가상 환경이 존재하며 활성화 되어있을 때 비활성화.
::--------------------------------------------------------------------------------
:disable
	echo __VENV_DISABLE_WINDOWS__
	if exist "%VENVPATH%" if defined VIRTUAL_ENV ( .venv\Scripts\deactivate.bat )
exit /b 0


::--------------------------------------------------------------------------------
:: 가상 환경 패키지 업데이트.
:: - 업데이트 전 가상 환경이 없으면 생성.
:: - 업데이트 전 가상 환경이 활성화 되어있지 않으면 활성화.
::--------------------------------------------------------------------------------
:update
	echo __VENV_UPDATE_WINDOWS__
	if not exist "%VENVPATH%" ( "%PYTHONFILEPATH%" -m venv "%VENVPATH%" )
	if not defined VIRTUAL_ENV ( .venv\Scripts\activate.bat )

	:: 패키지 설치용 파일 경로 설정.
	set REQUIREMENTSFILEPATH=%PROJECTPATH%\requirements.txt

	:: 패키지 설치.
	python --version
	python -m ensurepip --upgrade >nul 2>nul
	python -m pip install --upgrade pip >nul 2>nul
	python -m pip install --upgrade -r "%REQUIREMENTSFILEPATH%" >nul 2>nul

	:: 패키지 추가 설치.
	set IS_PACKAGE=1
	call "package.bat"
	set IS_PACKAGE=

	:: 현재 가상 환경에 설치된 모든 패키지 확인.
	python --version
	python -m pip list
exit /b 0