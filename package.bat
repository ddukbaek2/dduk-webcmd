@echo off
:: #------------------------------------------------------------------------
:: # 패키지 추가 설치. (Windows)
:: #------------------------------------------------------------------------
echo __PACKAGE_WINDOWS__

:: 독립 실행 방지.
if not defined IS_PACKAGE ( 
	echo This batch file cannot be executed.
	exit /b 1
)

:: BPY 라이브러리 다운로드.
if not exist "%BPYFILEPATH%" (
	echo "Not Exists '%BPYFILEPATH%'"
	curl -o "%BPYFILEPATH%" "%BPYFILEURL%"
)

:: MATHUTILS 라이브러리 다운로드.
if not exist "%MATHUTILSFILEPATH%" (
	echo "Not Exists '%MATHUTILSFILEPATH%'"
	curl -o "%MATHUTILSFILEPATH%" "%MATHUTILSFILEURL%"
)

:: BPY 라이브러리 설치.
python -m pip install "%BPYFILEPATH%" >nul 2>nul

:: MATHUTILS 라이브러리 설치.
python -m pip install "%MATHUTILSFILEPATH%" >nul 2>nul