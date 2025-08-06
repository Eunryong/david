좋습니다. 아래는 **`history` 명령어 목록(167\~235)** 중에서 **중복되거나 반복된 명령어**를 정리하고, 의미 있는 순서와 그룹으로 **간결하게 정리한 버전**입니다.

---

# ✅ 중복 제거 및 정리된 명령어 실행 기록

### 📁 1. Git 저장소 클론 및 커밋

```bash
git clone https://github.com/Eunryong/david.git
cd david/
touch tmp
git add .
git commit -m "chore: tmp"
git push origin main
rm tmp
git add .
git commit -m "chore: tmp"
git push origin main
```

> ⚠️ `git login`은 잘못된 명령어이며 `git commmit`도 오타입니다. 실사용 시 무시.

---

### 🧪 2. Flask 앱 실행 및 가상환경

```bash
python3 app.py
sudo python3 app.py
python3 -m venv .venv
source .venv/bin/activate      # 잘못된 `sudo source`는 생략
vim app.py                     # 수정 작업
python3 app.py
```

> `lsof -i:80`, `lsof -i:8080`은 Flask가 어떤 포트를 사용하는지 확인하기 위한 명령입니다.

---

### ⚙️ 3. systemd 유닛 파일 작성 및 등록

```bash
sudo vim /lib/systemd/system/david.service      # 유닛 파일 작성 및 수정 (여러 번 반복됨)
sudo systemctl daemon-reload                    # systemd에 변경 적용 (반복 OK)
sudo systemctl enable david.service             # 부팅 시 자동 실행 설정
sudo systemctl start david.service              # 서비스 수동 실행
sudo systemctl status david.service             # 서비스 상태 확인
journalctl -u david.service -e                  # 서비스 로그 확인
```

> `vim`, `daemon-reload`, `enable`, `start`, `status`의 반복은 동일 작업 반복이며, 하나로 요약합니다.

---

### 🔧 4. 기타 유틸성 명령어

```bash
ls
ls -a
pwd
which python3
lsof -i:8080
```

> 디렉토리 확인, Python 위치 확인, 포트 사용 확인 등으로 반복 사용되었으나 기능적으로는 중복.

---

## 📌 요약: 실행 흐름

1. Git 저장소 클론 및 테스트 커밋 푸시
2. Flask 앱 실행 → 에러 확인 → 수정 반복
3. 가상환경 생성 및 실행
4. systemd 유닛 파일 생성, 서비스 등록, 상태 확인
5. 포트 충돌 여부 확인 및 서비스 실행 로그 모니터링

---

필요하시면 위 내용을 **Markdown, PDF, 문서파일(DOCX)** 등으로 변환해 드릴 수 있습니다. 원하시는 형식을 알려주세요.
