# 磁力链接在线播放器

基于 Django 的 Web 服务，提供磁力链接在线原画质/音质播放和下载入口。界面自适应手机与电脑浏览器，可快速部署在本地或服务器。

## 功能特性

- ✨ 粘贴磁力链接即可调用 Webtor 播放器在线播放原始画质/音质的视频或音频。
- 📱 自适应布局，在手机、平板及桌面浏览器上均拥有良好体验。
- 📥 提供跳转至 Webtor 播放页和复制磁力链接的快捷入口，便于下载到本地客户端。
- 🔒 支持通过环境变量自定义密钥、调试模式和允许访问的主机列表。

## 快速开始

1. 安装依赖（需能够访问 Python 包索引）：

   ```bash
   pip install -r requirements.txt
   ```

2. 进入项目目录并运行开发服务器：

   ```bash
   cd magnetplayer
   python manage.py migrate  # 首次运行可选
   python manage.py runserver 0.0.0.0:8000
   ```

3. 打开浏览器访问 `http://127.0.0.1:8000/`，粘贴磁力链接后即可在线播放或下载。

> **提示**：如果运行环境无法访问外网，可将 `https://cdn.jsdelivr.net/npm/webtor@0.2.26/dist/webtor.min.js` 下载至本地并通过静态资源服务加载。

## 部署建议

- 如需对公网开放，建议在反向代理中启用 HTTPS，并配置跨域访问限制。
- 可通过环境变量 `DJANGO_SECRET_KEY`、`DJANGO_DEBUG`、`DJANGO_ALLOWED_HOSTS` 调整运行参数。
- 若需进一步扩展（如用户认证、播放历史等），可在 `stream` 应用内继续开发。
