import { createOpencodeClient } from "@opencode-ai/sdk";
/**
 * Usage:
 *   node find-by-parent.mjs <parentId> [baseUrl]
 *
 * Example:
 *   node find-by-parent.mjs msg_acc8e6444001qekbelwJYfmp5q http://127.0.0.1:65347
 */
async function main() {
  const [, , parentId, baseUrl = "http://127.0.0.1:65347"] = process.argv;
  if (!parentId) {
    console.error("Usage: node find-by-parent.mjs <parentId> [baseUrl]");
    process.exit(1);
  }
  const client = createOpencodeClient({ baseUrl });
  // 1) List sessions
  const sessionsRes = await client.session.list();
  const sessions = sessionsRes?.data ?? sessionsRes;
  if (!Array.isArray(sessions) || sessions.length === 0) {
    console.error("No sessions returned by the server.");
    process.exit(2);
  }
  // Helper to attempt to fetch the message in a single session
  async function tryFetchInSession(session) {
    try {
      // Do not throw on 404 - we want to inspect the response
      const res = await client.session.message({
        path: { id: session.id, messageID: parentId },
        throwOnError: false,
      });
      // If server returns data with parts, return it
      const data = res?.data ?? (res?.data?.info ? res.data : undefined);
      if (data && Array.isArray(data.parts) && data.parts.length > 0) {
        return { session, message: data };
      }
      // Some client variants return the object directly
      if (res && Array.isArray(res.parts) && res.parts.length > 0) {
        return { session, message: res };
      }
      // If response object exists, check HTTP status (not found -> skip)
      const status = res?.response?.status ?? res?.request?.response?.status;
      if (status && status !== 200 && status !== 201) {
        return null;
      }
      // Not found in this session
      return null;
    } catch (err) {
      // Network / unexpected error - surface minimal info and continue
      console.warn(`Error while checking session :`, err?.message ?? err);
      return null;
    }
  }
  // 2) Iterate sessions (sequentially to avoid overwhelming server).
  for (const session of sessions) {
    const found = await tryFetchInSession(session);
    if (found) {
      const parts = found.message.parts ?? [];
      // Reconstruct text by combining text parts, ordered by start time if available
      const text = parts
        .filter((p) => p.type === "text")
        .sort((a, b) => (Number(a.time?.start) || 0) - (Number(b.time?.start) || 0))
        .map((p) => p.text ?? "")
        .join("");
      console.log("Found in session:", session.id);
      console.log("Reconstructed text:\n");
      console.log(text || "(no text parts found)");
      process.exit(0);
    }
  }
  console.error("Message not found in any session.");
  process.exit(3);
}
main().catch((err) => {
  console.error("Unhandled error:", err);
  process.exit(4);
});