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