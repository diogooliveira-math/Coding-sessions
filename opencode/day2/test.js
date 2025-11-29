import { createOpencodeClient } from "@opencode-ai/sdk"

async function sendMessage() {
  // point to your local opencode server or remote baseUrl
  const client = createOpencodeClient({ baseUrl: "http://127.0.0.1:65347" })
  // create a session
  const session = await client.session.create({ body: {} })
  // send a text message
  const result = await client.session.prompt({
    path: { id: session.data.id },
    body: {
      parts: [
        { type: "text", text: "Tell me a joke" }
      ],
    },
  })
  console.log("Assistant message:", result.data.info)
  console.log("Parts:", result.data.parts)
}
sendMessage().catch(err => {
  console.error("sendMessage failed:", err)
})