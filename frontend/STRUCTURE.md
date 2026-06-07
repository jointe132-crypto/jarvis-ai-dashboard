frontend/
├── app/
│   ├── layout.tsx
│   ├── page.tsx
│   ├── dashboard/
│   │   └── page.tsx
│   ├── agents/
│   │   ├── page.tsx
│   │   ├── [id]/
│   │   │   └── page.tsx
│   │   └── create/
│   │       └── page.tsx
│   ├── models/
│   │   └── page.tsx
│   ├── chat/
│   │   └── page.tsx
│   └── settings/
│       └── page.tsx
├── components/
│   ├── ui/
│   │   ├── button.tsx
│   │   ├── card.tsx
│   │   ├── dialog.tsx
│   │   └── input.tsx
│   ├── common/
│   │   ├── Navbar.tsx
│   │   ├── Sidebar.tsx
│   │   └── Footer.tsx
│   ├── dashboard/
│   │   ├── DashboardHome.tsx
│   │   ├── StatsCard.tsx
│   │   └── RecentActivity.tsx
│   └── agents/
│       ├── AgentList.tsx
│       ├── AgentCard.tsx
│       └── AgentForm.tsx
├── hooks/
│   ├── useWebSocket.ts
│   ├── useAgent.ts
│   └── useAPI.ts
├── lib/
│   ├── api.ts
│   ├── websocket.ts
│   └── utils.ts
├── store/
│   ├── agentStore.ts
│   ├── modelStore.ts
│   └── uiStore.ts
├── types/
│   └── index.ts
├── styles/
│   └── globals.css
├── public/
│   ├── logo.svg
│   └── favicon.ico
├── .env.example
├── .env.local (git ignored)
├── package.json
├── tsconfig.json
├── next.config.js
├── tailwind.config.js
├── postcss.config.js
├── Dockerfile
└── README.md
