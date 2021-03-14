# data
    
[remote-opencv-streaming-live-video](https://github.com/rena2damas/remote-opencv-streaming-live-video)

# run

## Server
    
    cd /home/ubuntu/workspace/remote-opencv-streaming-live-video

    docker build -t camera:v1 .
    
    docker run -d \
        --name camera-server \
        --restart=always \
        -p 800:800 \
        -p 5000:5000 \
        camera:v1
    
    access：http://52.47.87.250:800   

# Client(Ubuntu)

    cd /home/wu/workspace/remote-opencv-streaming-live-video    

    pip install -r requirements.txt -i https://mirrors.bfsu.edu.cn/pypi/web/simple --no-cache-dir
    pip uninstall opencv-python 
    pip install opencv-contrib-python
    python -u client.py
 
