@echo off
title HaideMath 本地开发服务器
echo.
echo 🎓 HaideMath 学术笔记阅读器
echo ================================
echo.
echo 正在启动本地开发服务器...
echo.

REM 检查Python是否安装
python --version >nul 2>&1
if %errorlevel% neq 0 (
    echo ❌ 未找到Python，请先安装Python 3.6+
    echo 下载地址: https://www.python.org/downloads/
    pause
    exit /b 1
)

REM 启动服务器
python serve.py

pause
