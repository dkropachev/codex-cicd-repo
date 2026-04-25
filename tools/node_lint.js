const fs = require("node:fs");

const source = fs.readFileSync("js/text.js", "utf8");
if (!source.includes("module.exports")) {
  console.error("js/text.js must export its public API");
  process.exit(1);
}
console.log("node lint passed");
