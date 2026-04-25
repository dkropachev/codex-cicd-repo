const fs = require("node:fs");

const paths = ["js/text.js", "node_tests/text.test.js"];
let failed = false;

for (const path of paths) {
  const text = fs.readFileSync(path, "utf8");
  if (!text.endsWith("\n")) {
    console.error(`${path}: missing trailing newline`);
    failed = true;
  }
  for (const [index, line] of text.split(/\n/).entries()) {
    if (line.trimEnd() !== line) {
      console.error(`${path}:${index + 1}: trailing whitespace`);
      failed = true;
    }
  }
}

process.exit(failed ? 1 : 0);
