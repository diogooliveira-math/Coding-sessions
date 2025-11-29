import { tool } from "@opencode-ai/plugin"

export default tool({
  description: "Simple test tool, that tests the agent ability to call tools",
  args: {
    path: tool.schema.string().describe("Path to output the txt file with 'successeful text'"),
  },
  async execute(args) {
        console.log("test in action");
        const fs = await import('fs/promises');
        await fs.writeFile(args.path, "sucessefull test", "utf-8");
        return `test_artifact created at ${args.path}`;
  },
})