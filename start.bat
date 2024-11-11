@echo off
echo Running speedtest

REM Kiểm tra nếu Python đã được cài đặt
python --version >nul 2>&1
if %ERRORLEVEL% NEQ 0 (
    echo Python không được tìm thấy. Vui lòng cài đặt Python và thêm nó vào biến môi trường PATH.
    pause
    exit /B
)

REM Chạy speedtest
python main.py

echo Hoàn tất
pause
