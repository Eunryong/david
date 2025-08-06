

# 📄 init과 systemd의 차이

**`init`과 `systemd`는 Linux에서 부팅 시 시스템과 서비스를 관리하는 초기화 시스템(init system)입니다.**

---

## ✅ 개요 비교

| 항목           | SysVinit (`init`)   | `systemd`                             |
| ------------ | ------------------- | ------------------------------------- |
| 등장 시기        | 전통적 (1983년부터)       | 현대적 (2010년부터)                         |
| 동작 방식        | 순차적 서비스 실행          | 병렬 실행, 의존성 기반                         |
| 서비스 정의       | `/etc/init.d/` 스크립트 | `.service` 유닛 파일                      |
| 부팅 속도        | 느림 (순차 실행)          | 빠름 (병렬 실행)                            |
| 서비스 상태 확인    | 제한적 (`service` 명령)  | 강력한 상태 관리 (`systemctl`, `journalctl`) |
| 로깅 시스템       | syslog              | `journald` 내장                         |
| 타이머, 소켓 등 관리 | 불가능                 | 가능 (`.timer`, `.socket`)              |
| 의존성/순서 지정    | 복잡한 스크립트            | 단순하고 명확한 유닛 설정                        |

---

## ✅ 예시 비교

### ▶️ init 방식

```bash
/etc/init.d/apache2 start
```

### ▶️ systemd 방식

```bash
sudo systemctl start apache2
sudo systemctl enable apache2
sudo journalctl -u apache2
```

---

## ✅ 결론

| 상황                                      | 추천                      |
| --------------------------------------- | ----------------------- |
| 최신 리눅스 배포판 (Ubuntu ≥ 16.04, CentOS ≥ 7) | `systemd` 기본 사용         |
| 예전 배포판 유지보수, 경량 리눅스                     | `init` 또는 `OpenRC` 등 가능 |

`systemd`는 속도, 관리 편의성, 모듈성 등에서 우수하며, 현재는 **리눅스 표준 초기화 시스템으로 자리잡음**.

---

필요하다면 이 내용을 **Markdown, PDF, DOCX 등 파일**로 만들어 드릴 수 있습니다. 원하시는 형식을 알려주세요.
