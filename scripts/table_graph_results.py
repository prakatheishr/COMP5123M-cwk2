import matplotlib.pyplot as plt
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
results = BASE_DIR / "results"
results.mkdir(parents=True, exist_ok=True)

# performance data
loads = ["Low", "Medium", "High"]

cloud_latency = [2.55, 9.76, 31.94]
edge_latency = [1.55, 5.03, 17.39]

cloud_req = [4633, 5175, 6606]
edge_req = [9090, 10465, 12071]

# graph 1: Throughput Comparison
plt.figure(figsize=(8, 5))
plt.plot(loads, cloud_req, marker="o", linewidth=2, label="Cloud (kind)")
plt.plot(loads, edge_req, marker="o", linewidth=2, label="Edge (K3s)")
plt.title("Throughput Comparison (Cloud vs Edge)")
plt.xlabel("Load Level")
plt.ylabel("Requests per Second")
plt.legend()
plt.grid(True, alpha=0.3)
plt.tight_layout()
plt.savefig(results / "throughput_comparison.png", dpi=300)
plt.close()

# graph 2: Latency Comparison
plt.figure(figsize=(8, 5))
plt.plot(loads, cloud_latency, marker="o", linewidth=2, label="Cloud (kind)")
plt.plot(loads, edge_latency, marker="o", linewidth=2, label="Edge (K3s)")
plt.title("Latency Comparison (Cloud vs Edge)")
plt.xlabel("Load Level")
plt.ylabel("Average Latency (ms)")
plt.legend()
plt.grid(True, alpha=0.3)
plt.tight_layout()
plt.savefig(results / "latency_comparison.png", dpi=300)
plt.close()

# ASCII Table
table = """
Final Experimental Results

Low Load (10 connections)
+---------------+-------------+------------------+------------------+-------------+------------+
| Environment   | Avg Latency | Avg Requests/sec | Avg Transfer/sec | Avg Pod CPU | Pod Memory |
+---------------+-------------+------------------+------------------+-------------+------------+
| Cloud (kind)  | 2.55 ms     | 4633 req/s       | 3.77 MB/s        | 113m        | 3–4 Mi    |
| Edge (K3s)    | 1.55 ms     | 9090 req/s       | 7.40 MB/s        | 67m         | 3 Mi      |
+---------------+-------------+------------------+------------------+-------------+------------+

Medium Load (50 connections)
+---------------+-------------+------------------+------------------+-------------+------------+
| Environment   | Avg Latency | Avg Requests/sec | Avg Transfer/sec | Avg Pod CPU | Pod Memory |
+---------------+-------------+------------------+------------------+-------------+------------+
| Cloud (kind)  | 9.76 ms     | 5175 req/s       | 4.21 MB/s        | 108m        | 4 Mi       |
| Edge (K3s)    | 5.03 ms     | 10465 req/s      | 8.51 MB/s        | 220m        | 3 Mi       |
+---------------+-------------+------------------+------------------+-------------+------------+

High Load (200 connections)
+---------------+-------------+------------------+------------------+-------------+------------+
| Environment   | Avg Latency | Avg Requests/sec | Avg Transfer/sec | Avg Pod CPU | Pod Memory |
+---------------+-------------+------------------+------------------+-------------+------------+
| Cloud (kind)  | 31.94 ms    | 6606 req/s       | 5.25 MB/s        | 125m        | 4–5 Mi     |
| Edge (K3s)    | 17.39 ms    | 12071 req/s      | 9.82 MB/s        | 232m        | 3–4 Mi     |
+---------------+-------------+------------------+------------------+-------------+------------+
""".strip()

# save to text file
with open(results / "final_experimental_results.txt", "w", encoding="utf-8") as f:
    f.write(table + "\n")