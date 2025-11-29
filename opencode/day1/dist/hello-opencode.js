// src/personal/hello-opencode.ts
var exampleDiff = {
  file: "src/example.ts",
  before: "console.log('old');",
  after: "console.log('new!');",
  additions: 1,
  deletions: 1
};
function printFileDiff(diff) {
  console.log(`File ${diff.file} changed: +${diff.additions} / -${diff.deletions}`);
}
printFileDiff(exampleDiff);
