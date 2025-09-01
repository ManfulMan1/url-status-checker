import urllib.request, time, csv, pathlib
urls = [u.strip() for u in pathlib.Path("urls.txt").read_text(encoding="utf-8").splitlines() if u.strip()]
with open("status.csv", "w", newline="", encoding="utf-8") as f:
    w = csv.writer(f); w.writerow(["url","status","ms"])
    for u in urls:
        t0 = time.time()
        try:
            with urllib.request.urlopen(u, timeout=10) as resp:
                code = resp.getcode()
        except Exception:
            code = "ERROR"
        w.writerow([u, code, int((time.time()-t0)*1000)])
print("OK -> status.csv")
