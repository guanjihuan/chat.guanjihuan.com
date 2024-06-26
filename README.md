## chat.guanjihuan.com

这里把 https://chat.guanjihuan.com 的主要实现代码进行开源。代码参考各个开源大模型的 GitHub 或 HuggingFace 主页、大语言模型的 API 官网，以及 HuggingFace 和 Pytorch 的文档等。

硬件要求：如果是本地 GPU 运行模型，还需要 Nvidia 显卡，至少 6G 显存。说明：这里只测试了几个模型，还有更多开源大模型，感兴趣的可以自行测试。通常，8G 显存的显卡可以量化地加载 7B 左右的模型（70亿参数）；16G 显存的显卡可以完整加载 7B 左右的模型（70亿参数）或量化地加载 14B 左右的模型（140亿参数）；更大参数空间的模型的运行需要更大显存的显卡。开源大模型的排行榜有：

+ https://huggingface.co/spaces/HuggingFaceH4/open_llm_leaderboard
+ https://cevalbenchmark.com/static/leaderboard.html
+ https://opencompass.org.cn/leaderboard-llm
+ https://www.superclueai.com

### 一、基础环境

运行这里的代码需要安装 Python 环境，可以选择安装 Anaconda：https://www.anaconda.com 。

Web 框架是使用 Streamlit：https://streamlit.io 、https://github.com/streamlit/streamlit 。

Streamlit 的安装：

```
pip install streamlit
```

运行命令：

```
streamlit run web_demo.py
```

或

```
python -m streamlit run web_demo.py
```

如果是在公网IP下访问，并指定8501端口和黑色主题，那么运行命令为：

```
streamlit run web_demo.py --theme.base dark --server.port 8501 --server.address 0.0.0.0 
```

如果是本地运行开源大语言模型，为了防止一些不必要的报错，可以更新一下操作系统的显卡驱动并重启：

```
sudo apt-get update

sudo apt-get install ubuntu-drivers-common

sudo ubuntu-drivers autoinstall
```

此外，更新一下 Pytorch（ [https://pytorch.org/get-started/locally/](https://pytorch.org/get-started/locally/) ）也可以防止一些报错：

```
conda install pytorch torchvision torchaudio pytorch-cuda=11.8 -c pytorch -c nvidia
```

### 二、本地运行开源大语言模型

#### 1. 开源模型 ChatGLM

ChatGLM3-6B 主页：https://github.com/THUDM/ChatGLM3 。 安装该模型依赖的环境：

```
pip install -r requirements.txt
```

模型文件下载：https://huggingface.co/THUDM/chatglm3-6b-32k ，放在目录 THUDM/chatglm3-6b-32k 下。

显存/内存要求：量化加载大概要 6G 显存；默认加载大概需要 13G 显存；CPU加载大概需要 25G 内存。

运行命令：

```
python -m streamlit run ./ChatGLM.py --theme.base dark --server.port 8501
```

如果量化加载时 bitsandbytes 报错，那么安装该软件包：pip install bitsandbytes

#### 2. 开源模型 Qwen

Qwen 主页：https://github.com/QwenLM/Qwen 。 安装该模型依赖的环境：

```
pip install -r requirements.txt
```

Qwen-7B-Chat-Int4 模型文件下载：https://huggingface.co/Qwen/Qwen-7B-Chat-Int4 ，放在目录 Qwen/Qwen-7B-Chat-Int4 下。

Qwen-14B-Chat-Int4 模型文件下载：https://huggingface.co/Qwen/Qwen-14B-Chat-Int4 ，放在目录 Qwen/Qwen-14B-Chat-Int4 下。

显存要求：Qwen-7B-Chat-Int4 大概需要 8G 显存；Qwen-14B-Chat-Int4 大概需要 12G 显存。

运行命令：

```
python -m streamlit run ./Qwen.py --theme.base dark --server.port 8501
```

此外，如果运行有报错，可能还需要安装：

```
pip install optimum
pip install auto-gptq
pip install --upgrade s3fs aiobotocore botocore
```

#### 3. 开源模型 InternLM

InternLM 主页：https://github.com/InternLM/InternLM 。运行代码时，需要调用其中的 tools 文件夹。

internlm-chat-7b 模型文件下载：https://huggingface.co/internlm/internlm-chat-7b ，放在 internlm/internlm-chat-7b 目录下。说明：提供的代码是加载 internlm-chat-7b 模型， 目前已经有 internlm2-chat-7b 模型，但个人还未测试。internlm2-chat-7b 模型文件下载：https://huggingface.co/internlm/internlm2-chat-7b

显存要求：大概需要 7G 的显存。

运行命令：

```
python -m streamlit run ./InternLM.py --theme.base dark --server.port 8501
```

#### 4. ……

### 三、使用大语言模型 API

#### 1. 智谱 - ChatGLM_Turbo

智谱 API key 获取（收费，可免费试用）：https://maas.aminer.cn

运行命令：

```
python -m streamlit run ./ChatGLM_Turbo.py --theme.base dark --server.port 8501
```

说明：当前代码只对 pip install zhipuai==1.0.7 有效，对最新版本不兼容。另外，早期使用的模型调用是 model="chatglm_turbo"， 官网文档最新的模型是 model="glm-3-turbo"。工单客服回复内容为：“chatglm_turbo与glm-3-turbo是不同的模型，glm-3-turbo理论上能力优于chatglm_turbo，且价格更便宜”。个人推荐的是 glm-4-flash 模型。

#### 2. 阿里 - Qwen_Turbo

阿里 API key 获取（有的收费，有的免费）：https://dashscope.aliyun.com

运行命令：

```
python -m streamlit run ./Qwen_Turbo.py --theme.base dark --server.port 8501
```

需要安装软件包：pip install dashscope

#### 3. 腾讯 - 混元大模型

腾讯 API key 获取（有的收费，有的免费）：https://cloud.tencent.com/product/hunyuan

运行命令：
```
python -m streamlit run ./Hunyuan_Lite.py --theme.base dark --server.port 8501
```

#### 4. 讯飞 - 星火大模型

讯飞 API key 获取（有的收费，有的免费）：https://xinghuo.xfyun.cn

运行命令：

```
python -m streamlit run ./星火大模型.py --theme.base dark --server.port 8501
```

#### 5. 百度 - ERNIE_Speed_128K

百度千帆大模型平台 API key 获取（有的收费，有的免费）：https://console.bce.baidu.com/qianfan/overview

运行命令：

```
python -m streamlit run ./ERNIE_Speed_128K.py --theme.base dark --server.port 8501
```

#### 6. 零一万物 - Yi_Spark

零一万物大模型开放平台（有免费额度）：https://platform.lingyiwanwu.com

需要安装 OpenAI 软件包：

```
pip install openai
```

运行命令：

```
python -m streamlit run ./Yi_Spark.py --theme.base dark --server.port 8501
```

#### 7. 火山引擎 - Doubao_lite_32k

豆包大模型 - 火山引擎（有免费额度）：https://www.volcengine.com/product/doubao

需要安装：

```
pip install volcengine-python-sdk
```

运行命令：
```
python -m streamlit run ./Doubao_lite_32k.py --theme.base dark --server.port 8501
```

#### 8. OpenAI - GPT_3.5_Turbo

OpenAI 的 API 接口（需要海外的 IP 地址以及海外银行卡）：https://platform.openai.com

需要安装 OpenAI 软件包：

```
pip install openai
```

运行命令：

```
python -m streamlit run ./GPT_3.5_Turbo.py --theme.base dark --server.port 8501
```

#### 9. ……