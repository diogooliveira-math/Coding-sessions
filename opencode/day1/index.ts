import { createOpencode } from "@opencode-ai/sdk"

console.log("Starting Opencode client...")
const opencode = await createOpencode()
// Now you can use the `client` to interact with the Opencode AI services


console.log(`Server running at ${opencode.server.url}`)