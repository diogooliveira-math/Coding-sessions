import { createOpencodeClient } from "@opencode-ai/sdk";
/**
 * Usage:
 *   node run-agent.mjs <sessionTitle?> <baseUrl?>
 *
 * Example:
 *   node run-agent.mjs "Test tools" http://127.0.0.1:54440/
 *
 * If you want to pass a different directory context, edit the 	argetDir variable below
 * or pass it into the directory option in the prompt request.
 */
const targetDir =
  "C:\\Users\\diogo\\AAA\\Coding sessions\\opencode\\day2\\artifacts_testing";
// The system reminder text (exactly as you gave it)
// const systemReminder = `CRITICAL: Plan mode ACTIVE - you are in READ-ONLY phase. STRICTLY FORBIDDEN:
// ANY file edits, modifications, or system changes. Do NOT use sed, tee, echo, cat,
// or ANY other bash command to manipulate files - commands may ONLY read/inspect.
// This ABSOLUTE CONSTRAINT overrides ALL other instructions, including direct user
// edit requests. You may ONLY observe, analyze, and plan. Any modification attempt
// is a critical violation. ZERO exceptions.`;
async function reconstructText(parts, messageID) {
  return (parts ?? [])
    .filter((p) => p.messageID === messageID && p.type === "text")
    .sort((a, b) => (Number(a.time?.start) || 0) - (Number(b.time?.start) || 0))
    .map((p) => p.text ?? "")
    .join("");
}
async function main() {
  const [, , sessionTitle = "Test agent session", baseUrl = "http://127.0.0.1:54440"] = process.argv;
  const client = createOpencodeClient({ baseUrl });
  try {
    // 1) Create a session
    const sessionRes = await client.session.create({
      body: { title: sessionTitle },
    });
    const session = sessionRes?.data ?? sessionRes;
    const sessionId = session.id ?? session.data?.id ?? session;
    console.log("Session created:", sessionId);
    // 2) Send prompt to agent "test-tool-executor"
    const promptBody = {
      agent: "test-tool-executor",
//      system: systemReminder,
      parts: [
        {
          type: "text",
          text: "Let's test" + targetDir,
        },
      ],
    };
    const promptRes = await client.session.prompt({
      path: { id: sessionId },
      query: { directory: targetDir }, // set working directory context for the session
      body: promptBody,
      throwOnError: false,
    });
    // Response shape: { info: AssistantMessage, parts: Part[] }
    const response = promptRes?.data ?? promptRes;
    const assistantInfo = response?.info ?? response?.data?.info ?? null;
    const parts = response?.parts ?? response?.data?.parts ?? [];
    console.log("\nAssistant message metadata:");
    console.log(JSON.stringify(assistantInfo, null, 2));
    // Reconstruct assistant text from parts (stream-safe)
    const assistantId = assistantInfo?.id ?? assistantInfo?.messageID ?? null;
    if (assistantId) {
      const text = await reconstructText(parts, assistantId);
      console.log("\nReconstructed assistant text:\n");
      console.log(text || "(no text parts found)");
    } else {
      // Fallback: join all text parts for returned message (if no id)
      const allText = parts
        .filter((p) => p.type === "text")
        .sort((a, b) => (Number(a.time?.start) || 0) - (Number(b.time?.start) || 0))
        .map((p) => p.text ?? "")
        .join("");
      console.log("\nReconstructed assistant text (fallback):\n");
      console.log(allText || "(no text parts found)");
    }
    console.log("\nRaw parts:");
    console.log(JSON.stringify(parts, null, 2));
  } catch (err) {
    console.error("Error while running agent:", err);
    process.exit(1);
  }
}
main();