type FileDiff = {
  file: string;
  before: string;
  after: string;
  additions: number;
  deletions: number;
};

// Example usage of FileDiff type
const exampleDiff: FileDiff = {
  file: "src/example.ts",
  before: "console.log('old');",
  after: "console.log('new!');",
  additions: 1,
  deletions: 1,
};

function printFileDiff(diff: FileDiff) {
  console.log(`File ${diff.file} changed: +${diff.additions} / -${diff.deletions}`);
}

// Example usage of Session type (with only required fields for illustration)

// Use the example diff
printFileDiff(exampleDiff);

// Removed example usage of Session type
