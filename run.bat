@echo off
chcp 65001 >nul
::------------------------------------------------------------------------
:: 콘솔 실행 관련 통합 배치 파일. (Windows 전용)
:: - 일관적으로 사용하기 위해 가상 환경 관련 기능까지 포함 되어있음.
::------------------------------------------------------------------------
echo __RUN_WINDOWS__

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

:: 매개 변수 전역 설정.
set INDEX=0
for %%A in (%0 %*) do (
	call set ARGUMENT_%%INDEX%%=%%A
	call set /a INDEX=%%INDEX%%+1
)

:: 입력된 레이블이 없을 경우.
if "%COMMAND%" == "" (
	:: 레이블 설명 출력.
	setlocal enabledelayedexpansion
	set TEXT=Usage: %EXECUTEFILENAME% {venv^|build^|prebuild^|source^|service^|tests}
	echo !TEXT!
	set TEXT=run venv: 가상 환경 관련 명령
	echo !TEXT!
	set TEXT=run build: 빌드 관련 명령
	echo !TEXT!
	set TEXT=run prebuild: 소스 전에 선작업 관련 명령
	echo !TEXT!
	set TEXT=run source: 소스 관련 명령
	echo !TEXT!
	set TEXT=run service: 서비스 관련 명령
	echo !TEXT!
	set TEXT=tests: 단위테스트 관련 명령
	echo !TEXT!
	endlocal
	exit /b 1
) else (
	:: 레이블 실행.
	call :%COMMAND%
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
:: 가상 환경 관련 명령.
::--------------------------------------------------------------------------------
:venv
	echo __RUN_VENV_WINDOWS__

	:: 변수 설정.
	set VENV_COMMAND=%ARGUMENT_2%

	:: 가상환경 명령.
	call "venv.bat" %VENV_COMMAND%

	:: 오류가 있으면 실패.
	if not %errorlevel% equ 0 ( exit /b 1 )
exit /b 0


::--------------------------------------------------------------------------------
:: 빌드 관련 명령.
::--------------------------------------------------------------------------------
:build
	echo __RUN_BUILD_WINDOWS__

	:: 변수 설정.
	set BUILD_COMMAND=%ARGUMENT_2%

	:: 가상환경 생성 ==> 활성화 ==> 업데이트.
	call "venv.bat" update

	:: 빌드 전 처리 실행.
	python "%SOURCEPATH%\__prebuilder__.py"

	:: 빌드 생성.
	set BUILD=python -m PyInstaller ^
	-F --clean^
	--paths="%SOURCEPATH%" ^
	--paths="%RESPATH%" ^
	--add-data "%SOURCEPATH%\**;src" ^
	--add-data "%RESPATH%;res" ^
	--distpath "%BUILDBINPATH%" ^
	--specpath "%BUILDSPECPATH%" ^
	--workpath "%BUILDWORKPATH%" ^
	--name %BUILDNAME% ^
	--additional-hooks-dir="%HOOKSPATH%" ^
	--onefile "%SOURCEPATH%\__launcher__.py"

	:: 콘솔창 설정.
	if "%BUILD_NOCONSOLE%" == "true" (
		echo "NOCONSOLE"
		set BUILD=%BUILD% --noconsole
	)

	:: 빌드 실행.
	%BUILD%

exit /b 0


::--------------------------------------------------------------------------------
:: 빌드 전 처리 관련 명령.
::--------------------------------------------------------------------------------
:prebuild
	echo __RUN_PREBUILD_WINDOWS__

	:: 가상환경 생성 ==> 활성화 ==> 업데이트.
	call "venv.bat" update

	:: 빌드 전 처리 실행.
	python "%SOURCEPATH%\__prebuilder__.py"
exit /b 0


::--------------------------------------------------------------------------------
:: 소스 관련 명령.
::--------------------------------------------------------------------------------
:source
	echo __RUN_SOURCE_WINDOWS__

	:: 변수 설정.
	set SOURCE_SYMBOLS=%ARGUMENT_2%
	set SOURCE_ARGUMENTS=%ARGUMENT_3%

	:: 가상환경 생성 ==> 활성화 ==> 업데이트.
	call "venv.bat" update

	:: 빌드 전 처리 실행.
	:: python "%SOURCEPATH%\__prebuilder__.py"

	:: 변수 출력.
	:: echo SOURCE_SYMBOLS: %SOURCE_SYMBOLS%
	:: echo SOURCE_ARGUMENTS: %SOURCE_ARGUMENTS%

	:: 런처 실행.
	:: python "%SOURCEPATH%\__launcher__.py" "%SOURCE_SYMBOLS%" "%SOURCE_ARGUMENTS%"

exit /b 0


::--------------------------------------------------------------------------------
:: 서비스 관련 명령.
::--------------------------------------------------------------------------------
:service
	echo __RUN_SERVICE_WINDOWS__

	:: 변수 설정.
	set SERVICE_COMMAND=%ARGUMENT_2%

	:: 서비스 명령.
	call "service.bat" %SERVICE_COMMAND%

	:: 오류가 있으면 실패.
	if not %errorlevel% equ 0 ( exit /b 1 )
exit /b 0


::--------------------------------------------------------------------------------
:: 단위 테스트 관련 명령.
::--------------------------------------------------------------------------------
:tests
	echo __RUN_TESTS_WINDOWS__
	
	:: 단위 테스트 실행.
	python "%TESTSPATH%\__main__.py"
exit /b 0