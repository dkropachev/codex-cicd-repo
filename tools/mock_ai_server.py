from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
import json
import os
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
LOG_DIR = ROOT / ".mock-ai"
LOG_PATH = LOG_DIR / "requests.jsonl"


RESPONSES = {
    "fix-rust-lint": "Run `cargo fmt` to repair the Rust formatting failure, then rerun repo CI.",
    "fix-node-test": "Update node_tests/text.test.js to expect `Hello Codex`, then rerun repo CI.",
    "fix-python-test": "Update python_tests/test_words.py to expect `codex hello`, then rerun repo CI.",
    "context-too-large": "context_length_exceeded",
    "fallback-success": "Fallback model succeeded. Apply the targeted test expectation fix and rerun.",
    "unrelated-ci-ignore": "The failing check is unrelated to the branch changes. Do not edit code.",
    "whole-suite-failure-report": "The whole suite failed. Report the suite-level failure and stop.",
}


class Handler(BaseHTTPRequestHandler):
    def do_POST(self):
        length = int(self.headers.get("content-length", "0"))
        body = self.rfile.read(length).decode("utf-8")
        LOG_DIR.mkdir(exist_ok=True)
        with LOG_PATH.open("a") as handle:
            handle.write(body + "\n")

        scenario = os.environ.get("MOCK_AI_SCENARIO", "fallback-success")
        text = RESPONSES.get(scenario, RESPONSES["fallback-success"])
        response = {
            "id": "resp_mock",
            "object": "response",
            "created_at": 0,
            "status": "completed",
            "model": "mock-ci",
            "output": [
                {
                    "id": "msg_mock",
                    "type": "message",
                    "role": "assistant",
                    "content": [{"type": "output_text", "text": text}],
                }
            ],
            "usage": {"input_tokens": 1, "output_tokens": 1, "total_tokens": 2},
        }
        payload = json.dumps(response).encode("utf-8")
        self.send_response(200)
        self.send_header("content-type", "application/json")
        self.send_header("content-length", str(len(payload)))
        self.end_headers()
        self.wfile.write(payload)

    def log_message(self, format, *args):
        return


def main() -> None:
    server = ThreadingHTTPServer(("127.0.0.1", 18080), Handler)
    print("mock AI server listening on http://127.0.0.1:18080")
    server.serve_forever()


if __name__ == "__main__":
    main()
