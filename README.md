# BotPicUploader
易于部署的图床TG bot，随机分发给图床并失败弹出

<p align="center">
<img src="https://img.shields.io/badge/language-python-green.svg"/>
<img src="https://img.shields.io/badge/license-Apache-blue"/>
</p>


## Setup
```
pip install -r requirements.txt
```

**然后修改你的token,加入自己写的上传类。**

## Run

**在尾端列表加入你的类。**

```
nohup python main.py > output.log 2>&1 &
```

**查看进程**

```
ps -aux|grep python3
```

**终止进程**

```
kill -9  进程号
```
