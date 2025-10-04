# Danh Tính Học API

Ứng dụng Flask API cho phân tích danh tính học (tên Hán Việt, số nét, mệnh lý).

## Yêu cầu

- Docker
- Docker Compose (tùy chọn)

## Cách chạy với Docker

### 1. Build Docker Image

```bash
docker build -t danhtinhhoc-app .
```

### 2. Chạy Container

```bash
docker run -d -p 5000:5000 --name danhtinhhoc danhtinhhoc-app
```

### 3. Kiểm tra logs

```bash
docker logs -f danhtinhhoc
```

### 4. Dừng Container

```bash
docker stop danhtinhhoc
docker rm danhtinhhoc
```

## API Endpoints

Ứng dụng chạy trên port `5000` với các endpoints sau:

### 1. Convert Name (Chuyển đổi tên)
- **URL**: `/convert`
- **Method**: `GET` hoặc `POST`
- **Parameters**:
  - `family_name`: Họ (tiếng Việt hoặc tiếng Trung)
  - `given_name`: Tên (tiếng Việt hoặc tiếng Trung)
  - `language`: `vietnamese` hoặc `simplified chinese`

### 2. Get Stroke Count (Lấy số nét)
- **URL**: `/stroke`
- **Method**: `POST`
- **Body**:
  ```json
  {
    "family_name": ["陳"],
    "given_name": ["文", "明"],
    "language": "traditional chinese"
  }
  ```

### 3. Human Info (Thông tin cá nhân)
- **URL**: `/human_info`
- **Method**: `POST`
- **Body**:
  ```json
  {
    "family_name": ["陳"],
    "given_name": ["文", "明"],
    "birth": "1990-01-01"
  }
  ```

### 4. Relation Info (Thông tin quan hệ)
- **URL**: `/relation_info`
- **Method**: `POST`
- **Body**:
  ```json
  {
    "family_name": ["陳"],
    "given_name": ["文", "明"],
    "birth": "1990-01-01",
    "family_name_relation": ["黎"],
    "given_name_relation": ["明", "秀"],
    "birth_relation": "1992-05-15"
  }
  ```

### 5. Get Results (Lấy mô tả chi tiết)
- **URL**: `/get_results`
- **Method**: `POST`

## Cấu hình Production

Ứng dụng sử dụng **Gunicorn** với cấu hình:
- 4 worker processes
- Timeout: 120 giây
- Bind: `0.0.0.0:5000`

## Môi trường phát triển

Nếu muốn chạy trực tiếp không dùng Docker:

```bash
cd danhtinhhoc
pip install -r requirements.txt
python gift.py
```

Ứng dụng sẽ chạy ở chế độ debug trên port `5005`.

## Cấu trúc thư mục

```
.
├── Dockerfile
├── .dockerignore
├── README.md
└── danhtinhhoc/
    ├── requirements.txt
    ├── gift.py
    ├── gift_utils.py
    ├── human/
    ├── room/
    ├── head/
    └── ...
```

## Lưu ý

- Ứng dụng đã được chuyển từ AWS Lambda sang web server hosting
- Sử dụng Python 3.10
- Flask CORS đã được bật để hỗ trợ cross-origin requests
