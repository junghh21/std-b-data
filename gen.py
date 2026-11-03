import json, datetime, os
os.makedirs("out", exist_ok=True)
json.dump({"schema_version":1,"generated_at":datetime.datetime.now(datetime.timezone.utc).isoformat(timespec="seconds"),"items":[{"name":"alpha","v":1},{"name":"beta","v":2}]}, open("out/feed.json","w"), indent=1)
