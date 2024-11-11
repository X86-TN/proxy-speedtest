import os
import speedtest

# Read proxy
def read_proxies_from_file(file_path):
    proxies = []
    with open(file_path, 'r') as file:
        for line in file:
            parts = line.strip().split(':')
            if len(parts) == 4:
                ip, port, user, password = parts
                proxy = f"http://{user}:{password}@{ip}:{port}"
                proxies.append((ip, port, user, password, proxy))
    return proxies

# speedtest cons
def test_speed():
    try:
        st = speedtest.Speedtest()
        st.get_best_server()
        download_speed = st.download() / 1_000_000  # convert bps - Mbps
        upload_speed = st.upload() / 1_000_000      # convert bps - Mbps
        ping = st.results.ping

        return download_speed, upload_speed, ping
    except Exception as e:
        return None, None, None, str(e)


proxy_file = 'proxy.txt'
result_file = 'result.txt'


proxies = read_proxies_from_file(proxy_file)


try:
    with open(result_file, 'w', encoding='utf-8') as file:
        pass
except Exception as e:
    print(f"Lỗi khi xóa nội dung cũ: {e}")


for ip, port, user, password, proxy in proxies:

    os.environ["http_proxy"] = proxy
    os.environ["https_proxy"] = proxy
    print(f"Đang sử dụng proxy: {proxy}")

    try:
        # Starting speedtest
        download_speed, upload_speed, ping = test_speed()

        if download_speed is not None:
            result = (f"{ip}:{port}:{user}:{password}|"
                      f"dow:{download_speed:.2f}Mbps|"
                      f"up:{upload_speed:.2f}Mbps|"
                      f"ping:{ping:.2f}ms")
        else:
            result = f"{ip}:{port}:{user}:{password}|Lỗi khi kiểm tra tốc độ mạng"

        print(result)
    except Exception as e:
        # Write error
        result = f"{ip}:{port}:{user}:{password}|Lỗi: {str(e)}"
        print(result)

    # write result 
    try:
        with open(result_file, 'a', encoding='utf-8') as file:
            file.write(result + '\n')
    except Exception as e:
        print(f"Lỗi khi ghi kết quả vào tệp: {e}")
