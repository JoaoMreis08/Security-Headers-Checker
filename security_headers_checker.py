import requests

HEADERS_TO_CHECK = [
    "Content-Security-Policy",
    "X-Frame-Options",
    "X-Content-Type-Options",
    "Strict-Transport-Security",
    "Referrer-Policy",
    "Permissions-Policy"
]

def check_security_headers(url):
    try:
        response = requests.get(url)
        print(f"\n Checking security headers for: {url}\n")
        for header in HEADERS_TO_CHECK:
            if header in response.headers:
                print(f" {header}: Present")
            else:
                print(f" {header}: Missing")
    except Exception as e:
        print(f" Error: {e}")

if __name__ == "__main__":
    target = input("Enter a URL (with https://): ").strip()
    if target:
        check_security_headers(target)
