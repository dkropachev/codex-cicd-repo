import os
import sys
import time


def main() -> int:
    name = sys.argv[1] if len(sys.argv) > 1 else "slow"
    marker = f"CODEx_REPO_CI_ALLOW_{name.upper().replace('-', '_')}"
    if os.environ.get(marker) == "fail":
        print(f"{name} forced failure through {marker}")
        return 1
    time.sleep(0.1)
    print(f"{name} passed")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
