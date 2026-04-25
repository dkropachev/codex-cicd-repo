const assert = require("node:assert");
const { titleCase } = require("../js/text");

assert.strictEqual(titleCase("hello codex"), "Hello codex");
console.log("node tests passed");
