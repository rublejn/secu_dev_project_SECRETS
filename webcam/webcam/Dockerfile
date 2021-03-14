FROM python:3.9
EXPOSE 5000 8080

COPY  requirements.txt /root/app/
WORKDIR /root/app
RUN pip install -r requirements.txt -i https://mirrors.bfsu.edu.cn/pypi/web/simple --no-cache-dir \
    && pip uninstall opencv-python -y  \
    && pip install opencv-python-headless -i https://mirrors.bfsu.edu.cn/pypi/web/simple --no-cache-dir

COPY  . /root/app

ENTRYPOINT ["python"]
CMD ["server.py"]