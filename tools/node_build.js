const { titleCase } = require("../js/text");

if (titleCase("build check") !== "Build Check") {
  console.error("build check failed");
  process.exit(1);
}
console.log("node build passed");
