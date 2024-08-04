@echo off
chcp 65001 >nul
::------------------------------------------------------------------------
:: 서비스 관련 통합 배치 파일. (Windows 전용)
::------------------------------------------------------------------------
echo __SERVICE_WINDOWS__

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
	set TEXT=Usage: %EXECUTEFILENAME% {dev^|test^|live}
	echo !TEXT!
	set TEXT=service dev: 데브 서비스 실행
	echo !TEXT!
	set TEXT=service test: 테스트 서비스 실행
	echo !TEXT!
	set TEXT=service live: 라이브 서비스 실행
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
:: 서비스 - 데브.
::--------------------------------------------------------------------------------
:dev
	echo __SERVICE_DEV_WINDOWS__

	:: 가상환경 생성 ==> 활성화 ==> 업데이트.
	call "venv.bat" update

	:: 빌드 전 처리 실행.
	:: python "%SOURCEPATH%\__prebuilder__.py"

	:: 런처 실행.
	:: python "%SOURCEPATH%\__launcher__.py" "SERVICE/NODEBUG/LOG" "live"
	python "%SOURCEPATH%\__launcher__.py"
exit /b 0


::--------------------------------------------------------------------------------
:: 서비스 - 테스트.
::--------------------------------------------------------------------------------
:test
	echo __SERVICE_TEST_WINDOWS__

	:: 가상환경 생성 ==> 활성화 ==> 업데이트.
	call "venv.bat" update

	:: 빌드 전 처리 실행.
	:: python "%SOURCEPATH%\__prebuilder__.py"

	:: 런처 실행.
	:: python "%SOURCEPATH%\__launcher__.py" "SERVICE/NODEBUG/LOG" "test"
	python "%SOURCEPATH%\__launcher__.py"
exit /b 0


::--------------------------------------------------------------------------------
:: 서비스 - 라이브.
::--------------------------------------------------------------------------------
:live
	echo __SERVICE_LIVE_WINDOWS__

	:: 가상환경 생성 ==> 활성화 ==> 업데이트.
	call "venv.bat" update

	:: 빌드 전 처리 실행.
	:: python "%SOURCEPATH%\__prebuilder__.py"

	:: 런처 실행.
	:: python "%SOURCEPATH%\__launcher__.py" "SERVICE/NODEBUG/LOG" "live"
	python "%SOURCEPATH%\__launcher__.py"
exit /b 0