from pathlib import Path


PATHS = [Path("python_pkg/words.py"), Path("python_tests/test_words.py")]


def main() -> int:
    failures = []
    for path in PATHS:
        text = path.read_text()
        if not text.endswith("\n"):
            failures.append(f"{path}: missing trailing newline")
        for line_number, line in enumerate(text.splitlines(), start=1):
            if line.rstrip() != line:
                failures.append(f"{path}:{line_number}: trailing whitespace")
    for failure in failures:
        print(failure)
    return 1 if failures else 0


if __name__ == "__main__":
    raise SystemExit(main())
