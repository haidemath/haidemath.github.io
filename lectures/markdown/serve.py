#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
增强的HTTP服务器，用于本地测试Markdown阅读器
支持文件列表API，可以自动发现所有.md文件
运行: python serve.py
然后访问: http://localhost:8000/viewer.html
"""

import http.server
import socketserver
import webbrowser
import os
import sys
import json
import urllib.parse
import glob
from datetime import datetime

def main():
    # 设置端口
    PORT = 8000
    
    # 切换到当前脚本所在目录
    os.chdir(os.path.dirname(os.path.abspath(__file__)))
    
    # 创建增强的HTTP服务器处理器
    class EnhancedHTTPRequestHandler(http.server.SimpleHTTPRequestHandler):
        def end_headers(self):
            self.send_header('Access-Control-Allow-Origin', '*')
            self.send_header('Access-Control-Allow-Methods', 'GET, POST, OPTIONS')
            self.send_header('Access-Control-Allow-Headers', '*')
            super().end_headers()
        
        def do_GET(self):
            # 解析URL
            parsed_path = urllib.parse.urlparse(self.path)
            
            # API端点：获取文件列表
            if parsed_path.path == '/api/files':
                self.handle_api_files()
                return
            
            # API端点：获取文件信息
            if parsed_path.path.startswith('/api/file/'):
                filename = parsed_path.path[10:]  # 移除 '/api/file/' 前缀
                self.handle_api_file_info(filename)
                return
            
            # 默认行为：静态文件服务
            super().do_GET()
        
        def handle_api_files(self):
            """处理文件列表API请求"""
            try:
                # 获取所有 .md 文件
                markdown_files = []
                
                # 扫描当前目录的 .md 文件
                for md_file in glob.glob('*.md'):
                    file_info = self.get_file_info(md_file)
                    if file_info:
                        markdown_files.append(file_info)
                
                # 也扫描子目录中的 .md 文件
                for md_file in glob.glob('**/*.md', recursive=True):
                    if md_file not in [f['file'] for f in markdown_files]:
                        file_info = self.get_file_info(md_file)
                        if file_info:
                            markdown_files.append(file_info)
                
                # 按文件名排序
                markdown_files.sort(key=lambda x: x['title'])
                
                # 返回JSON响应
                self.send_response(200)
                self.send_header('Content-Type', 'application/json; charset=utf-8')
                self.end_headers()
                
                response = {
                    'success': True,
                    'count': len(markdown_files),
                    'files': markdown_files,
                    'timestamp': datetime.now().isoformat()
                }
                
                self.wfile.write(json.dumps(response, ensure_ascii=False, indent=2).encode('utf-8'))
                
            except Exception as e:
                self.send_error_response(f"获取文件列表失败: {str(e)}")
        
        def handle_api_file_info(self, filename):
            """处理单个文件信息API请求"""
            try:
                file_info = self.get_file_info(filename)
                if file_info:
                    self.send_response(200)
                    self.send_header('Content-Type', 'application/json; charset=utf-8')
                    self.end_headers()
                    self.wfile.write(json.dumps(file_info, ensure_ascii=False, indent=2).encode('utf-8'))
                else:
                    self.send_error_response("文件不存在")
            except Exception as e:
                self.send_error_response(f"获取文件信息失败: {str(e)}")
        
        def get_file_info(self, filename):
            """获取文件详细信息"""
            try:
                if not os.path.exists(filename):
                    return None
                
                # 获取文件统计信息
                stat = os.stat(filename)
                
                # 读取文件内容来提取标题
                title = os.path.splitext(os.path.basename(filename))[0].replace('-', ' ').replace('_', ' ').title()
                content_preview = ""
                
                try:
                    with open(filename, 'r', encoding='utf-8') as f:
                        content = f.read()
                        
                        # 尝试从第一个 # 标题中提取
                        lines = content.split('\n')
                        for line in lines:
                            line = line.strip()
                            if line.startswith('# '):
                                title = line[2:].strip()
                                break
                        
                        # 获取内容预览（前200字符）
                        content_preview = content[:200].replace('\n', ' ').strip()
                        if len(content) > 200:
                            content_preview += "..."
                
                except UnicodeDecodeError:
                    # 如果UTF-8解码失败，尝试其他编码
                    try:
                        with open(filename, 'r', encoding='gbk') as f:
                            content = f.read()
                            content_preview = content[:200].replace('\n', ' ').strip()
                    except:
                        content_preview = "无法读取文件内容"
                
                return {
                    'file': filename,
                    'title': title,
                    'size': stat.st_size,
                    'lastModified': datetime.fromtimestamp(stat.st_mtime).isoformat(),
                    'preview': content_preview
                }
                
            except Exception as e:
                print(f"获取文件信息失败 {filename}: {e}")
                return None
        
        def send_error_response(self, message):
            """发送错误响应"""
            self.send_response(500)
            self.send_header('Content-Type', 'application/json; charset=utf-8')
            self.end_headers()
            error_response = {
                'success': False,
                'error': message,
                'timestamp': datetime.now().isoformat()
            }
            self.wfile.write(json.dumps(error_response, ensure_ascii=False).encode('utf-8'))
    
    try:
        with socketserver.TCPServer(("", PORT), EnhancedHTTPRequestHandler) as httpd:
            print(f"🚀 HaideMath 本地开发服务器启动成功!")
            print(f"📡 服务器地址: http://localhost:{PORT}")
            print(f"📝 Markdown阅读器: http://localhost:{PORT}/viewer.html")
            print(f"📁 服务目录: {os.getcwd()}")
            print(f"🔍 文件列表API: http://localhost:{PORT}/api/files")
            print("\n按 Ctrl+C 停止服务器")
            
            # 自动打开浏览器
            try:
                webbrowser.open(f'http://localhost:{PORT}/viewer.html')
            except:
                pass
            
            # 启动服务器
            httpd.serve_forever()
            
    except KeyboardInterrupt:
        print("\n👋 服务器已停止")
    except OSError as e:
        if e.errno == 10048:  # Windows: 端口被占用
            print(f"❌ 端口 {PORT} 被占用，请尝试其他端口或关闭占用该端口的程序")
        else:
            print(f"❌ 服务器启动失败: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()
