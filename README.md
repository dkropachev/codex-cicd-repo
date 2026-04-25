# Codex Repo CI Broad Fixture

Public fixture for exercising Codex repo-ci learning, local runner generation,
slow-test separation, and deterministic mocked-AI repair flows.

## Local Checks

```bash
just prepare
just fmt
just lint
just clippy
just build
just test
just integration
just e2e
just ui-tests
```

## Scenarios

Use `python3 tools/scenario.py <name>`:

- `green`
- `rust-lint-fail`
- `node-test-fail`
- `python-test-fail`
- `slow-tests-only`
- `context-too-large-then-fallback`

## Mock AI

```bash
MOCK_AI_SCENARIO=fix-rust-lint python3 tools/mock_ai_server.py
```

The server listens on `127.0.0.1:18080` and writes requests to
`.mock-ai/requests.jsonl`.
