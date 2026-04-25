prepare:
    cargo fetch
    npm install --package-lock-only --ignore-scripts
    python3 --version

fmt:
    cargo fmt --check
    python3 tools/check_py_format.py
    node tools/check_node_format.js

lint:
    npm run lint

clippy:
    cargo clippy --all-targets -- -D warnings

build:
    cargo build
    npm run build

test:
    cargo test
    npm test
    python3 -m unittest discover -s python_tests

integration:
    python3 tools/slow_test.py integration

e2e:
    python3 tools/slow_test.py e2e

ui-tests:
    python3 tools/slow_test.py ui-tests
