from src.collectors.football_data import FootballDataCollector

API_KEY = "ضع الـ API الجديد هنا"

def main():
    collector = FootballDataCollector(API_KEY)

    data = collector.fetch()

    if data:
        print("Connection Successful")
        print(data)

if __name__ == "__main__":
    main()