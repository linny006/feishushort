# 飞书文档跳转服务

## 项目简介
这是一个基于 FastAPI 的简单服务，部署到 Vercel 后，用户访问服务地址时会自动跳转到指定的飞书文档链接。

## 功能
- **自动跳转**：访问根路径 `/` 时，自动跳转到指定的飞书文档。
- **健康检查**：访问 `/health` 路径时，返回服务健康状态。

## 快速开始

### 1. 克隆项目
```bash
git clone git@github.com:linny006/feishushort.git
cd feishushort
```

### 2. 安装依赖
确保已安装 Python 3.9 或更高版本。
```bash
pip install -r requirements.txt
```

### 3. 本地运行
使用 Uvicorn 启动服务：
```bash
uvicorn main:app --reload
```
服务启动后：
- 访问 `http://127.0.0.1:8000/` 会跳转到飞书文档。
- 访问 `http://127.0.0.1:8000/health` 查看健康状态。

### 4. 部署到 Vercel
1. 将代码推送到 GitHub 仓库。
2. 在 [Vercel](https://vercel.com/) 创建新项目，选择该 GitHub 仓库。
3. 部署完成后，访问 Vercel 提供的域名即可。

## 文件结构
```
feishushort/
├── main.py          # FastAPI 应用主文件
├── requirements.txt # Python 依赖文件
├── vercel.json      # Vercel 配置文件
└── README.md        # 项目说明文档
```

## 配置
- **飞书文档链接**：在 `main.py` 文件中修改 `FEISHU_URL` 常量即可更改跳转目标。

## 贡献
欢迎提交 Issue 或 Pull Request 来改进本项目。

## 许可证
MIT License
