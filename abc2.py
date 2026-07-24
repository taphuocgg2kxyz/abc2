import requests

def check_ip_info_v2():
    print("=" * 45)
    ip_address = input("Nhập IPv4 muốn check (bấm Enter để lấy IP hiện tại): ").strip()
    print("=" * 45)
    
    # 1. Nếu không nhập IP, lấy IP công cộng thực tế hiện tại qua API
    if not ip_address:
        try:
            ip_address = requests.get("https://api.ipify.org?format=json", timeout=5).json().get("ip")
            print(f"🌐 IP Công cộng hiện tại của bạn: {ip_address}\n")
        except Exception as e:
            print(f"❌ Không lấy được IP công cộng: {e}")
            return

    # 2. Tra cứu thông tin chi tiết của IP đó
    url = f"http://ip-api.com/json/{ip_address}?fields=status,message,country,regionName,city,zip,lat,lon,timezone,isp,org,as,query"
    
    try:
        response = requests.get(url, timeout=10)
        data = response.json()
        
        if data.get("status") == "fail":
            print(f"❌ Lỗi: {data.get('message', 'IP không hợp lệ!')}")
            return

        print(f"📌 Kết quả tra cứu cho IP: {data.get('query')}")
        print(f"🏢 Nhà mạng (ISP) : {data.get('isp')}")
        print(f"🏳️  Quốc gia      : {data.get('country')}")
        print(f"🏙️  Tỉnh/Thành    : {data.get('regionName')} - {data.get('city')}")
        print(f"📍 Tọa độ (Lat/Lon): {data.get('lat')}, {data.get('lon')}")
        print(f"🔗 Xem trên Maps  : https://www.google.com/maps?q={data.get('lat')},{data.get('lon')}")
        print("=" * 45)

    except requests.exceptions.RequestException as e:
        print(f"❌ Lỗi kết nối: {e}")

if __name__ == "__main__":
    check_ip_info_v2()
