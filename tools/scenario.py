from pathlib import Path
import shutil
import sys


ROOT = Path(__file__).resolve().parents[1]
SCENARIOS = {
    "green",
    "rust-lint-fail",
    "node-test-fail",
    "python-test-fail",
    "slow-tests-only",
    "context-too-large-then-fallback",
}


GREEN = {
    "src/lib.rs": """pub fn normalize_name(input: &str) -> String {
    input.trim().to_lowercase()
}

#[cfg(test)]
mod tests {
    use super::normalize_name;

    #[test]
    fn normalizes_name() {
        assert_eq!(normalize_name(" Codex "), "codex");
    }
}
""",
    "node_tests/text.test.js": """const assert = require("node:assert");
const { titleCase } = require("../js/text");

assert.strictEqual(titleCase("hello codex"), "Hello Codex");
console.log("node tests passed");
""",
    "python_tests/test_words.py": """import unittest

from python_pkg.words import reverse_words


class WordTests(unittest.TestCase):
    def test_reverses_words(self):
        self.assertEqual(reverse_words("hello codex"), "codex hello")


if __name__ == "__main__":
    unittest.main()
""",
}


def reset_green() -> None:
    for relative, text in GREEN.items():
        (ROOT / relative).write_text(text)
    shutil.rmtree(ROOT / ".mock-ai", ignore_errors=True)


def apply(name: str) -> None:
    reset_green()
    if name == "rust-lint-fail":
        (ROOT / "src/lib.rs").write_text(GREEN["src/lib.rs"].replace("input.trim()", "input . trim()"))
    elif name == "node-test-fail":
        (ROOT / "node_tests/text.test.js").write_text(
            GREEN["node_tests/text.test.js"].replace('"Hello Codex"', '"Hello codex"')
        )
    elif name == "python-test-fail":
        (ROOT / "python_tests/test_words.py").write_text(
            GREEN["python_tests/test_words.py"].replace('"codex hello"', '"hello codex"')
        )
    elif name in {"green", "slow-tests-only", "context-too-large-then-fallback"}:
        pass
    else:
        raise SystemExit(f"unknown scenario {name!r}; expected one of {sorted(SCENARIOS)}")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        raise SystemExit(f"usage: {sys.argv[0]} <scenario>")
    apply(sys.argv[1])
