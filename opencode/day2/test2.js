import { createOpencodeClient } from "@opencode-ai/sdk";
async function main() {
  const [, , baseUrl = "http://127.0.0.1:54440"] = process.argv;
  const client = createOpencodeClient({ baseUrl });
  try {
    const res = await client.app.agents({ throwOnError: false });
    const agents = res?.data ?? res;
    if (!Array.isArray(agents) || agents.length === 0) {
      console.log("No agents found.");
      return;
    }
    for (const a of agents) {
      // defensive access in case fields are missing
      const name = a.name ?? "<unknown>";
      const mode = a.mode ?? "<unknown>";
      const builtIn = a.builtIn ? "built-in" : "custom";
      const desc = a.description ? a.description.replace(/\s+/g, " ").trim() : "";
      const tools = a.tools ? Object.keys(a.tools).filter(k => a.tools[k]).join(", ") : "";
      console.log(`- ${name} (${mode}, ${builtIn})`);
      if (desc) console.log(`  Description: ${desc}`);
      if (a.model && a.model.providerID && a.model.modelID) {
        console.log(`  Model: ${a.model.providerID}/${a.model.modelID}`);
      } else if (a.model) {
        console.log(`  Model: ${a.model}`);
      }
      if (tools) console.log(`  Tools: ${tools}`);
    }
  } catch (err) {
    console.error("Failed to fetch agents:", err);
    process.exit(1);
  }
}
main();