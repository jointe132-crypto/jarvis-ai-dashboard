# 🤖 Jarvis Agent System

Complete guide to creating, managing, and executing intelligent agents.

## 📖 Agent Architecture

### Agent Structure
```typescript
interface Agent {
  id: string
  userId: string
  name: string
  description?: string
  model: string  // 'gpt-4', 'claude-3', etc.
  systemPrompt: string
  tools: Tool[]
  temperature: number
  maxTokens: number
  isActive: boolean
  createdAt: Date
  updatedAt: Date
}
```

### Tool Structure
```typescript
interface Tool {
  id: string
  name: string
  description: string
  schema: JSONSchema
  handler: string  // Function reference
  isEnabled: boolean
}
```

### Execution Flow
```
User Input
   ↓
Agent receives task
   ↓
LLM generates response with tool calls
   ↓
Tools are executed
   ↓
Results fed back to LLM
   ↓
Final response generated
   ↓
Results returned to user
```

## 🛠️ Available Tools

### Code Execution
```typescript
{
  name: 'code-executor',
  description: 'Execute Python and JavaScript code',
  handler: 'code_executor',
  schema: {
    language: 'string', // 'python' or 'javascript'
    code: 'string',
    timeout: 'number'
  }
}
```

### File Management
```typescript
{
  name: 'file-manager',
  description: 'Read, write, and manage files',
  handler: 'file_manager',
  schema: {
    action: 'string', // 'read', 'write', 'delete', 'list'
    path: 'string',
    content?: 'string'
  }
}
```

### Web Search
```typescript
{
  name: 'web-search',
  description: 'Search the internet',
  handler: 'web_search',
  schema: {
    query: 'string',
    numResults: 'number'
  }
}
```

### Database Query
```typescript
{
  name: 'database-query',
  description: 'Execute database queries',
  handler: 'database_query',
  schema: {
    query: 'string',
    database: 'string'
  }
}
```

### Calculator
```typescript
{
  name: 'calculator',
  description: 'Perform mathematical operations',
  handler: 'calculator',
  schema: {
    expression: 'string'
  }
}
```

## 🎯 Creating an Agent

### Via API
```bash
curl -X POST http://localhost:5000/api/agents \
  -H "Authorization: Bearer token" \
  -H "Content-Type: application/json" \
  -d '{
    "name": "CodeAssistant",
    "model": "gpt-4",
    "systemPrompt": "You are a helpful code assistant.",
    "tools": ["code-executor", "file-manager"],
    "temperature": 0.7,
    "maxTokens": 2000
  }'
```

### Response
```json
{
  "id": "agent_123",
  "name": "CodeAssistant",
  "model": "gpt-4",
  "tools": ["code-executor", "file-manager"],
  "createdAt": "2024-01-10T12:00:00Z"
}
```

## ▶️ Executing an Agent

### Simple Execution
```bash
curl -X POST http://localhost:5000/api/agents/agent_123/execute \
  -H "Authorization: Bearer token" \
  -H "Content-Type: application/json" \
  -d '{
    "task": "Write a Python function to calculate fibonacci",
    "context": {}
  }'
```

### Streaming Execution
```bash
curl -X POST http://localhost:5000/api/agents/agent_123/execute/stream \
  -H "Authorization: Bearer token" \
  --stream
```

### Response
```json
{
  "executionId": "exec_456",
  "status": "running",
  "result": "...",
  "toolCalls": [
    {
      "tool": "code-executor",
      "input": { "code": "...", "language": "python" },
      "result": "..."
    }
  ],
  "completedAt": "2024-01-10T12:01:00Z"
}
```

## 🔄 Multi-Agent Orchestration

### Parallel Execution
```typescript
const results = await Promise.all([
  executeAgent(agent1Id, task),
  executeAgent(agent2Id, task),
  executeAgent(agent3Id, task)
])
```

