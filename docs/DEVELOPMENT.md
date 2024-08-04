# 컨버전 모델검수서버 개발 가이드


## 개요
개발 관련 정리   


## 개발을 위한 설치 및 실행 (Windows)
1. VC_redist x64 재배포 패키지 (2015~2022) 설치. (bpy 윈도우 버전에 필요)   
2. Blender 4.0.2을(를) 기본 설치 위치로 지정하여 설치.   
3. Fork 기본 설치 위치로 지정하여 설치.   
4. 모델 검수 서버 프로젝트의 깃 레포지토리 다운로드 받기.   
5. 다운로드 받은 프로젝트 폴더에 .env 환경 변수 파일 넣기. (보안 상 별도 관리 대상)   
6. VS Code 1.19.1을(를) System Installer 로 설치.   
7. VS Code "Python" 확장 플러그인 설치.   
8. VS Code 로 다운로드 받은 프로젝트 열기.   
9. VS Code에 새로운 터미널을 열어서 다음과 같이 실행. (윈도우 프롬프트)   
```batch
run venv update
```
10. 코딩 작업 시작.   


## 작업 후 실행 방법
> VSCode 좌측 메뉴 > 실행 및 디버그 > No Debug 선택 상태 ==> 상단 메뉴 > 실행 > 디버깅 없이 실행 (CTRL + F5)   
> VSCode 좌측 메뉴 > 실행 및 디버그 > Debug 선택 상태 ==> 상단 메뉴 > 실행 > 디버깅 시작 (F5)   
> VSCode 상단 메뉴 > 터미널 > 새 터미널 ==> 터미널에서 명령어 입력 `run source "{심볼목록}" "{인수목록}"`   
```batch
:: 예문.
:: 심볼목록: NODEBUG/LOG
:: 인수목록: dev, altava, Shoes, C:/FBX/altava.fbx
run source "NODEBUG/LOG" "dev, altava, Shoes, C:/FBX/altava.fbx"
```

## 작업 후 빌드 방법
> VSCode 상단 메뉴 > 터미널 > 빌드 작업 실행 (CTRL + SHIFT + B)   
> VSCode 상단 메뉴 > 터미널 > 새 터미널 ==> 터미널에서 명령어 입력 `run build`   
~~~batch
:: 빌드 후 실행 예문.
:: 실행 파일에 넣을 때는 각 인자가 독립적으로 쌍따옴표로 존재 해야 함. (소스 실행과 인자 형태가 다름)
:: 추후 개선 진행 예정.
D:\Github\Altava_Conversion_ModelValidator\build\bin\ConversionModelValidator "dev" "altava" "Shoes" "C:/FBX/altava.fbx"
~~~

## 작업 후 서비스 방법
- README.md 참고   


## 명령어 (Windows)
- venv create   
- venv destroy   
- venv enable   
- venv disable   
- venv update   
- run venv 
- run venv create   
- run venv destroy   
- run venv enable   
- run venv disable   
- run venv update   
- run build   
- run prebuild   
- run source   
- run service   
- run tests   