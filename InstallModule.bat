@echo off
echo Checking for pip...

REM Kiem tra module da duoc cai dat chua
python -m pip --version >nul 2>&1
if %ERRORLEVEL% NEQ 0 (
    echo Pip khong tim thay module. Tien hanh cai dat...
    python -m ensurepip --default-pip
    if %ERRORLEVEL% NEQ 0 (
        echo Loi khi cai dat module.
        pause
        exit /B
    )
)

echo Module duoc cai dat thanh cong.

REM Cai dat cac thu vien can thiet
pip install speedtest-cli



echo Hoan Thanh.
pause
