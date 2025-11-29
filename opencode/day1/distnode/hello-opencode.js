"use strict";
Object.defineProperty(exports, "__esModule", { value: true });
// Example usage of FileDiff type
var exampleDiff = {
    file: "src/example.ts",
    before: "console.log('old');",
    after: "console.log('new!');",
    additions: 1,
    deletions: 1,
};
function printFileDiff(diff) {
    console.log("File ".concat(diff.file, " changed: +").concat(diff.additions, " / -").concat(diff.deletions));
}
// Example usage of Session type (with only required fields for illustration)
var exampleSession = {
    id: "session-123",
    projectID: "proj-1",
    directory: "/home/user/opencode",
    title: "Learning Example",
    version: "1.0",
    time: {
        created: Date.now(),
        updated: Date.now(),
    }
};
// Use the example diff
printFileDiff(exampleDiff);
// Show some session info
console.log("Session \"".concat(exampleSession.title, "\" is stored in: ").concat(exampleSession.directory));
