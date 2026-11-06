from datetime import datetime

def main():
    now = datetime.now()
    # 格式化输出，自动补0
    time_str = now.strftime("%Y-%m-%d %H:%M:%S")
    print(f"当前时间：{time_str}")
    print("Hello GitHub & Python!")

if __name__ == "__main__":
    main()
