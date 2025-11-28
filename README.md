# Movie Recommendation Web Service 🎬🍿

## 프로젝트 개요 🌟
이 프로젝트는 Django와 Vue.js를 기반으로 만들어진 **영화 추천 웹 서비스**입니다. 사용자는 팔로우, 좋아요 기능을 통해 자신이 선호하는 영화와 다른 사용자와 상호작용할 수 있어요. 또한, **JSON 파일을 불러와서 영화 데이터를 동적으로 관리**하며, 영화 장르별로 메인 화면에 영화를 출력합니다.

## 주요 기능 ✨
- **팔로우/언팔로우 기능**: 사용자는 다른 사용자를 팔로우하거나 언팔로우할 수 있어요. 👥
- **좋아요 기능**: 영화에 대해 좋아요를 눌러 자신이 선호하는 영화를 표시할 수 있어요. ❤️
- **영화 장르별 출력**: 영화 데이터를 장르별로 필터링하여 메인 화면에 표시합니다. 🎥
- **영화 데이터**: JSON 파일을 불러와 영화 데이터를 동적으로 관리하고, 장르별로 분류하여 화면에 출력합니다. 🗂️

## 기술 스택 🛠️
- **Backend**: Django (Python)
- **Frontend**: Vue.js (JavaScript)
- **Database**: SQLite (기본 DB)
- **API**: Axios를 사용하여 JSON 파일을 불러오고 처리
- **Version Control**: Git, GitHub

## 설치 방법 ⚙️
1. **클론 받기**:
   ```bash
   git clone https://github.com/username/movie-recommendation.git

2. 가상 환경 설정:

```bash
cd movie-recommendation
python3 -m venv venv
source venv/bin/activate

# Windows는 venv\Scripts\activate
```

3. 필요한 패키지 설치:

```bash
pip install -r requirements.txt
```

4. Django 마이그레이션:

```bash
python manage.py migrate
```

5. 서버 실행:

```bash
python manage.py runserver
```

6. 이후 http://127.0.0.1:8000
에서 프로젝트를 확인할 수 있어요. 🌐

## 기능 설명 📝
### 팔로우 및 좋아요 기능 💬

- 팔로우: 사용자는 다른 사용자를 팔로우하고, 그 사용자가 좋아하는 영화나 활동을 볼 수 있어요. 🔍

- 좋아요: 영화에 좋아요를 눌러 자신이 선호하는 영화를 표시할 수 있어요. ❤️

###  JSON 파일 불러오기 📂

- `movie_data.json` 파일을 프로젝트에 포함시켜 데이터를 로드하며, 이를 통해 동적으로 영화를 장르별로 필터링하여 메인 화면에 출력합니다. 🔄

### 영화 장르별 출력 🎥

- 영화 데이터를 장르별로 나누어 메인 화면에 표시됩니다. 이때 장르는 JSON 파일의 각 항목에 포함된 정보를 바탕으로 필터링됩니다. 🎞️

### 폴더 구조 📂
```csharp
movie-recommendation/
│
├── backend/             # Django 백엔드 프로젝트
│   ├── manage.py
│   ├── movieapp/        # 영화 관련 앱
│   ├── requirements.txt
│
├── frontend/            # Vue.js 프론트엔드 프로젝트
│   ├── src/
│   └── public/
├── movie_data.json      # 영화 데이터 JSON 파일
└── README.md            # 이 문서
```

## 기여 방법 🙌

1. 이 프로젝트를 포크합니다. 🍴

2. 새로운 기능이나 버그 수정 작업을 브랜치에서 수행합니다. 🔧

3. 작업을 완료한 후, **풀 리퀘스트(PR)**를 생성하여 기여를 제출합니다. 📝

## 개발자
- 팀장 : 조하원
- 팀원 : 손효지