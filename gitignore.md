1. __pycache__ 디렉토리
생성 이유:

Python이 컴파일된 바이트코드를 __pycache__ 디렉토리에 저장하여 향후 import 시 파싱 및 컴파일 과정을 건너뛰고 직접 사용할 수 있도록 함
소스 코드가 바이트코드로 컴파일되고 .pyc 파일에 캐시되어 다음번 실행 시 더 빠른 실행이 가능

상세 동작:

파일이 단순히 실행될 때가 아니라 import될 때만 생성됨
3.2부터 추가되었으며, 이전 버전에서는 .pyc 파일이 같은 디렉토리에 생성되던 문제를 해결
은 해당 .pyc 파일이 최신인지 확인하고, 오래된 경우 스크립트를 다시 컴파일함
`uv pip install` does not create `__pycache__` directories in virtual enviroments · Issue #4188 · astral-sh/uv

2. .venv 디렉토리
생성 이유:

독립적인 Python 패키지 세트가 설치된 사이트 디렉토리를 가진 "가상 환경"을 생성하기 위함
프로젝트별로 격리된 환경을 제공하여 패키지 충돌을 방지


