import { createOpencode } from "@opencode-ai/sdk";
async function main() {
    const { client } = await createOpencode();
    // Try something simple, like listing projects
    const projects = await client.project.list();
    console.log(projects);
}
main().catch(err => console.error(err));
