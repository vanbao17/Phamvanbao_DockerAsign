

# Sử dụng Python 3.8-slim làm base image để giảm kích thước của image
FROM python:3.8-slim

# Thiết lập thư mục làm việc trong container
WORKDIR /app

# Sao chép file requirements.txt đầu tiên để tận dụng Docker cache
COPY requirements.txt /app/

# Cài đặt các thư viện cần thiết cho Flask app
RUN pip install  -r requirements.txt

# Sao chép tất cả các file còn lại vào thư mục làm việc trong container
COPY . /app

# Định nghĩa lệnh để chạy Flask app khi container được start
CMD ["python", "app.py"]