### Sequential Execution
```typescript
let result = await executeAgent(agent1Id, task)
result = await executeAgent(agent2Id, { ...result })
result = await executeAgent(agent3Id, { ...result })
```

### Hierarchical Execution
```typescript
const masterAgent = await getAgent('master_agent_id')
const specialistAgents = ['code_agent', 'data_agent', 'ui_agent']

// Master delegates to specialists
const delegatedResults = await masterAgent.delegate(specialistAgents, task)
```

## 🛡️ Safety & Approval System

### Setting Approval Requirements
```typescript
const agent = {
  name: 'SystemAgent',
  approvalRequired: true,
  approvalLevel: 'high', // 'low', 'medium', 'high'
  allowedTools: ['safe-tool-1', 'safe-tool-2']
}
```

### Approval Workflow
```
Agent generates action
   ↓
Action marked for approval
   ↓
User receives notification
   ↓
User reviews & approves/rejects
   ↓
Action executed or cancelled
```

### Blocking Actions
```typescript
const blockedActions = [
  'DELETE_ALL_FILES',
  'FORMAT_DISK',
  'SEND_EMAIL_TO_ALL'
]

if (blockedActions.includes(action)) {
  await requireApproval(execution)
}
```

## 📊 Agent Monitoring

### Execution History
```bash
curl http://localhost:5000/api/agents/agent_123/history \
  -H "Authorization: Bearer token"
```

### Metrics
```json
{
  "totalExecutions": 150,
  "successRate": 0.95,
  "avgExecutionTime": 2500,
  "errorRate": 0.05,
  "lastExecution": "2024-01-10T12:00:00Z"
}
```

## 🔧 Custom Tool Creation

### Define Tool Schema
```typescript
const customTool = {
  name: 'email-sender',
  description: 'Send emails',
  schema: {
    type: 'object',
    properties: {
      to: { type: 'string' },
      subject: { type: 'string' },
      body: { type: 'string' }
    },
    required: ['to', 'subject', 'body']
  }
}
```

### Implement Handler
```typescript
export async function emailSender(input: {
  to: string
  subject: string
  body: string
}) {
  // Send email logic
  return { success: true, messageId: '...' }
}
```

### Register Tool
```bash
curl -X POST http://localhost:5000/api/tools \
  -H "Authorization: Bearer token" \
  -d '{
    "name": "email-sender",
    "description": "Send emails",
    "schema": { ... }
  }'
```

## 📈 Advanced Patterns

### Router Agent
```typescript
// Routes tasks to specialized agents
const routerAgent = new Agent({
  name: 'Router',
  model: 'gpt-4',
  systemPrompt: `You route tasks to the right specialist.
    Available specialists: ${specialistAgents.map(a => a.name).join(', ')}
  `,
  tools: ['delegate-to-agent']
})
```

### Chain of Thought
```typescript
// Agent thinks step-by-step
const agent = new Agent({
  systemPrompt: `Think step-by-step:
    1. Break down the task
    2. Plan your approach
    3. Execute the plan
    4. Verify the results
  `
})
```

### Self-Correcting Agent
```typescript
// Agent can review and fix its own output
const agent = new Agent({
  tools: ['self-review', 'code-executor', 'file-manager'],
  systemPrompt: `If you make a mistake, review it and fix it.
    Always verify your work before returning.
  `
})
```

## 🚀 Best Practices

1. **Use specific system prompts** - Clear instructions lead to better results
2. **Limit tool scope** - Give agents only necessary tools
3. **Set timeouts** - Prevent infinite loops
4. **Monitor execution** - Track all agent actions
5. **Require approval** - For sensitive operations
6. **Use streaming** - Better UX for long operations
7. **Handle errors gracefully** - Retry with different approaches
8. **Log everything** - For debugging and auditing

## 🔗 Related Documentation

- [Architecture Guide](./ARCHITECTURE.md)
- [API Documentation](./API.md)
- [Deployment Guide](./DEPLOYMENT.md)
