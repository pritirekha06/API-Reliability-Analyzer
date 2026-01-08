def analyze_results(results):
    total = len(results)
    successes = [r for r in results if r["success"]]
    failures = total - len(successes)

    times = [r["time"] for r in successes if r["time"] is not None]

    avg_time = sum(times) / len(times) if times else 0
    max_time = max(times) if times else 0
    success_rate = (len(successes) / total) * 100 if total else 0

    if success_rate > 95 and avg_time < 0.5:
        verdict = "Stable"
    elif success_rate > 80:
        verdict = "Degrading"
    else:
        verdict = "Unstable"

    return {
        "total_requests": total,
        "success_rate": round(success_rate, 2),
        "avg_response_time": round(avg_time, 3),
        "max_response_time": round(max_time, 3),
        "verdict": verdict
    }
