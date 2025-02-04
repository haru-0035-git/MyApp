import { defineConfig } from "vite";
import react from "@vitejs/plugin-react";

// https://vite.dev/config/
export default defineConfig({
  plugins: [react()],
  base: "/Myapp/note-app/", // デプロイ先のパス
  server: {
    host: true, // 外部からのアクセスを許可
    port: 3000, // 任意のポート番号
  },
});
