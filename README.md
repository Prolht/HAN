# 标注工具
## 安装
### 建立虚拟环境
```
virtualenv env
source env/bin/activate
```
### django
```
pip install -r requirements.txt
python manage.py migrate
python manage.py createsuperuser
```
### vue
```
cd frontend
cnpm install
cnpm run build
```
## 启动
```
python manage.py runserver 8000
```