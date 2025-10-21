# 제주 사투리 번역 프로그램 (Jeju Dialect Translator)

![Devfest Presentation Banner](https://raw.githubusercontent.com/mireu-lab/Jeju-Island-dialect-translation-program/main/data/img/devfest.png)

이 프로젝트는 [2023 Devfest Cloud]에서 발표한 **'GCP를 활용한 제주도 사투리 학습 및 번역'** 과제입니다. AI Hub에서 제공하는 제주 방언 데이터를 전처리하고, Google Cloud Platform(GCP)의 PaLM2 언어 모델을 미세 조정(Fine-tuning)하여 제주 사투리를 표준어로 번역하는 모델을 개발하는 과정을 담고 있습니다.

## ✨ 주요 기능

*   **데이터 전처리**: AI Hub의 제주 방언 JSON 데이터를 CSV 형식으로 변환하고, 중복 데이터를 제거하여 학습용 데이터셋을 구축합니다.
*   **모델 학습**: GCP Vertex AI를 통해 PaLM2 모델을 미세 조정하여 제주 사투리 번역 기능을 구현합니다.
*   **간편한 환경 구성**: Docker를 활용하여 개발 및 실행 환경을 손쉽게 구축할 수 있습니다.

## 🛠️ 기술 스택

*   **언어**: Python 3
*   **주요 라이브러리**: `pandas`, `tqdm`, `openpyxl`
*   **플랫폼**: Google Cloud Platform (GCP)
*   **AI/ML**: Vertex AI, PaLM2
*   **데이터셋**: [AI Hub 한국어 방언 발화(제주도)](https://aihub.or.kr/aihubdata/data/view.do?currMenu=&topMenu=&aihubDataSe=data&dataSetSn=121)
*   **기타**: Docker, Docker Compose

## 📂 디렉터리 구조

```
.
├── README.md                 # 프로젝트 설명 파일
├── data
│   └── csv                   # 전처리된 CSV 데이터 저장 위치
│       ├── 사투리.csv
│       ├── 전체_데이터.csv
│       └── 표준어.csv
├── docker-compose.yml        # Docker Compose 설정
├── dockerfile                # Docker 이미지 빌드 파일
├── requirements.txt          # Python 의존성 목록
├── slides/                   # Devfest 발표 자료
└── src
    ├── json_to_csv.py        # JSON을 CSV로 변환하는 스크립트
    ├── test.ipynb            # 데이터 탐색 및 테스트용 노트북
    └── 중복제거.ipynb        # CSV 데이터 중복 제거 스크립트
```

## 🚀 시작하기

### 1. 사전 준비

*   [AI Hub](https://aihub.or.kr/aihubdata/data/view.do?currMenu=&topMenu=&aihubDataSe=data&dataSetSn=121)에서 '한국어 방언 발화(제주도)' 데이터셋을 다운로드합니다.
*   프로젝트 루트에 `raw_data` 디렉터리를 생성하고, 다운로드한 JSON 파일들을 모두 이 디렉터리 안에 넣어주세요.
    ```
    .
    ├── raw_data/
    │   ├── DZES20000888.json
    │   └── ... (다운로드한 모든 JSON 파일)
    ...
    ```    *(참고: `raw_data` 디렉터리는 용량이 크므로 Git 추적에서 제외하는 것을 권장합니다.)*

### 2. 환경 설정

#### 방법 A: Python 가상 환경 사용

1.  **저장소 복제**
    ```bash
    git clone https://github.com/your-username/Jeju-Island-dialect-translation-program.git
    cd Jeju-Island-dialect-translation-program
    ```

2.  **가상 환경 생성 및 활성화**
    ```bash
    python -m venv venv
    source venv/bin/activate  # macOS/Linux
    # venv\Scripts\activate   # Windows
    ```

3.  **의존성 설치**
    ```bash
    pip install -r requirements.txt
    ```

#### 방법 B: Docker 사용

Docker와 Docker Compose가 설치되어 있어야 합니다.

```bash
docker-compose up -d --build
```
이 명령은 Docker 이미지를 빌드하고 백그라운드에서 컨테이너를 실행합니다.

## ▶️ 실행 방법

데이터 전처리 과정은 아래 순서로 진행됩니다.

### 1단계: JSON을 CSV로 변환

`src/json_to_csv.py` 스크립트를 실행하여 `raw_data` 폴더의 원본 JSON 파일들을 CSV로 변환합니다. 결과물은 `data/csv/` 디렉터리에 저장됩니다.

```bash
python src/json_to_csv.py
```

### 2단계: 데이터 중복 제거

`src/중복제거.ipynb` Jupyter Notebook을 실행하여 `data/csv/`에 생성된 파일들의 중복 데이터를 제거하고 데이터셋을 정제합니다.

### 3단계: 모델 학습 (GCP Vertex AI)

전처리가 완료된 `사투리.csv` 또는 `전체_데이터.csv` 파일을 사용하여 GCP Vertex AI에서 PaLM2 모델을 미세 조정(Fine-tuning)합니다. 이 과정은 GCP 콘솔 또는 관련 SDK를 통해 진행됩니다.

## 🎤 발표 자료

본 프로젝트에 대한 자세한 내용은 `slides/` 디렉터리의 발표 자료에서 확인하실 수 있습니다.

*   **[[2023 Devfest Cloud] - GCP를 가지고 제주도 사투리 학습 시켜보기.pptx](slides/[2023%20Devfest%20Cloud]%20-%20GCP%EB%A5%BC%20%EA%B0%80%EC%A7%80%EA%B3%A0%20%EC%A0%9C%EC%A3%BC%EB%8F%84%20%EC%82%AC%ED%88%AC%EB%A6%AC%20%ED%95%99%EC%8A%B5%20%EC%8B%9C%EC%BC%9C%EB%B3%B4%EA%B8%B0.pptx)**

## 👤 개발자

*   **임미르 (Mireu Lim)**
*   **소속**: 대구가톨릭대학교 AI빅데이터공학과, None Labs
*   **GitHub**: [@mireu-lab](https://github.com/mireu-lab)
