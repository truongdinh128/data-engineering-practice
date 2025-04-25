# Exercise-1:
**docker build --tag=exercise-1 .**
![alt text](./images/image.png)
![alt text](./images/image-1.png)

**docker-compose up run**
![](images/2025-04-23-12-54-00.png)
![](images/2025-04-23-12-56-15.png)

# Exercise-2:
**docker build --tag=exercise-2 .**
Trong requirements.txt, thêm: beautifulsoup4==4.12.3
![](images/2025-04-23-14-57-14.png)

**docker-compose up run**
![](images/2025-04-23-15-00-03.png)

# Exercise-3:
Không thể dùng boto3 vì Bucket public này không cho truy cập qua boto3 từ bên ngoài AWS, cần chuyển sang dùng request với 
URL: https://data.commoncrawl.org/

**docker build --tag=exercise-3 .**
![](images/2025-04-23-18-23-53.png)

**docker-compose up run**
Khi chạy sẽ hiển thị text liên tục, **CTRL + C** để dừng
![](images/2025-04-23-19-59-09.png)

# Exercise-4:
**Build và run**
![](images/2025-04-23-20-23-31.png)

# Exercise-5:
**Build và run với các lệnh như cũ**

**Kiểm tra**
![](images/2025-04-23-20-53-12.png)

# Pipeline:
**Kết quả: Thành công**

![](images/2025-04-25-01-31-56.png)

**Log Task 1**
![](images/2025-04-25-01-33-06.png)

**Log Task 2: Exercise 1**
![](images/2025-04-25-01-39-10.png)

**Log Task 3: Exercise 2**
![](images/2025-04-25-01-42-48.png)

**Log Task 4: Exercise 3**
![](images/2025-04-25-01-37-50.png)

**Log Task 5: Exercise 4**
![](images/2025-04-25-01-40-34.png)

**Log Task 6: Exercise 5 (task này không có output)**
![](images/2025-04-25-01-41-42.png)